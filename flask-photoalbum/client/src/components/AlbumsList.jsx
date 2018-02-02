import React from 'react';

import './AlbumsList.css';
import ImageRow from './components/ImageRow';


const Timestamp = require('react-timestamp');

class AlbumsList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      albumID: -1,
      imgID: -1,
      imgHovered: false,
      imgClicked: false
    }
  }
  albumHover(albumindex) {
    this.setState({
      albumID: this.state.albumID === albumindex ? -1 : albumindex,
    });
  }
  albumMouseLeave() {
    this.setState({
      albumID: -1,
      imgHovered: false,
      imgClicked: false
    });
  }
  imgHover(imgindex) {
    this.setState({
      imgID: imgindex,
      imgHovered: true
    });
  }
  imgMouseLeave(imgindex) {
    var myindex = this.state.imgID;
    if (imgindex !== myindex) {
      this.setState({
        imgID: -1,
        imgHovered: false,
        imgClicked: false
      });
    }
  }
  openImg() {
    this.setState({
      imgClicked: true,
      imgHovered: false,
      albumID: -1,
      imgID: -1,
    });
  }
  closeImg() {
    this.setState({
      imgClicked: false,
      imgHovered: true,
      albumID: -1,
      imgID: -1
    });
  }

  render() {
    return (
      <div className="albumSpace">
        {
          this.props.albums.map((album, albumindex) => {
            return (
              <div
                key={albumindex}
                onMouseEnter={this.albumHover.bind(this, albumindex)}
                onMouseLeave={this.albumMouseLeave.bind(this)}
                className="container album fill"
              >
                <div className="header row">
                  <h2>{album.title}</h2>
                  <h6>{album.images.length} files - <Timestamp time={album.created_at} format='full' /> - <i><Timestamp time={album.created_at} format='ago' includeDay={true} precision={2} autoUpdate={60} /></i></h6>
                  <h5>{album.description}</h5>
                </div>
                <ImageRow albums={this.props.albums} albumkey={albumindex} />
              </div>
            )
          })
        }
      </div>
    )
  }
};

export default AlbumsList;

import React from 'react';

import './AlbumsList.css';
import ImageRow from './ImageRow';


const Timestamp = require('react-timestamp');

class AlbumsList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      albumID: -1
    }
  }
  albumHover(albumindex) {
    this.setState({
      albumID: this.state.albumID === albumindex ? -1 : albumindex,
    });
  }
  albumMouseLeave() {
    this.setState({
      albumID: -1
    });
  }

  render() {
    return (
      <div className="albumSpace" id="albumSpace">
        {
          this.props.albums.map((album, albumindex) => {
            return (
                <div
                  onMouseEnter={this.albumHover.bind(this, albumindex)}
                  onMouseLeave={this.albumMouseLeave.bind(this)}
                  className="container album"
                  key={albumindex}
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

import React from 'react';

import './AlbumsList.css';

const Timestamp = require('react-timestamp');

class AlbumsList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      albumHovered: -1,
      imgHovered: -1,
      imgClicked: false
    }
  }
  albumHover(albumindex) {
    this.setState({
      albumHovered: this.state.albumHovered === albumindex ? -1 : albumindex
    });
  }
  imgHover(imgindex) {
    this.setState({
      imgHovered: this.state.imgHovered === imgindex ? -1 : imgindex,
    });
  }
  openImg() {
    this.setState({
      imgClicked: true
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
                className="container album fill"
              >
                <div className="header row">
                  <h2>{album.title}</h2>
                  <h6>{album.images.length} files - <Timestamp time={album.created_at} format='full' /> - <i><Timestamp time={album.created_at} format='ago' includeDay={true} precision={2} autoUpdate={60} /></i></h6>
                  <h5>{album.description}</h5>
                </div>
                <div className="slideshow row align-items-center">
                  <div className="arrow col-md-1 text-center">
                    <img src={require('./static/arrow-left.png')} width={50} alt="arrow" />
                  </div>
                  <div className="allImages col-md-10 text-center">
                  {
                    album.images.slice(0, 5).map((i, imgindex) => {
                      const {imgHovered, albumHovered, imgClicked} = this.state
                      var zoomedImg = (imgHovered === imgindex && albumHovered === albumindex) ? "zoomed" : "";
                      var openImg = (imgHovered === imgindex && albumHovered === albumindex && imgClicked === true) ? "opened" : "";
                      var imgClass = `imageContainer ${openImg} ${zoomedImg}`
                      return (
                        <div className={imgClass} key={imgindex}>
                          {imgHovered === imgindex && albumHovered === albumindex && <img className="expand" onClick={this.openImg.bind(this)} src={require('./static/expand.png')} width={45} alt="arrow" />}
                          <img className="image" onMouseEnter={this.imgHover.bind(this, imgindex)} src={i} alt='album img' />
                        </div>
                      )
                    })
                  }
                  </div>
                  <div className="arrow col-md-1 text-center">
                    <img src={require('./static/arrow-right.png')} width={50} alt="arrow" />
                  </div>
                </div>
              </div>
            )
          })
        }
      </div>
    )
  }
};

export default AlbumsList;

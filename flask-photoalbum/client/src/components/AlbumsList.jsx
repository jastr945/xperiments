import React from 'react';

import './AlbumsList.css';

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
      imgHovered: true
    });
  }
  imgHover(imgindex) {
    this.setState({
      imgID: this.state.imgID === imgindex ? -1 : imgindex,
      imgHovered: true
    });
  }
  openImg(imgindex) {
    var myindex = this.state.imgID;
    if (imgindex === myindex) {
      this.setState({
        imgHovered: false,
        imgClicked: true
      });
    }
  }
  imgMouseLeave(imgindex) {
    var myindex = this.state.imgID;
    if (imgindex === myindex) {
      this.setState({
        imgClicked: false
      });
    }
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
                      const {imgID, albumID, imgClicked, imgHovered} = this.state
                      var zoomedImg = (imgID === imgindex && albumID === albumindex && imgClicked === false && imgHovered === true) ? "zoomed" : "";
                      var openImg = (imgID === imgindex && albumID === albumindex && imgClicked === true && imgHovered === false) ? "opened" : "";
                      var imgClass = `imageContainer ${openImg} ${zoomedImg}`
                      console.log(imgID, albumID, imgClicked, imgHovered);
                      return (
                        <div className={imgClass} key={imgindex}>
                          {imgID === imgindex && albumID === albumindex && imgClicked === false && imgHovered === true && <img className="icon" src={require('./static/expand.png')} width={45} alt="arrow" />}

                          {imgID === imgindex && albumID === albumindex && imgClicked === true && imgHovered === false && <img className="icon" onClick={this.closeImg.bind(this)} src="http://icons.iconarchive.com/icons/graphicloads/100-flat/256/close-icon.png" width={15} alt="close" />}

                          <img className="image" onClick={this.openImg.bind(this, imgindex)} onMouseEnter={this.imgHover.bind(this, imgindex)} onMouseLeave={this.imgMouseLeave.bind(this, imgindex)} src={i} alt='album img' />
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

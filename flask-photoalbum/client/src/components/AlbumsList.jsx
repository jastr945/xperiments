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
      imgClicked: false,
      start: 0,
      finish: 5
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
  leftClick() {
    let start = this.state.start;
    let finish = this.state.finish;
    if (start > 0 && finish > 0) {
      this.setState({
        start: start - 5,
        finish: finish - 5,
      });
    }
  }
  rightClick() {
    let start = this.state.start;
    let finish = this.state.finish;
    if (finish < this.props.albums.images.length) {
      this.setState({
        start: start + 5,
        finish: finish + 5
      });
    }
  }
  render() {
    var startindex = this.state.start;
    var finishindex = this.state.finish;
    console.log(startindex, finishindex);
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
                <div className="slideshow row">
                  <div className="arrow col-md-1 text-center" onClick={this.leftClick.bind(this)}>
                    <img src={require('./static/arrow-left.png')} width={50} alt="arrow" />
                  </div>
                  {
                    album.images.slice(startindex, finishindex).map((i, imgindex) => {
                      const {imgID, albumID, imgClicked, imgHovered} = this.state
                      var zoomedImg = (imgID === imgindex && albumID === albumindex && imgClicked === false && imgHovered === true) ? "zoomed" : "";
                      var openImg = (imgID === imgindex && albumID === albumindex && imgClicked === true) ? "opened" : "";
                      var imgClass = `imageContainer ${openImg} ${zoomedImg}`
                      console.log(imgID, albumID, imgClicked, imgHovered);
                      return (
                        <div className={imgClass} key={imgindex}>
                          {imgID === imgindex && albumID === albumindex && imgClicked === false && imgHovered === true && <img className="icon" onClick={this.openImg.bind(this)} onMouseEnter={this.imgHover.bind(this, imgindex)} src={require('./static/expand.png')} width={30} alt="expand" />}

                          {imgID === imgindex && albumID === albumindex && imgClicked === true && <img className="icon" onClick={this.closeImg.bind(this)} src="http://icons.iconarchive.com/icons/graphicloads/100-flat/256/close-icon.png" width={15} alt="close" />}

                          <img className="image" onMouseEnter={this.imgHover.bind(this, imgindex)} onMouseLeave={this.imgMouseLeave.bind(this, imgindex)} src={i} alt='album img' />
                        </div>
                      )
                    })
                  }
                  <div className="arrow col-md-1 text-center" onClick={this.rightClick.bind(this)}>
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

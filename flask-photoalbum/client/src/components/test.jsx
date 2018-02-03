import React from 'react';

import './ImageRow.css';

class AlbumsList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      start: 0,
      finish: 5
    }
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
  rightClick(length) {
    let start = this.state.start;
    let finish = this.state.finish;
    if (finish < length) {
      this.setState({
        start: start + 5,
        finish: finish + 5
      });
    }
  }

  render() {
    var startindex = this.state.start;
    var finishindex = this.state.finish;
    var length = this.props.albums[this.props.albumkey].images.length;
    return (
      <div className="slideshow row">
        <div className="arrow col-md-1 text-center" onClick={this.leftClick.bind(this)}>
          <img src={require('./static/arrow-left.png')} width={50} alt="arrow" />
        </div>
        {
          this.props.albums[this.props.albumkey].images.slice(startindex, finishindex).map((i, imgindex) => {
            const {imgID, albumID, imgClicked, imgHovered} = this.state
            var zoomedImg = (imgID === imgindex && albumID === albumindex && imgClicked === false && imgHovered === true) ? "zoomed" : "";
            var openImg = (imgID === imgindex && albumID === albumindex && imgClicked === true) ? "opened" : "";
            var imgClass = `imageContainer ${openImg} ${zoomedImg}`
            return (
              <div className={imgClass} key={imgindex}>
                {imgID === imgindex && albumID === albumindex && imgClicked === false && imgHovered === true && <img className="icon" onClick={this.openImg.bind(this)} onMouseEnter={this.imgHover.bind(this, imgindex)} src={require('./static/expand.png')} width={30} alt="expand" />}

                {imgID === imgindex && albumID === albumindex && imgClicked === true && <img className="icon" onClick={this.closeImg.bind(this)}  src="http://icons.iconarchive.com/icons/graphicloads/100-flat/256/close-icon.png" width={15} alt="close" />}

                <img className="image" onMouseEnter={this.imgHover.bind(this, imgindex)} onMouseLeave={this.imgMouseLeave.bind(this, imgindex)} src={i} alt='album img' />
              </div>
            )
          })
        }
        <div className="arrow col-md-1 text-center" onClick={this.rightClick.bind(this, length)}>
          <img src={require('./static/arrow-right.png')} width={50} alt="arrow" />
        </div>
      </div>
    )
  }
}

export default ImageRow;

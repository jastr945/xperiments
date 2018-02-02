import React from 'react';

import './ImageRow.css';

class ImageRow extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      start: 0,
      finish: 5,
      fadedleft: true,
      fadedright: false
    }
  }

  leftClick() {
    let start = this.state.start;
    let finish = this.state.finish;
    if (start > 0 && finish > 0) {
      this.setState({
        start: start - 5,
        finish: finish - 5,
        fadedright: false
      });
    } else {
      this.setState({
        fadedleft: true
      });
    }
  }
  
  rightClick(length) {
    let start = this.state.start;
    let finish = this.state.finish;
    if (finish < length) {
      this.setState({
        start: start + 5,
        finish: finish + 5,
        fadedleft: false
      });
    } else {
      this.setState({
        fadedright: true
      });
    }
  }

  render() {
    const {start, finish, fadedleft, fadedright} = this.state
    const left = fadedleft ? "arrow-left col-md-1 text-center faded-left" : "arrow-left col-md-1 text-center";
    const right = fadedright ? "arrow-right col-md-1 text-center faded-right" : "arrow-right col-md-1 text-center";
    var length = this.props.albums[this.props.albumkey].images.length;
    return (
      <div className="slideshow row">
        <div className={left} onClick={this.leftClick.bind(this)}>
          <img src={require('./static/arrow-left.png')} width={50} alt="arrow" />
        </div>
        {
          this.props.albums[this.props.albumkey].images.slice(start, finish).map((i, imgindex) => {
            return (
              <div className="" key={imgindex}>
                <img className="image" src={i} alt='album img' />
              </div>
            )
          })
        }
        <div className={right} onClick={this.rightClick.bind(this, length)}>
          <img src={require('./static/arrow-right.png')} width={50} alt="arrow" />
        </div>
      </div>
    )
  }
}

export default ImageRow;

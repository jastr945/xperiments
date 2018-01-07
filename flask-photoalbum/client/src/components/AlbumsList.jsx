import React from 'react';

import './AlbumsList.css';

const Timestamp = require('react-timestamp');

class AlbumsList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isHovered: -1
    }
  }
  handleHover(index) {
    this.setState({
        isHovered: this.state.isHovered === index ? -1 : index,
    });
  }
  render() {
    return (
      <div className="albumSpace">
        {
          this.props.albums.map((album) => {
            return (
              <div
                key={album.id}
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
                    album.images.slice(0, 5).map((i, index) => {
                      const { isHovered } = this.state
                      return (
                        <div className="imageContainer" key={index}>
                          {isHovered === index && <img className="expand" src={require('./static/expand.png')} width={45} alt="arrow" />}
                          <img className="image" onMouseEnter={this.handleHover.bind(this, index)} src={i} alt='album img' height={120} />
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

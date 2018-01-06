import React from 'react';

import './AlbumsList.css';

const Timestamp = require('react-timestamp');

const AlbumsList = (props) => {
  return (
    <div className="albumSpace">
      {
        props.albums.map((album) => {
          return (
            <div
              key={album.id}
              className="container album"
            >
              <h2>{album.title}</h2>
              <h6>{album.images.length} files - <Timestamp time={album.created_at} format='full' /> - <i><Timestamp time={album.created_at} format='ago' includeDay={true} precision={2} autoUpdate={60} /></i></h6>
              <h5>{album.description}</h5>
              <div className="row">
                <div className="arrow col-md-1 text-center">
                  <img src={require('./static/arrow-left.png')} width={50} alt="arrow" />
                </div>
                <div className="allImages col-md-10 text-center">
                {
                  album.images.map((i) => {
                    return (
                      <img className="image" key={i.id} src={i} alt='album img' height={120} />
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
};

export default AlbumsList;

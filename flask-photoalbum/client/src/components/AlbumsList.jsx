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
              {album.title} - {album.description} - <Timestamp time={album.created_at} format='full' /> - <Timestamp time={album.created_at} format='ago' includeDay={true} precision={2} autoUpdate={60} /> - {album.images.length} files
              <div className="col-md-12">
                <div className="row">
                  {
                    album.images.map((i) => {
                      return (
                        <div
                          className="image col-md-2"
                          key={i.id}
                        >
                          <img src={i} alt='album img' width={200} height={120} />
                        </div>
                      )
                    })
                  }
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

import React from 'react';

const Timestamp = require('react-timestamp');

const AlbumsList = (props) => {
  return (
    <div>
      {
        props.albums.map((album) => {
          return (
            <h4
              key={album.id}
              className="well"
            >{album.title} - {album.description} - <Timestamp time={album.created_at} format='full' /> - <Timestamp time={album.created_at} format='ago' includeDay={true} precision={2} autoUpdate={60} />
            </h4>
          )
        })
      }
    </div>
  )
};

export default AlbumsList;

import React from 'react';

const AddAlbum = (props) => {
  return (
    <form onSubmit={(event) => props.addAlbum(event)} method="POST" encType="multipart/form-data">
      <div className="form-group">
        <input
          className="form-control input-lg"
          type="file"
          multiple
          onChange={props.handleFileChange}
        />
      </div>
      <div className="form-group">
        <input
          name="title"
          className="form-control input-lg"
          type="text"
          placeholder="Enter a title..."
          required
          value={props.title}
          onChange={props.handleChange}
        />
      </div>
      <div className="form-group">
        <input
          name="description"
          className="form-control input-lg"
          type="description"
          placeholder="Enter some description..."
          required
          value={props.description}
          onChange={props.handleChange}
        />
      </div>
      <input
        type="submit"
        className="btn btn-primary btn-lg btn-block"
        value="Submit"
      />
    </form>
  )
}

export default AddAlbum;

import React from 'react';

import './AddAlbum.css';


const AddAlbum = (props) => {
  return (
    <div class="jumbotron">
      <div class="jumbo container">
        <div class="col-md-6">
          <form onSubmit={(event) => props.addAlbum(event)} method="POST" encType="multipart/form-data">
            <div className="form-group">
              <input
                className="inputfile form-control input-lg"
                name="photos"
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
        </div>
      </div>
    </div>
  )
}

export default AddAlbum;

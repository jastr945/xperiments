import React, { Component } from 'react';
import axios from 'axios';

import AlbumsList from './components/AlbumsList';
import AddAlbum from './components/AddAlbum';

class App extends Component {
  constructor() {
    super()
    this.state = {
      error: null,
      albums: [],
      title: '',
      description: '',
      file: null
    }
  }
  componentDidMount() {
    this.getAlbums();
  }
  getAlbums() {
    axios.get('http://192.168.0.109:5001/albums')
    .then((res) => { this.setState({ albums: res.data.data.albums }); })
    .catch((err) => { console.log(err); })
  }
  addAlbum(event) {
    event.preventDefault();
    var formData = new FormData();
    for (let i=0; i < this.state.file.length; i++) {
      formData.append('photos', this.state.file[i]);
    }
    formData.append('title', this.state.title);
    formData.append('description', this.state.description);
    console.log(formData);
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
    axios.post('http://192.168.0.109:5001/albums', formData, config)
    .then((res) => {
      this.getAlbums();
      this.setState({ title: '', description: '', file: null });
    })
    .catch((err) => { console.log(err); })
  }
  handleFileChange(event) {
    this.setState({
      file: Array.from(event.target.files)
    });
  }
  handleChange(event) {
    var obj = {};
    obj[event.target.name] = event.target.value;
    this.setState(obj);
  }
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <br/>
            <h1>React + Flask Photo Album</h1>
            <hr/><br/>
            <AddAlbum
              title={this.state.title}
              description={this.state.description}
              file={this.state.file}
              handleChange={this.handleChange.bind(this)}
              handleFileChange={this.handleFileChange.bind(this)}
              addAlbum={this.addAlbum.bind(this)}
            />
            <br/>
          </div>
        </div>
        <div className="row">
          <div className="col-md-12">
            <AlbumsList albums={this.state.albums}/>
          </div>
        </div>
      </div>
    )
  }
}

export default App;
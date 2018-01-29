import React, { Component } from 'react';
import axios from 'axios';

import AlbumsList from './components/AlbumsList';
import AddAlbum from './components/AddAlbum';
import Navbar from './components/Navbar';
import './index.css';

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
      <body>
        <Navbar />
          <AddAlbum
            title={this.state.title}
            description={this.state.description}
            file={this.state.file}
            handleChange={this.handleChange.bind(this)}
            handleFileChange={this.handleFileChange.bind(this)}
            addAlbum={this.addAlbum.bind(this)}
          />
          <div className="container">
            <AlbumsList albums={this.state.albums}/>
          </div>
      </body>
    )
  }
}

export default App;

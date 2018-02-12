import React, { Component } from 'react';
import axios from 'axios';

import AlbumsList from './components/AlbumsList';
import UploadButton from './components/UploadButton';
import Form from './components/AddAlbum';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import './index.css';

class App extends Component {
  constructor() {
    super()
    this.state = {
      error: null,
      albums: [],
      title: '',
      description: '',
      file: null,
      formOpened: false,
      loginErrorVisible: false
    }
    this.openForm = this.openForm.bind(this);
  }
  componentDidMount() {
    this.getAlbums();
    this.getGoogleData();
  }
  getAlbums() {
    axios.get('http://192.168.0.109:5001/albums')
    .then((res) => { this.setState({ albums: res.data.data.albums }); })
    .catch((err) => { console.log(err); })
  }
  getGoogleData() {
    let currentURL = window.location.href;
    console.log(currentURL);
    let token = currentURL.match(/[^\/]*$/);
    console.log(token);
    let baseURL = "/login/authorized?code=4/"
    let newURL = baseURL + token;
    console.log(newURL);
    fetch(newURL, {})
    .then(response => console.log(response.json()))
    .catch(error => console.log(error))
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
    .catch((err) => {
      if( err.response ){
        console.log(err.data.message);
      } else {console.log(err);}
    })
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
  openForm() {
    this.setState({
      formOpened: true
    });
  }
  render() {
    const formOpened = this.state.formOpened;
    var bg = require('./components/static/landscape.jpg')
    return (
      <div className="app">
        <Navbar />
        <div className="jumbotron"  style ={{backgroundImage: "url("+bg+")"}} >
          <div className="jumbo container">
            {formOpened ? (
              <Form
                title={this.state.title}
                description={this.state.description}
                file={this.state.file}
                handleChange={this.handleChange.bind(this)}
                handleFileChange={this.handleFileChange.bind(this)}
                addAlbum={this.addAlbum.bind(this)}
                error={this.state.loginErrorVisible}
              />
            ) : (
              <UploadButton openForm={this.openForm} />
            )}
          </div>
        </div>
        <div className="container">
          <AlbumsList albums={this.state.albums}/>
        </div>
        <Footer />
      </div>
    )
  }
}

export default App;

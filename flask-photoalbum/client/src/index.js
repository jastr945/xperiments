import React, { Component } from 'react';
import ReactDOM from 'react-dom';
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
      photos: ''
    }
  }
  componentDidMount() {
    this.getAlbums();
  }
  getAlbums() {
    axios.get('http://localhost:5001/albums')
    .then((res) => { this.setState({ albums: res.data.data.albums }); })
    .catch((err) => { console.log(err); })
  }
  addAlbum(event) {
    event.preventDefault();
    console.log(this.state.photos)
    const data = {
      title: this.state.title,
      description: this.state.description,
      photos: this.state.photos
    }
    axios.post('http://localhost:5001/albums', data)
    .then((res) => {
      this.getAlbums();
      this.setState({ title: '', description: '', photos: '' });
    })
    .catch((err) => { console.log(err); })
  }
  handleChange(event) {
    try {
      const obj = {};
      if (obj[event.target.name] === 'photos') {
        for (let size=0; size < event.target.files.length; size++) {
          console.log("Image list length",event.target.files.length);
          let images = [];
          images.push(event.target.files[size]);
          obj[event.target.name] = images;
        }
      } else {
        obj[event.target.name] = event.target.value;
      }
      this.setState(obj);
      console.log(obj);
    } catch (error) {
      this.setState({ error });
    }
  }
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <br/>
            <h1>Photo Album</h1>
            <hr/><br/>
            <AddAlbum
              title={this.state.title}
              description={this.state.description}
              photos={this.state.photos}
              handleChange={this.handleChange.bind(this)}
              addAlbum={this.addAlbum.bind(this)}
            />
            <br/>
            <AlbumsList albums={this.state.albums}/>
          </div>
        </div>
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

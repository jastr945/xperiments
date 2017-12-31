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
    console.log(this.state.file)
    const data = {
      title: this.state.title,
      description: this.state.description,
      file: this.state.file
    }
    const config = {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    }
    axios.post('http://192.168.0.109/albums', data, config)
    .then((res) => {
      this.getAlbums();
      this.setState({ title: '', description: '', file: null });
    })
    .catch((err) => { console.log(err); })
  }
  handleFileChange(event) {
    this.setState({
      file: event.target.files[0]
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
            <h1>Photo Album</h1>
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

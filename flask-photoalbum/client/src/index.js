import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import AlbumsList from './components/AlbumsList';
import AddAlbum from './components/AddAlbum';


class App extends Component {
  constructor() {
    super()
    this.state = {
      albums: [],
      title: '',
      description: ''
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
    const data = {
      title: this.state.title,
      description: this.state.description
    }
    axios.post('http://localhost:5001/albums', data)
    .then((res) => {
      this.getAlbums();
      this.setState({ title: '', description: '' });
    })
    .catch((err) => { console.log(err); })
  }
  handleChange(event) {
    const obj = {};
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

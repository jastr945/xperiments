import React, { Component } from 'react';
import axios from 'axios';

import './Navbar.css';


class Navbar extends Component  {
  constructor() {
    super()
    this.state = {
      user: null
    }
  }
  componentDidMount() {
    this.getUser();
  }
  getUser() {
    axios.get('http://192.168.0.109.nip.io:5001')
    .then((res) => { this.setState({ user: res.data.data }); console.log(res.data.data); })
    .catch((err) => { console.log(err); })
    const config = {
      headers: {
        'Access-Control-Allow-Origin': '*'
      }
    }
  }
  render() {
    return (
      <nav className="navbar navbar-inverse navbar-static-top">
    		<div className="navbar-header">
    			<button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
    				<span className="sr-only">Toggle navigation</span>
    				<span className="icon-bar"></span>
    				<span className="icon-bar"></span>
            <span className="icon-bar"></span>
    			</button>
    			<a className="navbar-brand" href="#">React + Flask Photo Album</a>
    		</div>
    		<div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
    			<ul className="nav navbar-nav navbar-right">
    				<li><a href="https://github.com/jastr945" target="_blank" >About</a></li>
    				<li><a href="http://polina.mee.how/" target="_blank" >Contact</a></li>
            <li><a href="http://192.168.0.109.nip.io:5001/login">Sign in</a></li>
            <li>{this.state.user}</li>

    			</ul>
      	</div>
      </nav>
    )
  }
}

export default Navbar;

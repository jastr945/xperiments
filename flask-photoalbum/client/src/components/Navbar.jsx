import React, { Component } from 'react';
import { Navbar, Nav, NavItem } from 'react-bootstrap';

import './Navbar.css';


class Header extends Component  {
  constructor() {
    super()
    this.state = {
      useremail: null,
      userpic: null
    }
  }
  componentDidMount() {
    this.getGoogleData();
  }
  getGoogleData() {
    var pathname = /^(?:\w+\:\/\/)?([^\/]+)(.*)$/.exec(window.location.href);
    var path = pathname[2];
    var finalurl = 'http://192.168.0.107.nip.io:5001' + path;
    console.log(finalurl);
    fetch(finalurl, {
    method: 'GET',
    credentials: 'include',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    },
    })
    .then(res => {
      console.log(res);
      return res.json();
      this.setState({
        useremail: res.data.email,
        userpic: res.data.picture
      });
    })
    .catch(error => console.log(error))
  }
  render() {
    return (
      <Navbar inverse fluid className="navbar">
        <Navbar.Header>
          <Navbar.Brand className="navbar-brand">
            <a href="#">React + Flask Photo Album</a>
          </Navbar.Brand>
          <Navbar.Toggle />
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav pullRight>
            <NavItem eventKey={1} href="https://github.com/jastr945" target="_blank">About</NavItem>
            <NavItem eventKey={2} href="http://polina.mee.how/" target="_blank">Contact</NavItem>
            {!this.state.useremail && <NavItem eventKey={3} href="http://192.168.0.107.nip.io:5001/login">Sign in</NavItem>}
            {this.state.useremail && <NavItem>{this.state.useremail} | <img src={this.state.userpic} height="22px" width="22px"/></NavItem>}
            {this.state.useremail && <NavItem eventKey={3} href="http://192.168.0.107.nip.io:5001/logout">Log out</NavItem>}
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}

export default Header;

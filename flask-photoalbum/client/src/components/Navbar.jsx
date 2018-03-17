import React, { Component } from 'react';
import { Navbar, Nav, NavItem } from 'react-bootstrap';

import './Navbar.css';


class Header extends Component  {
  constructor() {
    super()
    this.state = {
      useremail: null,
      userpic: 'https://github.com/jastr945/PDXclass/blob/master/portfolio/myportfolio/portfoliopages/static/portfoliopages/img/pofi.jpg?raw=true'
    }
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
            {this.state.useremail && <NavItem eventKey={3}>Log out</NavItem>}
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}

export default Header;

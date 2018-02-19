import React, { Component } from 'react';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem } from 'react-bootstrap';

import './Navbar.css';


class Header extends Component  {
  constructor() {
    super()
    this.state = {
      useremail: ''
    }
  }
  render() {
    return (
      <Navbar>
        <Navbar.Header>
          <Navbar.Brand>
            <a href="#">React + Flask Photo Album</a>
          </Navbar.Brand>
          <Navbar.Toggle />
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav pullRight>
            <NavItem eventKey={1} href="https://github.com/jastr945" target="_blank">About</NavItem>
            <NavItem eventKey={2} href="http://polina.mee.how/" target="_blank">Contact</NavItem>
            <NavItem eventKey={3} href="http://192.168.0.109.nip.io:5001/login">Sign in</NavItem>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}

export default Header;

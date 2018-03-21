import React, { Component } from 'react';
import { Navbar, Nav, NavItem } from 'react-bootstrap';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

import './Navbar.css';


class Header extends Component  {
  constructor() {
    super()
    this.state = {
      useremail: null,
      userpic: null
    }
    this.responseGoogle = this.responseGoogle.bind(this);
    this.logout = this.logout.bind(this);
  }
  responseGoogle = (response) => {
    console.log('login');
    console.log(response.profileObj);
    this.setState({
      useremail: response.profileObj.email,
      userpic: response.profileObj.imageUrl
    });
  }
  logout = () => {
    console.log('logout');
    this.setState({
      useremail: null,
      userpic: null
    });
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
            {!this.state.useremail && <NavItem eventKey={3}>
            <GoogleLogin
              clientId="418257197191-75oafj28gkn84pj7ebgvt54av0vtt7br.apps.googleusercontent.com"
              buttonText="Login"
              onSuccess={this.responseGoogle}
              onFailure={this.responseGoogle}
              offline={true}
              approvalPrompt="force"
              responseType="id_token"
              isSignedIn={false}
            />
            </NavItem>}
            {this.state.useremail && <NavItem>{this.state.useremail} | <img src={this.state.userpic} height="22px" width="22px"/></NavItem>}
            {this.state.useremail && <NavItem eventKey={3}>
              <GoogleLogout buttonText="Logout" onLogoutSuccess={this.logout} />
            </NavItem>}
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}

export default Header;

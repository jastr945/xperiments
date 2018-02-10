import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Link, Switch, Route, Redirect } from 'react-router-dom';


import App from './App.jsx';

ReactDOM.render((
  <BrowserRouter>
    <Route path="/" component={App}>
    </Route>
  </BrowserRouter>
), document.getElementById('root'))

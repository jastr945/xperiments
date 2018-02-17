import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

import Login from './components/Login';
import NotFound from './components/NotFound';


const Routes = () => (
  <BrowserRouter >
    <Switch>
      <Route path="/login" component={Login}/>
      <Route path="*" component={NotFound}/>
    </Switch>
  </BrowserRouter>
);

export default Routes;

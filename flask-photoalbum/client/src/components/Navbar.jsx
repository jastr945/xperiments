import React, { Component } from 'react';


const Navbar = (props) => {
  return (
    <nav class="navbar navbar-inverse navbar-static-top">
    	<div class="container">
    		<div class="navbar-header">
    			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
    				<span class="sr-only">Toggle navigation</span>
    				<span class="icon-bar"></span>
    				<span class="icon-bar"></span>
            <span class="icon-bar"></span>
    			</button>
    			<a class="navbar-brand" href="#"><h1>React + Flask Photo Album</h1></a>
    		</div>
    		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
    			<ul class="nav navbar-nav navbar-right">
    				<li><a href="https://github.com/jastr945" target="_blank" >About</a></li>
    				<li><a href="http://polina.mee.how/" target="_blank" >Contact</a></li>
    			</ul>
    		</div>
    	</div>
    </nav>
  )
}

export default Navbar;

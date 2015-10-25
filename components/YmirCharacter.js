// search.js
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./NavBar');
var Catagory = require('./Catagory');


ReactDOM.render(
  <div>
  	<NavBar />
  	<Catagory catagory={'Characters'}/>
  </div>,
  document.getElementById('react')
);
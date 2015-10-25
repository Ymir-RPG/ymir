// search.js
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./NavBar');
var Category = require('./Category');


ReactDOM.render(
  <div>
  	<NavBar />
  	<Category category={'Places'}/>
  </div>,
  document.getElementById('react')
);
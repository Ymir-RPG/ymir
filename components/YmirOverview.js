"use strict";
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('navbar.js');
var TableOfContents = require('tableofcontents.js');

var YmirOverview = React.createClass({

    render: function() {
        return React.createElement('div', {},
            React.createElement(NavBar, {}, "Hello, this is the nav bar!"),
            React.createElement('h1', {className: "text-center"}, "Ymir RPG Campaign Manager"),
            React.createElement(TableOfContents, {}, "Table of Contents")
        );
    }
});

ReactDOM.render(
  React.createElement(YmirOverview, {}, null),
  document.getElementById('react')
);
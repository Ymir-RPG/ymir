"use strict";
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./NavBar');
var TableOfContents = require('./TableOfContents');
var OverviewFeed = require('./OverviewFeed');

var YmirOverview = React.createClass({

    render: function() {

        return (
            <div>
                <NavBar />
                <div className="container"> 
                    <br />
                    <h1 className="text-center">Ymir RPG Campaign Manager</h1>
                    <br />
                    <TableOfContents>
                        <h5 className="text-center">Catagories</h5>
                        <a href="character.html">Character</a>
                        <br/>
                        <a href="places.html">Places</a>
                    </TableOfContents>
                    <OverviewFeed>
                        <h4>Recent changes</h4>
                    </OverviewFeed>
                </div>
            </div>
        );
    }
});

ReactDOM.render(
  React.createElement(YmirOverview, {}, null),
  document.getElementById('react')
);
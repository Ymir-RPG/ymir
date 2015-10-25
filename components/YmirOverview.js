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
                <h1 className="text-center">Ymir RPG Campaign Manager</h1>
                <TableOfContents>
                    <h4 className="text-center">Table of Contents</h4>
                    <a href="character.html">Character</a>
                    <br/>
                    <a href="places.html">Places</a>
                </TableOfContents>
                <OverviewFeed>
                    <h3 className="text-center">I MUST FEED</h3>
                </OverviewFeed>
            </div>
        );
    }
});

ReactDOM.render(
  React.createElement(YmirOverview, {}, null),
  document.getElementById('react')
);
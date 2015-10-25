"use strict";
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./navbar');
var TableOfContents = require('./tableofcontents');
var OverviewFeed = require('./feed');

var YmirOverview = React.createClass({

    render: function() {

        return (
            <div>
                <NavBar />
                <h1 className="text-center">Ymir RPG Campaign Manager</h1>
                <TableOfContents>
                    <h4 className="text-center">Table of Contents</h4>
                    <a href="characters">Characters</a>
                    <br/>
                    <a href="places">Places</a>
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
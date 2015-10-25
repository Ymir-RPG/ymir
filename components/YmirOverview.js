"use strict";

var NavBar = React.createClass({

    render: function() {
        return React.createElement('div', {className: "top-nav"}, this.props.children);
    }
});

var TableOfContents = React.createClass({

    render: function() {
        return React.createElement('div', {className: "three columns table-of-contents"}, this.props.children);
    }
});

var Feed = React.createClass({
    render: function() {
        return "hi!"
    }
});

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
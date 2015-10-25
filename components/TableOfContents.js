var React = require('react');

var TableOfContents = React.createClass({

    render: function() {
        return React.createElement('div', {className: "three columns table-of-contents"}, this.props.children);
    }
});

module.exports = TableOfContents;
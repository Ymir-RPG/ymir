var React = require('react');

var NavBar = React.createClass({

    render: function() {
    	return (
    		<div className = "top-nav">
    			{this.props.children}
    		</div>
    	);
    }
});

module.exports = NavBar;
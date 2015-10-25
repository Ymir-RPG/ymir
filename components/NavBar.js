var React = require('react');

var NavBar = React.createClass({

    render: function() {
    	return (
    		<div className = "top-nav">
    			<span className="nav-text">Ymir RPG</span>
    		</div>
    	);
    }
});

module.exports = NavBar;
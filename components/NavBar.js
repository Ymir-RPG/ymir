var React = require('react');

var NavBar = React.createClass({

    render: function() {
    	return (
    		<div className = "top-nav">
    			<span className="nav-text">Ymir RPG</span>
    			<a href="worldList.html">worlds </a>
    			<a href="character.html"> characters</a>
    		</div>
    	);
    }
});

module.exports = NavBar;
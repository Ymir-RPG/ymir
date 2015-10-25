var React = require('react');

var NavBar = React.createClass({

    render: function() {
    	return (
    		<div className = "top-nav">
    			<span className="nav-text">Ymir RPG</span>
    			<a className="nav-text" href="worldList.html">Worlds</a>
    			<a className="nav-text" href="character.html">Characters</a>
    		</div>
    	);
    }
});

module.exports = NavBar;
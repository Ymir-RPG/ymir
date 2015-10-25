var React = require('react');

var NavBar = React.createClass({

    render: function() {
    	return (
    		<div className = "top-nav">
    			<div className="container">
    				<span className="nav-text">
    					<a href="worldList.html">
    						Ymir RPG
    					</a>
    				</span>
    				<a className="nav-text" href="character.html">Characters</a>
    				<a className="nav-text" href="places.html">Places</a>
    			</div>
    		</div>
    	);
    }
});

module.exports = NavBar;

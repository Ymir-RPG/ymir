var React = require('react');

var NavBar = React.createClass({

    render: function() {
    	return (
    		<div className = "top-nav">
    			<div className="container">
    				<span className="nav-text">
    					<a href="overview.html">
    						Ymir RPG
    					</a>
    				</span>
    				<a className="nav-text" href="worldList.html">Worlds</a>
    				<a className="nav-text" href="character.html">Characters</a>
    			</div>
    		</div>
    	);
    }
});

module.exports = NavBar;
var React = require('react');

var OverviewFeed = React.createClass({
    render: function() {
        return (
        	<div className = "seven columns overview-feed">
        		{this.props.children}
        	</div>
        );
    }
});

module.exports = OverviewFeed;
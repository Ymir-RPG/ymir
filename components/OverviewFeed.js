var React = require('react');
var ymirAPI =require('../static/js/ymirWrapper.js');
var Model = ymirAPI;

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}

var OverviewFeed = React.createClass({

	getInitialState: function(){
	    return {
	    	people: [],
	    	places: []
	    }
	},

	componentDidMount: function(){
	    var self = this;
	    var world = Model(getCookie('worldId'));
	    world['Characters'].all().then(function(res){
	    	console.log(res);
	        var st=self.state;
	        st.people = res.data;
	        self.setState(st);
	    });
	    world['Places'].all().then(function(res){
	    	console.log(res);
	        var st=self.state;
	        st.places = res.data;
	        self.setState(st);
	    });
	},

    render: function() {
        return (
        	<div className = "eight columns overview-feed">
        		<div className = "one-half column">
        			Some garbage here
        		</div>
        		<div className = "one-half column">
        			Some garbage there
        		</div>
        	</div>
        );
    }
});

module.exports = OverviewFeed;
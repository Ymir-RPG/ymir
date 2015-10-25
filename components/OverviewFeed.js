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
	    world['Characters'].chrono().then(function(res){
	    	console.log(res);
	        var st=self.state;
	        st.people = res.data;
	        self.setState(st);
	    });
	    world['Places'].chrono().then(function(res){
	    	console.log(res);
	        var st=self.state;
	        st.places = res.data;
	        self.setState(st);
	    });
	},

    render: function() {
    	var mappedPeople = this.state.people.map((i,n)=>{
			return(
				<li key={n}>
					<a className="name">{i.name}</a>
				</li>
			);
		});
    	var mappedPlaces = this.state.places.map((i,n)=>{
			return(
				<li key={n}>
					<a className="place">{i.name}</a>
				</li>
			);
		});

        return (
        	<div className = "eight columns overview-feed">
        		{this.props.children}
        		<div className = "one-half column">
        			{mappedPeople}
        		</div>
        		<div className = "one-half column">
        			{mappedPlaces}
        		</div>
        	</div>
        );
    }
});

module.exports = OverviewFeed;
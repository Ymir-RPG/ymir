// search.js
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./NavBar');
var ymirAPI =require('../static/js/ymirWrapper.js');
var Model = ymirAPI(1);


var WorldList = React.createClass({
	getInitialState: function(){
	    return {worlds:[]}
	},

	componentDidMount: function(){
	    var self = this;
	    Model.Worlds.all().then(function(res){
	        var st=self.state;
	        st.worlds = res.data;
	        self.setState(st);
	    })
	},

	render: function(){
		var foo = this.state.worlds.map(function(i){
			return(
				<li> {i.id}: {i.name}</li>
			);
		});
	    return(
	    	<div>
				<NavBar />	    		
				<h1>WorldList </h1>
				<ul>
					{foo}
				</ul>
	    	</div>
	    )
	}
})

ReactDOM.render(
  <WorldList/>,
  document.getElementById('react')
);
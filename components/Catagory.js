// search.js
var React = require('react');
var ReactDOM = require('react-dom');
var ymirAPI =require('../static/js/ymirWrapper.js');
var Model = ymirAPI('1');

var Catagory = React.createClass({
	getInitialState: function(){
	    return {worlds:[]}
	},

	componentDidMount: function(){
	    var self = this;
	    Model['Characters'].all().then(function(res){
	    	console.log(res);
	        var st=self.state;
	        st.worlds = res.data;
	        self.setState(st);
	    })
	},

	render: function(){
		var foo = this.state.worlds.map((i,n)=>{
			return(
				<li key={n}> <a>{i.id}: {i.name}</a></li>
			);
		});
	    return(
	    	<div>
				<h1>{this.props.catagory} </h1>
				{foo}
	    	</div>
	    )
	}
})

module.exports = Catagory;


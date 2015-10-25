// search.js
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./NavBar');
var ymirAPI =require('../static/js/ymirWrapper.js');
var Model = ymirAPI(1);


var Search = React.createClass({
	getInitialState: function(){
	    return {worlds:[]}
	},

	componentDidMount: function(){
	    var self = this;
	    Model.Worlds.all().then(function(res){
	        console.log(res.data)
	        var st=self.state;
	        st.worlds = res.data;
	        self.setState(st);
	    })
	},

	render: function(){
	    return(
	    	<div> search! </div>
	    )
	}
})

ReactDOM.render(
  <Search/>,
  document.getElementById('react')
);
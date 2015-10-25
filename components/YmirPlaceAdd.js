// search.js
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./NavBar');
var ymirAPI =require('../static/js/ymirWrapper.js');
var Model = ymirAPI(getCookie('worldId'));

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

var PlaceAdd = React.createClass({
	getInitialState: function(){
	    return {worlds:[], places:{}}
	},
	componentDidMount: function(){
	    var self = this;
	    Model.Worlds.all().then(function(res){
	    	console.log(res.data);
	        var st=self.state;
	        st.worlds = res.data;
	        self.setState(st);
	    }).catch(function(res){
	    	console.log(res)
	    });
	    if(this.props.id){
	    	Model.Places.findOne(this.props.id).then(function(res){
	    		console.log(res);
	    	})
	    }
	   
	},
	save: function(){
		var name = document.getElementById('name').value;
		Model.Places.create({name:name})
		location.reload()
	},
	render:function(){
		var options = this.state.worlds.map((i,n)=>{
			return(
				<option key={i.id} value={i.id}>{i.name}</option>
			);
		});
		return(
			<div>
				<textfield>name</textfield>
				<input id="name"/> <br />
				<button onClick={this.save}>SAVE</button>	
				<button >CANCEL</button>	
			</div>
		)
	}
})	

ReactDOM.render(
  <div>
  	<NavBar />
  	<PlaceAdd />
  </div>,
  document.getElementById('react')
);
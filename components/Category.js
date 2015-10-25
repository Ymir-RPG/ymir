// search.js
var React = require('react');
var ReactDOM = require('react-dom');
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

var Category = React.createClass({
	getInitialState: function(){
	    return {worlds:[]}
	},

	componentDidMount: function(){
	    var self = this;
	    Model(getCookie('worldId'))['Characters'].all().then(function(res){
	    	console.log(res);
	        var st=self.state;
	        st.worlds = res.data;
	        self.setState(st);
	    });
	},

	render: function(){
		var items = this.state.worlds.map((i,n)=>{
			return(
				<li key={n}>
					<a className="name">{i.id}: {i.name}</a>
					<a href={"CharactersEdit.html?id="+i.id} > | edit </a>
					<a>| delete </a>
				</li>
			);
		});
	    return(
	    	<div id="CAT">
				<h1>{this.props.category} <a href={this.props.category + "Add.html"}>+</a> </h1>
				<input className="search" placeholder="Search" />
				<ul className="list">
					{items}
				</ul>
	    	</div>
	    )
	}
})

module.exports = Category;


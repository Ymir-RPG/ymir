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
	    var context = this.props.category;
	    Model(getCookie('worldId'))[context].all().then(function(res){
	    	console.log(res);
	        var st=self.state;
	        st.worlds = res.data;
	        self.setState(st);
	    });
	},

	rm: function(id){
	    var context = this.props.category;
		Model(getCookie('worldId'))[context].del(id).then(function(res){
			console.log(res);
		});
		location.reload()
	},

	cookieFunction: function(id) {
		document.cookie = "characterEditId="+id;
		location.href=this.props.category+"Edit.html"
	},

	render: function(){
		var self = this;
		var items = this.state.worlds.map((i,n)=>{
			return(
				<li key={n}>
					<a className="name">{i.name}</a>
					<a className="button sm-button" onClick={function(){self.cookieFunction(i.id)}}>edit</a>
					<a className="button sm-button" onClick={self.rm(.bind(this,)i.id)}>delete</a>
				</li>
			);
		});
	    return(
	    	<div id="CAT">
				<div className="header">
					<div className="container">
						<h1>{this.props.category} <a href={this.props.category + "Add.html"}>+</a> </h1>
						<input type="text" className="search" placeholder="Search" />
					</div>
				</div>
				<div className="container">
					
					<ul className="list">
						{items}
					</ul>
				</div>
				
	    	</div>
	    )
	},


})

module.exports = Category;


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
		console.log('asdfsad');
	    var self = this;
	    Model.Worlds.all().then(function(res){
	    	console.log(res.data);
	        var st=self.state;
	        st.worlds = res.data;
	        self.setState(st);
	    }).catch(function(res){
	    	console.log(res)
	    })
	},

	changeWorld : function(id){
		console.log(id);
		document.cookie="worldId="+id;
		console.log(document.cookie);
		location.href="character.html";
	},

	create: function(){
		Model.Worlds.create({name:document.getElementById('worldName').value}).then(function(res){
			console.log(res);
		});
		location.reload();
	},

	render: function(){
		var foo = this.state.worlds.map((i,n)=>{
			return(
				<li key={n}> <a onClick={this.changeWorld.bind(this, i.id)}>{i.name}</a></li>
			);
		});
	    return(
	    	<div>
				<NavBar />
				<div className="sm-container">	
					<br />
					<br />
					<br />	
					<h1 className="center">Choose Your World</h1>
					<ul>
						{foo}
					</ul>
					<input type="text" name="name" id="worldName" style={{width: "100%"}}/> <br />
					<button onClick={this.create} className="text-center" style={{width: "100%"}}>New World</button>
				</div>
	    	</div>
	    )
	}
})

ReactDOM.render(
  <WorldList/>,
  document.getElementById('react')
);

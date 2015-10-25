"use strict";

var URL = "http://127.0.0.1:2841";

if (typeof(module) !== 'undefined') {
    var axios = require('axios');
}

var urlify = function(arr){
	return URL + arr.map(function(el){return "/"+el}).join("");
}

var resource = function(resource){
	return {
		all: function(){
			return axios.get(urlify(resource))
		},
		chrono: function(){
			return axios.get(urlify(resource), {
				params:{
					chrologilical:true
				}
			})
		},
		findOne: function(id){
			resource.push(id)
			return axios.get(urlify(resource))
		},
		create: function(data){
			return axios.post(urlify(resource), data)
		},
		update: function(data){
			return axios.put(urlify(resource), data)
		},
		del: function(data){
			resource.push(data)
			return axios.delete(urlify(resource))
		}
	};
}

var ymirAPI = function(world){
	var model = {
		world: world
	};

	model.getWorld = function(){
		return model.world;
	}

	model.Worlds = function(){
		return axios.get(urlify(['worlds']))
	}

	model.Worlds     = resource(['worlds']);
	model.Characters = resource(['worlds', model.world , 'characters']);
	model.Places     = resource(['worlds', model.world , 'places']);

	return model;
}

if (typeof(module) !== 'undefined') {
	module.exports = ymirAPI;
}


// example
var Model = ymirAPI(1);

// var query = Model.Worlds.create({name:'Thedas'});
// // var query = Model.Characters.create({name:'Joe'});
// // // var query = Model.Worlds.del(9);
// // // var query = Model.Worlds.all();


// query.then(function(res){
// 	console.log(res);
// }).catch(function(response){
// 	console.log(response.data);
// });

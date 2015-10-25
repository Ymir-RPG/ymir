"use strict";

if (typeof(module) !== 'undefined') {
    var axios = require('axios');
}

var urlify = function(arr){
	return arr.map(function(el){return "/"+el}).join("");
}

var resource = function(resource){
	return {
		all: function(){
			return axios.get(urlify([resource]))
		},
		findOne: function(id){
			return axios.get(urlify([resource]), {params: {
     			 ID: id
    		}})
		}
	};
}

var ymirAPI = function(world){
	var model = {
		world: world
	};

	model.world = function(){
		return model.world;
	}

	model.Worlds = function(){
		return axios.get('/worlds')
	}

	model.Characters = resource('characters');
	model.Places     = resource('places');

	return model;
}

var Model = ymirAPI('middel_earth');
Model.Worlds().then(function(res){
	console.log(res);
});


axios.get('http://ymirrpg.com/worlds').then(function(res){
	console.log(res);
})

// Model.Characters.all().then(function(res){
// 	console.log(res);
// });
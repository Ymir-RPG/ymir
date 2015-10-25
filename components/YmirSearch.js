"use strict";

var Model = ymirAPI(1);

var NavBar = React.createClass({

    render: function() {
        return React.createElement('div', {className: "top-nav"}, this.props.children);
    }
});

var TableOfContents = React.createClass({

    render: function() {
        return React.createElement('div', {className: "three columns table-of-contents"}, this.props.children);
    }
});

var Feed = React.createClass({
    render: function() {
        return "hi!"
    }
});

var YmirSearch = React.createClass({
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
        var 
        return React.createElement('div', {}, "search")
    }
});

var YmirSearchPage = React.createClass({

    render: function() {
        return React.createElement('div', {},
            React.createElement(NavBar, {}, "Hello, this is the nav bar!"),
            React.createElement('h1', {className: "text-center"}, "Search"),
            React.createElement(YmirSearch, {}, "Hello, this is the nav bar!")
        );
    }
});

ReactDOM.render(
  React.createElement(YmirSearchPage, {}, null),
  document.getElementById('react')
);
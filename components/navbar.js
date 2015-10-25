var NavBar = React.createClass({

    render: function() {
        return React.createElement('div', {className: "top-nav"}, this.props.children);
    }
});
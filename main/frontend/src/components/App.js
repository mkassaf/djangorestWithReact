import React, {Component} from 'react';
import ReactDom from 'react-dom';


class App extends Component {
    render(){
        return <h1>Assaf 33 react App </h1>
    }
}

ReactDom.render(<App />, document.getElementById('app'));
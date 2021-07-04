import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import 'chinese-layout'
import 'chinese-gradient'
import SearchBox from './SearchBox'

class App extends Component {
    constructor(props){
        super(props);
        this.state = {}
    }
    render() {
        return (
            <div className="container">
                <SearchBox />
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'))
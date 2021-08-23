import React, { Component } from 'react'

export class Header extends Component {
    render() {
        return (
            <nav className="nav">
                <a className="nav-link active" aria-current="page" href="#">Active</a>
                <a className="nav-link" href="#">Link</a>
                <a className="nav-link" href="#">Link</a>
                <a className="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
            </nav>
        )
    }
}

export default Header

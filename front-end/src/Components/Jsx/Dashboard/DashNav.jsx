import React, { Component } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars, faSignOutAlt } from '@fortawesome/free-solid-svg-icons'
import '../../Css/Dashboard.css'


class DashNav extends Component {
    constructor(){
        super();
        this.handleLogout=this.handleLogout.bind(this)
    }

    async handleLogout(event){
        event.preventDefault();
    
        this.props.history.push("/Login")
        
        }
    
    render() {
        return (
            <div id="dashnav">
              <button id="logout" onClick={ this.handleLogout} ><FontAwesomeIcon icon={faSignOutAlt} />  </button>    
            </div>
            
        )
    }
}

export default DashNav

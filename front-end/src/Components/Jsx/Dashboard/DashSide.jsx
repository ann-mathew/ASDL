import React, { Component } from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link} from 'react-router-dom';
import { SidebarData } from './SidebarData'
import '../../Css/Sidebar.css'

class DashSide extends Component {
    render() {
        return (
            <div id="sidebar">
                 <ul className='sidebar-items'>
                {SidebarData.map((item, index) => {
                return (
                    <li key={index} className={item.cName}>
                    <FontAwesomeIcon className="sidebar-icon" icon={ item.icon } />
                    <Link to={item.path}>
                        <p>{item.title}</p>
                    </Link>
                    </li>
              );
            })}




             </ul>

                
            </div>
        )
    }
}

export default DashSide

import React, { Component } from 'react'
import LandingPage from './Pages/LandingPage'
import Booking from './Pages/Booking'
import Account from './Pages/Account'
import DashNav from './DashNav'
import DashSide from './DashSide'
import { Switch, Route } from 'react-router-dom';


class Dashboard extends Component {
    render() {
        return (
            <div>
                <DashNav history={this.props.history}/>
                <DashSide/>
                <Switch>
                                {/* different pages */}
                   <Route  path="/Dashboard/Booking"> <Booking/> </Route> 
                   <Route  path="/Dashboard/Account"> <Account/> </Route>
                   <Route  path="/Dashboard"> <LandingPage/> </Route>

                </Switch>            
            </div>
        )
    }
}

export default Dashboard

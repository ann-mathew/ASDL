import React, { Component } from 'react'
import './App.css'
import Login from './Components/Jsx/Login'
import Register from './Components/Jsx/Register'
import Dashboard from './Components/Jsx/Dashboard/Dashboard'
import Booking from './Components/Jsx/Dashboard/Pages/Booking'
import { BrowserRouter, Switch, Route } from 'react-router-dom';


export class App extends Component {
  
  render() {
    return (
      <BrowserRouter>
          <Switch>
                <Route exact path="/Login" component={Login} />
                <Route path="/Dashboard" component={ Dashboard } />  
                <Route exact path="/Register" component={Register} /> 
                <Route exact path="/Booking" component={Booking} />
                      
              
          </Switch>  
      </BrowserRouter>        
      
    )
  }
}

export default App

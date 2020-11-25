import React, { Component } from 'react'
import './App.css'
import Login from './Components/Jsx/Login'
import Register from './Components/Jsx/Register'
import Dashboard from './Components/Jsx/Dashboard/Dashboard'
import { BrowserRouter, Switch, Route } from 'react-router-dom';


export class App extends Component {
  
  render() {
    return (
      <BrowserRouter>
          <Switch>
                <Route exact path="/Login" component={Login} />
                <Route path="/Dashboard" component={ Dashboard } />  
                <Route exact path="/Register" component={Register} />                
              
          </Switch>  
      </BrowserRouter>        
      
    )
  }
}

export default App

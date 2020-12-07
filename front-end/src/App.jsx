import React, { Component } from 'react'
import './App.css'
import Login from './Components/Jsx/Login'
import Register from './Components/Jsx/Register'
import Dashboard from './Components/Jsx/Dashboard/Dashboard'
import Payment from './Components/Jsx/Dashboard/Pages/Payment'
import Receipt from './Components/Jsx/Dashboard/Pages/Receipt'
import { BrowserRouter, Switch, Route } from 'react-router-dom';


export class App extends Component {
  
  render() {
    return (
      <BrowserRouter >
          <Switch>
                <Route exact path="/Login" component={Login} />
                <Route path="/Dashboard" component={ Dashboard } />  
                <Route exact path="/Register" component={Register} /> 
                <Route exact path="/Payment" component={Payment} />
                <Route exact path="/Receipt" component={Receipt} />
                
                
                      
              
          </Switch>  
      </BrowserRouter>        
      
    )
  }
}

export default App

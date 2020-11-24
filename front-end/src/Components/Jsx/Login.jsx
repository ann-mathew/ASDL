import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import "../Css/Login.css"



export class Login extends Component {
    constructor(){
        super()
        this.state={
          email: "",
          password: ""
        }
        this.handleChange=this.handleChange.bind(this)
        this.handleSubmit=this.handleSubmit.bind(this)
      }

    handleChange(event){
        this.setState({
            [ event.target.name ] : event.target.value
          })
      }

    async handleSubmit(event){
       event.preventDefault();
       console.log(this.state);
       fetch(URL,{
           method: 'POST',
           headers : {'Content-type': 'application/json'},
           body: JSON.stringify(this.state)
       })       
       .then( data =>{ console.log(data) })
        .catch( error => console.error(error))

        // this.props.history.push('/Dashboard');  
    }
    render() {
        return (
            <div id="logincard" className="card">
                <div className="card-body">
                    <h2 className="text-center">Login </h2><br/>
                    
                    <form autoComplete="off">
                        
                        <div className="form-group">
                            <input id="email" className="form-control" type="text" value={this.state.email} name="email" placeholder="Enter Email" onChange={this.handleChange}/>
                        </div>
                        
                        <div className="form-group">
                            <input id="password" className="form-control" type="password" value={this.state.password} name="password" placeholder="Enter Password" onChange={this.handleChange}/><br/>
                        </div>
                        
                        <button  type="submit" id="button" className="btn btn-primary deep-purple btn-block" onClick={this.handleSubmit}>Submit</button><br/>
                        <p style={{textAlign: "center"}}>Don't have an account? <Link to="/Register">Register</Link> </p>
            
                    </form>
                </div>
            </div>
        )
    }
}

export default Login

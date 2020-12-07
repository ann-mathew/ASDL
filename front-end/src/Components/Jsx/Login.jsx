import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser , faLock} from "@fortawesome/free-solid-svg-icons";
import "../Css/Login.css"

class Login extends Component {
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
        var form={
            email: this.state.email,
            password: this.state.password
        }

       event.preventDefault();
       fetch("http://127.0.0.1:8000/user/login/",{
           method: 'POST',
           headers : {'Content-type': 'application/json'},
           body: JSON.stringify(form)
       })       
       .then( data =>{ 
        
        this.props.history.push('/Dashboard');  
        console.log(data) }
       
       )
        .catch( error => console.error(error))

    }
    
    render(){
        return (
                <div className="login">
                    <div className="login-box">
                        <h2>Login</h2>
                        <form autoComplete="off">

                        <div className="login-textbox">
                            <FontAwesomeIcon icon={faUser} />
                            <input className="l-email" name="email" type="text" value={this.state.email} onChange={this.handleChange}  placeholder="Email" required/>
                        </div>
                        
                        <div className="login-textbox">
                            <FontAwesomeIcon icon={faLock} />
                            <input className="l-password" name="password" type="password" value={this.state.password} onChange={this.handleChange}  placeholder="Password" required/>
                        </div>
                            
                        <input className="login-submit" type="submit" onClick={this.handleSubmit} value="Login"/><br/>
                        </form>
                        <p style={{textAlign: "center"}}>Don't have an account? <Link  style={{color:"white"}} to="/Register">Register</Link> </p>


                    </div>
                </div>

        )
    }
}

export default Login

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
       event.preventDefault();
       console.log(this.state);
       fetch(URL,{
           method: 'POST',
           headers : {'Content-type': 'application/json'},
           body: JSON.stringify(this.state)
       })       
       .then( data =>{ console.log(data) })
        .catch( error => console.error(error))

        this.props.history.push('/Dashboard');  
    }
    
    render(){
        return (
                <div className="login">
                    <div className="login-box">
                        <h2>Login</h2>
                        <form autoComplete="off">

                        <div className="textbox">
                            <FontAwesomeIcon icon={faUser} />
                            <input className="email" name="email" type="text" value={this.state.email} onChange={this.handleChange}  placeholder="Email" required/>
                        </div>
                        
                        <div className="textbox">
                            <FontAwesomeIcon icon={faLock} />
                            <input className="password" name="password" type="password" value={this.state.password} onChange={this.handleChange}  placeholder="Password" required/>
                        </div>
                            
                        <input className="submit" type="submit" onClick={this.handleSubmit} value="Login"/><br/>
                        </form>
                        <p style={{textAlign: "center"}}>Don't have an account? <Link  style={{color:"white"}} to="/Register">Register</Link> </p>


                    </div>
                </div>

        )
    }
}

export default Login

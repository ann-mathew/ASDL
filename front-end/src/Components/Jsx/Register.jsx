import React, { Component } from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser , faLock ,faPhoneAlt , faEnvelope, faCalendarAlt } from "@fortawesome/free-solid-svg-icons";
import '../Css/Register.css'

export class Register extends Component {
    constructor(){
        super()
        this.state={
          name:"",
          email:"",
          phone:"",
          password: "",
          dob: ""
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
          
        this.props.history.push('/Dashboard');  
    }
   
      
    render() {
        return (

            <div className="register">
                    <div className="register-box">
                        <h2>Create Account</h2>
                        <form autoComplete="off">

                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faUser} />
                            <input className="name" name="name" type="text" value={this.state.name} onChange={this.handleChange}  placeholder="Enter Full Name" required/>
                        </div>


                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faCalendarAlt} />
                            <input className="dob" name="dob" type="date" value={this.state.dob} onChange={this.handleChange}  placeholder="Date of Birth" required/>
                        </div>
                        
                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faEnvelope} />
                            <input className="email" name="email" type="email" value={this.state.email} onChange={this.handleChange}  placeholder="Enter Email" required/>
                        </div>

                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faPhoneAlt} />
                            <input className="phone" name="phone" type="text" value={this.state.phone} onChange={this.handleChange}  placeholder="Enter Phone Number" required/>
                        </div>

                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faLock} />
                            <input className="password" name="password" type="password" value={this.state.password} onChange={this.handleChange}  placeholder="Enter Password" required/>
                        </div>

                            
                        <input className="register-submit" type="submit" onClick={this.handleSubmit} value="Register"/><br/>
                        </form>
                        


                    </div>
                </div>
            
        )
    }
}

export default Register ;

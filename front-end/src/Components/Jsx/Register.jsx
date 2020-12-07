import React, { Component } from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser , faLock ,faPhoneAlt , faEnvelope, faCalendarAlt } from "@fortawesome/free-solid-svg-icons";
import '../Css/Register.css'

export class Register extends Component {
    constructor(){
        super()
        this.state={
          Rname:"",
          username:"",
          email:"",
          phone:"",
          password: "",
          age: ""
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
            full_name: this.state.Rname,
            username: this.state.username,
            password:this.state.password,
            email:this.state.email,
            phoneNo:this.state.phone,
            age:this.state.age,

        }
       event.preventDefault();
       console.log(this.state);
       fetch("http://127.0.0.1:8000/user/register/",{
           method: 'POST',
           headers : {'Content-type': 'application/json'},
           body: JSON.stringify(form)
       })       
       .then( data =>{
        this.props.history.push('/Login');     
        console.log(data) })
        .catch( error => console.error(error))

    }
   
      
    render() {
        return (

            <div className="register">
                    <div className="register-box">
                        <h2>Create Account</h2>
                        <form autoComplete="off">

                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faUser} />
                            <input className="Rname" name="Rname" type="text" value={this.state.Rname} onChange={this.handleChange}  placeholder="Enter Full Name" required/>
                        </div>

                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faUser} />
                            <input className="username" name="username" type="text" value={this.state.username} onChange={this.handleChange}  placeholder="Enter Username" required/>
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
                            <FontAwesomeIcon icon={faCalendarAlt} />
                            <input className="age" name="age" type="int" value={this.state.age} onChange={this.handleChange}  placeholder="Enter Age" required/>
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

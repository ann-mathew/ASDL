import React, { Component } from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser , faLock ,faPhoneAlt , faEnvelope, faCalendarAlt } from "@fortawesome/free-solid-svg-icons";
import '../Css/Register.css'

const validEmailRegex = RegExp(/^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i);
const validPasswordRegex = RegExp(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/i);
const validPhoneNoRegex =RegExp(/^((\+\d{1,2}|1)[\s.-]?)?\(?[2-9](?!11)\d{2}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/i);

export class Register extends Component {
    constructor(){
        super()
        this.state={
          Rname:"",
          username:"",
          email:"",
          phone:"",
          password: "",
          age: "",
          available:"",
          errors:{
              email:"",
              password:"",
              phone:""
          }
        }
        this.handleChange=this.handleChange.bind(this)
        this.handleSubmit=this.handleSubmit.bind(this)
      }

    handleChange(event){
        event.preventDefault();
        const { name, value } = event.target;
        let errors = this.state.errors;

        switch (name) {
        case 'email': 
            errors.email = 
            validEmailRegex.test(value)
                ? ''
                : 'Email is not valid.';
            break;
        case 'password': 
            errors.password = 
            validPasswordRegex.test(value)
                ? ''
                : 'Password must contain atleast one uppercase letter, lowercase letter, number and special character. Min length 8 characters.';
            break;
        case 'phone': 
            errors.phone = 
            validPhoneNoRegex.test(value)
                ? ''
                : 'Phone No. not valid.';
            break;
        
        default:
            break;
        }

        this.setState({errors, [name]: value});

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
       fetch("http://127.0.0.1:8000/user/register/",{
           method: 'POST',
           headers : {'Content-type': 'application/json'},
           body: JSON.stringify(form)
       })       
       .then( data =>{ 
        if (data.status=="400")
        {   console.log("Hello")
            this.setState({
                available: "Email already exists."
            })
        }

        else{
         this.props.history.push('/Login');  
         console.log(data) }

        }

    )
     .catch( error => console.error(error))

 }
      
    render() {

        return (

            <div className="register">
                    <div className="register-box">
                        <h2>Create Account</h2>
                        <form autoComplete="off" onSubmit={this.handleSubmit}>

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
                            <input className="email" name="email" type="text" value={this.state.email} onChange={this.handleChange}  placeholder="Enter Email" required/>
                            { this.state.errors.email > 0 &&  
                             <p className='error'>{ this.state.errors.email}</p>}
                        </div>

                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faPhoneAlt} />
                            <input className="phone" name="phone" type="text" value={this.state.phone} onChange={this.handleChange}  placeholder="Enter Phone Number" required/>
                            { this.state.errors.phone > 0 &&  
                             <p className='error'>{ this.state.errors.phone}</p>}
                        </div>
                        
                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faCalendarAlt} />
                            <input className="age" name="age" type="int" value={this.state.age} onChange={this.handleChange}  placeholder="Enter Age" required/>
                        </div>

                        <div className="register-textbox">
                            <FontAwesomeIcon icon={faLock} />
                            <input className="password" name="password" type="password" value={this.state.password} onChange={this.handleChange}  placeholder="Enter Password" required/>
                            { this.state.errors.password > 0 &&  
                             <p className='error'>{ this.state.errors.password}</p>}
                        </div>

                            
                        <input className="register-submit" type="submit"  value="Register"/><br/>
                        
                        { this.state.available > 0 &&  
                             <p className='error'>{this.state.available}</p>}

                        </form>
                        


                    </div>
                </div>
            
        )
    }
}

export default Register ;

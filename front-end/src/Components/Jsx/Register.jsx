import React, { Component } from 'react'
import '../Css/Register.css'

export class Register extends Component {
    constructor(){
        super()
        this.state={
          name:"",
          email:"",
          phone:"",
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
          
        // this.props.history.push('/Dashboard');  
    }
   
      
    render() {
        return (
                <div id="registercard" className="card">
                    <div className="card-body">
                        <h2 className="text-center">Create Account</h2><br/>
                        
                        <form autocomplete="off">
                            
                            <div className="form-group">
                                <input id="name" className="form-control" type="text" value={this.state.name} name="name" placeholder="Enter Full Name" onChange={this.handleChange}/>
                            </div>

                            <div className="form-group">
                                <input id="email" className="form-control" type="text" value={this.state.email} name="email" placeholder="Enter Email" onChange={this.handleChange}/>
                            </div>

                            <div className="form-group">
                                <input id="phone" className="form-control" type="text" value={this.state.phone} name="phone" placeholder="Enter Phone Number" onChange={this.handleChange}/>
                            </div>
                            
                            <div className="form-group">
                                <input id="password" className="form-control" type="password" value={this.state.password} name="password" placeholder="Enter Password" onChange={this.handleChange}/><br/>
                            </div>
                            
                            <button  type="submit" id="button" className="btn btn-primary deep-purple btn-block" onClick={this.handleSubmit}>Submit</button><br/>
                
                        </form>
                    </div>
                </div>
        )
    }
}

export default Register ;

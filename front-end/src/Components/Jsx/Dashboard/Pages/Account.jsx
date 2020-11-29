import React, { Component } from 'react'
import '../../../Css/Account.css'

class Account extends Component {
    constructor(){
        super();
        this.state={
            name:"Aiswarya Jayachandran",
            DOB: "24-05-20",
            email :"aiswarya@gmail.com",
            phone : "2123445444"
        }
        
        this.handleChange = this.handleChange.bind(this)

    }

    handleChange(e){
        this.setState({
            [ e.target.name ] : e.target.value})
    }

    // updateProfile(){ 
    //     var self = this;
    //     axios.post('/updateProfile', {
    //       name: this.state.name,
    //       password: this.state.password
    //     })
    //     .then(function (response) {
    //       if(response){
    //         hashHistory.push('/')  
    //       }
    //     })
    //     .catch(function (error) {
    //       console.log('error is ',error);
    //     });
    //   }
     
    render() {
        return (
            <div id="main-content" >
                <div className=" account col-md-12">
                    <div className="form-area"> 
                        <h3  id="account-title">Account Details</h3>
    
                        <form id="account-form">

                            <div className="form-group">
                            <label for="name">Name:</label>
                            <input id="name" value={this.state.name} name="name" type="text" onChange={this.handleChange} className="form-control" placeholder="Name"  />
                            
                            <label for="DOB">DOB:</label>
                            <input  id="DOB" value={this.state.DOB} name="DOB" type="date" onChange={this.handleChange} className="form-control" placeholder="DOB" />
                            
                            <label for="Email">Email:</label>
                            <input id="Email" value={this.state.email}  name="email" type="text" onChange={this.handleChange} className="form-control" placeholder="Email" />
                            
                            <label for="phone">Phone:</label>
                            <input id="phone" value={this.state.phone} name="phone" type="text" onChange={this.handleChange} className="form-control" placeholder="Phone"  />
                            </div>
                            
                            <button  id="account-button" type="button" onClick={this.updateProfile} id="submit" name="submit" className="btn btn-primary pull-right">Update</button>
                        </form>
                    </div>
                </div>

            </div>
        )
    }
}

export default Account

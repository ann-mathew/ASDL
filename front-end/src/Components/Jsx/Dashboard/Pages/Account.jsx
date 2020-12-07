import React, { Component } from 'react'
import '../../../Css/Account.css'

class Account extends Component {
    constructor(){
        super();
        this.state={
            Aname:"Aiswarya Jayachandran",
            Age: "20",
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
             <h3  id="account-title">Account Details</h3>

                <div className=" account col-md-12">
                    <div className="form-area"> 
    
                        <form id="account-form">

                            <div >
                            <label for="Aname">Name:</label>
                            <input id="Aname" value={this.state.Aname} name="Aname" type="text" onChange={this.handleChange} className="form-control" placeholder="Name"  />
                            
                            <label for="Age">Age:</label>
                            <input  id="Age" value={this.state.Age} name="Age" type="number" onChange={this.handleChange} className="form-control" placeholder="Age" />
                            
                            <label for="email">Email:</label>
                            <input id="email" value={this.state.email}  name="email" type="text" onChange={this.handleChange} className="form-control" placeholder="Email" />
                            
                            <label for="phone">Phone:</label>
                            <input id="phone" value={this.state.phone} name="phone" type="text" onChange={this.handleChange} className="form-control" placeholder="Phone"  />
                            </div>
                            
                            <button  id="account-button" type="button" onClick={this.updateProfile} id="submit" name="submit" className="btn btn-primary  mt-4 pull-right">Update</button>
                        </form>
                    </div>
                </div>

            </div>
        )
    }
}

export default Account

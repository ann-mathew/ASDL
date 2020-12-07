import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrain , faCalendarAlt, faUser} from "@fortawesome/free-solid-svg-icons";
import "../../../Css/Booking.css"


class Booking extends Component {
    
    constructor(){
        super()
        this.state={
            
            boarding : "",
            destination : "",
            classoftravel : "",
            dateoftravel : "",
            passengers : ""

        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
        this.setState({
            [ event.target.name ] : event.target.value
          })
      }

    async handleSubmit(event){
       event.preventDefault();
       console.log(this.state)
       fetch(URL,{
        method: 'POST',
        headers : {'Content-type': 'application/json'},
        body: JSON.stringify(this.state)
    })       
    .then( data =>{ console.log(data) })
     .catch( error => console.error(error))
       

        this.props.history.push('/Dashboard/Train');  
    }
    
    
    
    
    render() {
        return (
            <div  id="main-content" className="booking">
                
                <div className="booking-form">
                    <h3>Book Tickets</h3>
                    
                    <form autoComplete="off">
                        
                        <div className="booking-textbox">
                            <FontAwesomeIcon icon = {faTrain} />
                            <input classname = "boarding" name="boarding" type="text" value={this.state.boarding} onChange={this.handleChange} placeholder="From" required/>
                        </div>

                        <div className="booking-textbox">
                            <FontAwesomeIcon icon = {faTrain} />
                            <input classname = "destination" name="destination" type="text" value={this.state.destination} onChange={this.handleChange} placeholder="To" required/>
                        </div>

                        <div className="booking-textbox">
                            <FontAwesomeIcon icon = {faCalendarAlt} />
                            <input classname = "dateoftravel" name="dateoftravel" type="date" value={this.state.dateoftravel} onChange={this.handleChange} placeholder="Travel Date"  required/>
                        </div>

                        <div  className="booking-textbox">
                            
                                <select classnName="selectclass" defaultValue={this.state.classoftravel} onChange={this.handleChange}>
                                    <option value="" disabled className="text-hide">Select Class</option>
                                    <option value="Sleeper Class">Sleeper Class</option>
                                    <option value="Third AC">Third AC</option>
                                    <option value="Second AC">Second AC</option>
                                    <option value="First AC">First AC</option>
                                    <option value="Second Seating">Second Seating</option>
                                    <option value="AC Chair Car">AC Chair Car</option>
                                    <option value="First Class">First Class</option>
                                </select>
                            
                        </div>

                        <div className="booking-textbox">
                            <FontAwesomeIcon icon = {faUser} />
                            <input classname ="passengers" name="passengers" placeholder="0" type="number" min="1" max="7" value={this.state.passengers} onChange={this.handleChange}  required/>
                            
                        </div>
                        <input className="submit_booking" type="submit" onClick={this.handleSubmit} value="Search"/><br/>
                    </form>


                </div>
            
                
            </div>
        )
    }
}

export default Booking

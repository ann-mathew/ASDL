import React, { Component } from 'react'
import '../../../Css/Train.css'

class Train extends Component {
    constructor(){
        super()
        this.state={
            Trains:[
                {
                    TrainNO: 12,
                    Trainname: "Blore. Express",
                    Dep: "12 Pm",
                    Arrival: "8 Pm",
                    Price: 200,
                    Seats: 400
                },
                {
                    TrainNO: 10,
                    Trainname: "Ekm. Express",
                    Dep: "2 Pm",
                    Arrival: "9 Pm",
                    Price: 400,
                    Seats: 200
                },
                {
                    TrainNO: 420,
                    Trainname: "Manglore. Express",
                    Dep: "1 Pm",
                    Arrival: "8 Pm",
                    Price: 300,
                    Seats: 300
                },
                
            ]
        }
        this.changeRoute=this.changeRoute.bind(this)
    }

    changeRoute(){
        let path = `/Payment`;
        this.props.history.push(path)
    }
    render() {
        return (
            <div id="main-content" >
                <div id="train-deets">
                <h3> Available Trains: </h3>

                    <table className="table table-bordered table-xs-responsive table-hover">
                        <thead className="thead-dark">  
                        <tr>
                            <th>Train No</th>
                            <th>Train Name</th>
                            <th>Time of Dep.</th>
                            <th>Time of Arrival</th>
                            <th>Price</th>
                            <th>Available Seats </th>
                            <th> Booking</th>


                        </tr>
                        </thead>
                        <tbody>
                        {
                             this.state.Trains.map((item) => (
                                <tr key={item.TrainNO}>
                                     <td>{item.TrainNO}</td>
                                    <td>{item.Trainname}</td>
                                    <td>{item.Dep}</td>
                                    <td>{item.Arrival}</td>
                                    <td> ₹ {item.Price}</td>
                                    <td>{item.Seats}</td>
                                    <td><button onClick={this.changeRoute} className="btn btn-primary pull-right">Book</button></td>


                                </tr>
                            ))
                        }
                            
                        </tbody>
                    </table>
                </div>
                </div>
        )
    }
}

    

export default Train

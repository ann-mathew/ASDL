import React, { Component } from 'react'
import '../../../Css/Train.css'


class Train extends Component {
    constructor(props){
        super(props)
        this.state={
            Trains: []
        }
        this.changeRoute=this.changeRoute.bind(this)
    }



    componentDidMount(){
        const state = this.props.location.state.data

        this.setState({
            Trains: state
        })

        console.log(this.state.Trains)
    }

    changeRoute(){
        let path = `/Payment`;
        this.props.history.push(path)
    }
    render() {

        console.log(this.state.Trains)
        return (
            <div id="main-content" >
                <div id="train-deets">
                <h4> Available Trains: </h4>

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

                <div id="train-deets">
                <h4> Reserved Trains: </h4>

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

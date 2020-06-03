import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import MaterialTable from 'material-table'
import axios from 'axios'

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {data: []}
    }

    componentDidMount() {
        this.updateRecords();
    }

    updateRecords() {
        console.log('updated');
        axios.get('records').then(response => {
            console.log(response);
            this.setState({data: response.data});
        });
    }

    addRecord(recordData) {
        console.log('add record');
        console.log(recordData);
        recordData['cost'] = 0;
        recordData['cost'] = 0;
        axios.post('records/', {}).then(response => {
            console.log(response);
        });
    }

    render() {
        return (
            <div className="m-2 mb-5">

                <MaterialTable

                    title={'Irrigation Logger'}

                    columns={[
                        {
                            title: 'Bill no.',
                            field: 'id',
                            type: 'numeric',
                            editable: 'never',
                            initialEditValue: this.state.data.length + 1,
                            headerStyle: {
                                border: '1px solid #dee2e6'
                            },
                            cellStyle: {
                                border: '1px solid #dee2e6'
                            }
                        },
                        {
                            title: 'Date', field: 'date', type: 'date', initialEditValue: new Date(), headerStyle: {
                                border: '1px solid #dee2e6'
                            },
                            cellStyle: {
                                border: '1px solid #dee2e6'
                            }
                        },
                        {
                            title: 'Name',
                            field: 'customer',
                            type: 'numeric',
                            lookup: {1: 'Manan', 2: 'Manan', 3: 'Manan', 4: 'Manan'},
                            headerStyle: {
                                border: '1px solid #dee2e6'
                            },
                            cellStyle: {
                                border: '1px solid #dee2e6'
                            }
                        },
                        {
                            title: 'Start time', field: 'start_time', type: 'time', headerStyle: {
                                border: '1px solid #dee2e6'
                            },
                            cellStyle: {
                                border: '1px solid #dee2e6'
                            }
                        },
                        {
                            title: 'End time', field: 'end_time', type: 'time', headerStyle: {
                                border: '1px solid #dee2e6'
                            },
                            cellStyle: {
                                border: '1px solid #dee2e6'
                            }
                        },
                        {
                            title: 'Hours', field: 'time_difference', type: 'numeric', editable: 'never', headerStyle: {
                                border: '1px solid #dee2e6'
                            },
                            cellStyle: {
                                border: '1px solid #dee2e6'
                            }
                        },
                        {
                            title: 'Cost', field: 'cost', type: 'numeric', editable: 'never', headerStyle: {
                                border: '1px solid #dee2e6'
                            },
                            cellStyle: {
                                border: '1px solid #dee2e6'
                            }
                        }
                    ]}

                    options={{
                        headerStyle: {
                            backgroundColor: '#EEE'
                        }
                    }}

                    data={this.state.data}

                    editable={{
                        onRowAdd: newData =>
                            new Promise((resolve, reject) => {
                                setTimeout(() => {
                                    {
                                        const data = this.state.data;
                                        data.push(newData);
                                        console.log(newData)
                                        this.setState({data}, () => resolve());
                                        this.addRecord(newData);
                                        // this.updateRecords();
                                    }
                                    resolve();
                                }, 500);
                            }),
                        onRowUpdate: (newData, oldData) =>
                            new Promise((resolve, reject) => {
                                setTimeout(() => {
                                    {
                                        const data = this.state.data;
                                        const index = data.indexOf(oldData);
                                        data[index] = newData;
                                        this.setState({data}, () => resolve());
                                        this.updateRecords();
                                    }
                                    resolve();
                                }, 500);
                            }),
                        onRowDelete: oldData =>
                            new Promise((resolve, reject) => {
                                setTimeout(() => {
                                    {
                                        let data = this.state.data;
                                        const index = data.indexOf(oldData);
                                        data.splice(index, 1);
                                        this.setState({data}, () => resolve());
                                        this.updateRecords();
                                    }
                                    resolve();
                                }, 500);
                            })
                    }}
                />
            </div>
        )
    }
}

ReactDOM.render(
    <App/>, document.getElementById('root'));
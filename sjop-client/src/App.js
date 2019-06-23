import React from 'react';
import Container  from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './App.css';
import ReliefInput from './components/ReliefInput';
import Canvas from './components/Canvas';

class App extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            reliefData: `{
                "track": [{"key": 0, "x":3, "y": 3, "len": 3, "type": 1}],
                "signal": [{"key": 1, "x":4, "y": 3, "type": 1, "dir": "l", "signal": "red"},{"key": 2, "x":5, "y": 3, "type": 1, "dir": "r", "signal": "green"},{"key": 3, "x":6, "y": 3, "type": 2, "dir": "l", "signal": "blue"}]
            }`,

        };
        this.handleButton = this.handleButton.bind(this);
    }

    handleButton(data, event) {
        this.setState({reliefData: data});
        event.preventDefault();
    }

    render() {
        return (
            <div id="root">
                <Container fluid="true">
                    <Row id="header_row">
                        <Col>
                            <ReliefInput buttonClicked={this.handleButton} data={this.state.reliefData} />
                        </Col>
                    </Row>
                    <Row>
                        <Col id="canvas_place">
                            <Canvas data={this.state.reliefData} />
                        </Col>
                    </Row>
                    <Row id="footer_row">
                        <Col>
                            Footer text
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}

export default App;

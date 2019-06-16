import React from 'react';
import ReactDOM from 'react-dom'
import Container  from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import {Circle, Layer, Rect, Stage, Konva} from 'react-konva';
import logo from './logo.svg';
import './App.css';

class ReliefInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: 'Prosím, vložte definici reliéfu...',
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    render() {
        return (
            <React.Fragment>
                <form>
                    <fieldset>
                        <div className="form-group">
                            <label className="form-control-sm" htmlFor="reliefTextarea">Reliéf</label>
                            <textarea
                            className="form-control form-control-sm"
                            id="reliefTextarea"
                            rows="5"
                            value={this.state.value}
                            onChange={this.handleChange}
                            />
                        </div>
                    </fieldset>
                    <button
                        onClick={this.props.buttonClicked.bind(this, this.state.value)}
                        className="btn btn-primary btn-sm"
                    >
                        Vykreslit
                    </button>
                </form>
            </React.Fragment>
        );
    }
}

class Canvas extends React.Component {
    state = {
    stageWidth: 1,
    stageHeight: 1
    };

    componentDidMount() {
        this.checkSize();
        window.addEventListener("resize", this.checkSize);
    }

    componentWillUnmount() {
        window.removeEventListener("resize", this.checkSize);
    }

    checkSize = () => {
        const width = this.container.offsetWidth;

        var root = document.getElementById("root")
        var header_row = document.getElementById("header_row")
        var footer_row = document.getElementById("footer_row")
        const height = root.offsetHeight - header_row.offsetHeight - footer_row.offsetHeight;

        this.setState({
            stageWidth: width,
            stageHeight: height
        });
    }

    render() {
        const radius = this.state.stageWidth / 10;
        return (
            <div
                style={{
                    width: "100%",
                    height: "100%",
                    border: "1px solid grey"
                }}
                ref={node => {
                    this.container = node;
                }}
            >
                <Stage width={this.state.stageWidth} height={this.state.stageHeight}>
                    <Layer>
                        <Circle x={radius} y={radius} radius={radius} fill="red" />
                    </Layer>
                </Stage>
            </div>
        );
    }
}

class App extends React.Component{
    state = {
        count: 0
    }

    handleButton(data, event) {
        console.log("Handle Button:", data);
        event.preventDefault();
    }

    render() {
        return (
            <div id="root">
                <Container fluid="true">
                    <Row id="header_row">
                        <Col>
                            <ReliefInput buttonClicked={this.handleButton}/>
                        </Col>
                    </Row>
                    <Row>
                        <Col id="canvas_place">
                            <Canvas />
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

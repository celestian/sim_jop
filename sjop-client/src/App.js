import React from 'react';
import Container  from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import {Layer, Rect, Stage, Line} from 'react-konva';
import './App.css';

class ReliefInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: this.props.data,
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

class Track extends React.Component {
    // zoom 2, w 12, h 18
    render() {
        return (
            <Rect
                x={this.props.x * 12}
                y={this.props.y * 18 + 8}
                width={12}
                height={2}
                fill="gray"
            />
        );
    }
}

class Cursor extends React.Component {
    // zoom 2, w 12, h 18
    render() {
        return (
            <Rect
                x={this.props.x - (this.props.x % 12)}
                y={this.props.y - (this.props.y % 18)}
                width={12}
                height={18}
                fill="rgba(0,0,0,0)"
                stroke="rgba(255,0,0,1)"
                strokeWidth={1}
            />
        );
    }
}

class Signal extends React.Component {
    // zoom 2, w 12, h 18
    render() {
        if (this.props.type === 1) {
            return (
                <Line
                    y={1}
                    points={this.props.dir === "r" ? [this.props.x * 12 - 9, this.props.y * 18 + 4, this.props.x * 12 - 3, this.props.y * 18 + 8, this.props.x * 12 - 9, this.props.y * 18 + 12, this.props.x * 12 - 10, this.props.y * 18 + 12, this.props.x * 12 - 10, this.props.y * 18 + 4] : this.props.dir === "l" ? [this.props.x * 12 - 3, this.props.y * 18 + 4, this.props.x * 12 - 9, this.props.y * 18 + 8, this.props.x * 12 - 3, this.props.y * 18 + 12, this.props.x * 12 - 2, this.props.y * 18 + 12, this.props.x * 12 - 2, this.props.y * 18 + 4] : ""}
                    fill={this.props.signal === "red" ? "red" : this.props.signal === "green" ? "lime" : this.props.signal === "blue" ? "blue" : "gray"}
                    stroke={this.props.signal === "red" ? "red" : this.props.signal === "green" ? "lime" : this.props.signal === "blue" ? "blue" : "gray"}
                    strokeWidth={2}
                    lineCap="square"
                    lineJoin="square"
                    closed="true"
                />
            );
        } else if (this.props.type === 2) {
            return (
                <Line
                    y={1}
                    points={this.props.dir === "r" ? [this.props.x * 12 - 9, this.props.y * 18 + 4, this.props.x * 12 - 3, this.props.y * 18 + 8, this.props.x * 12 - 9, this.props.y * 18 + 12] : this.props.dir === "l" ? [this.props.x * 12 - 3, this.props.y * 18 + 4, this.props.x * 12 - 9, this.props.y * 18 + 8, this.props.x * 12 - 3, this.props.y * 18 + 12] : ""}
                    stroke={this.props.signal === "red" ? "red" : this.props.signal === "green" ? "lime" : this.props.signal === "blue" ? "blue" : "gray"}
                    strokeWidth={2}
                    lineCap="square"
                    lineJoin="square"
                />
            );
        }
    }
}

class Canvas extends React.Component {
    state = {
        stageWidth: 1,
        stageHeight: 1,
        mouseCoords: {x: 0, y: 0}
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

        var root = document.getElementById("root");
        var header_row = document.getElementById("header_row");
        var footer_row = document.getElementById("footer_row");
        const height = root.clientHeight - header_row.clientHeight - footer_row.clientHeight - 5;

        this.setState({
            stageWidth: width,
            stageHeight: height
        });
        console.log(`Resolution: ${width}x${height} pts`);
        console.log(`            ${(width - (width % 12)) / 12}x${(height - (height % 18)) / 18} tiles`);
    }

    getMouseCoords = (e) => {
        console.log(`Cursor relative offset to canvas: x:${e.evt.offsetX} y:${e.evt.offsetY}`);
        this.setState({
            mouseCoords: {
                x: e.evt.offsetX,
                y: e.evt.offsetY
            }
        });
    }

    render() {
        var data = JSON.parse(this.props.data);
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
                <Stage width={this.state.stageWidth} height={this.state.stageHeight} onMouseMove={this.getMouseCoords.bind(this.getMouseCoords)}>
                    <Layer>
                        {data['track'].map(i => (
                            <Track key={i.key} x={i.x} y={i.y}/>
                        ))}
                        {data['signal'].map(i => (
                            <Signal key={i.key} x={i.x} y={i.y} type={i.type} dir={i.dir} signal={i.signal}/>
                        ))}
                        <Cursor x={this.state.mouseCoords.x} y={this.state.mouseCoords.y}/>
                    </Layer>
                </Stage>
            </div>
        );
    }
}

class App extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            reliefData: `{
                "track": [{"key": 0, "x":3, "y": 3},{"key": 1, "x":4, "y": 3},{"key": 2, "x":5, "y": 3}],
                "signal": [{"key": 3, "x":4, "y": 3, "type": 1, "dir": "l", "signal": "red"},{"key": 4, "x":5, "y": 3, "type": 1, "dir": "r", "signal": "green"},{"key": 5, "x":6, "y": 3, "type": 2, "dir": "l", "signal": "blue"}]
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

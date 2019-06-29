import React from 'react';
import {Layer, Stage} from 'react-konva';
import Signal from './Signal';
import Track from './Track';
import Junction from './Junction';
import Cursor from './Cursor';

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
                            <Track key={i.key} x={i.x} y={i.y} type={i.type}/>
                        ))}
                        {data['signal'].map(i => (
                            <Signal key={i.key} x={i.x} y={i.y} type={i.type} dir={i.dir} signal={i.signal}/>
                        ))}
                        {data['junction'].map(i => (
                            <Junction key={i.key} x={i.x} y={i.y} type={i.type} />
                        ))}
                        <Cursor x={this.state.mouseCoords.x} y={this.state.mouseCoords.y}/>
                    </Layer>
                </Stage>
            </div>
        );
    }
}

export default Canvas;

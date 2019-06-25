import React from 'react';
import {Line} from 'react-konva';

class Signal extends React.Component {

    // zoom 2, w 12, h 18
    render() {
        var signal = this.props.signal === "red" ? "red" : this.props.signal === "green" ? "lime" : this.props.signal === "blue" ? "blue" : this.props.signal === "white" ? "white" : "gray";
        if (this.props.type === 1) {
            return (
                <Line
                    y={1}
                    points={this.props.dir === "r" ? [
                        (this.props.x + 1) * 12 - 9, this.props.y * 18 + 1,
                        (this.props.x + 1) * 12 - 2, this.props.y * 18 + 8,
                        (this.props.x + 1) * 12 - 9, this.props.y * 18 + 15,
                        (this.props.x + 1) * 12 - 10, this.props.y * 18 + 15,
                        (this.props.x + 1) * 12 - 10, this.props.y * 18 + 1
                    ] : this.props.dir === "l" ? [
                        (this.props.x + 1) * 12 - 3, this.props.y * 18 + 1,
                        (this.props.x + 1) * 12 - 10, this.props.y * 18 + 8,
                        (this.props.x + 1) * 12 - 3, this.props.y * 18 + 15,
                        (this.props.x + 1) * 12 - 2, this.props.y * 18 + 15,
                        (this.props.x + 1) * 12 - 2, this.props.y * 18 + 1
                    ] : ""}
                    fill={signal}
                    stroke={signal}
                    strokeWidth={2}
                    lineCap="square"
                    lineJoin="square"
                    closed={true}
                />
            );
        } else if (this.props.type === 2) {
            return (
                <Line
                    y={1}
                    points={this.props.dir === "r" ? [
                        (this.props.x + 1) * 12 - 10, this.props.y * 18 + 1,
                        (this.props.x + 1) * 12 - 2, this.props.y * 18 + 8,
                        (this.props.x + 1) * 12 - 10, this.props.y * 18 + 15
                    ] : this.props.dir === "l" ? [
                        (this.props.x + 1) * 12 - 2, this.props.y * 18 + 1,
                        (this.props.x + 1) * 12 - 10, this.props.y * 18 + 8,
                        (this.props.x + 1) * 12 - 2, this.props.y * 18 + 15
                    ] : ""}
                    stroke={signal}
                    strokeWidth={2}
                    lineCap="square"
                    lineJoin="square"
                />
            );
        }
    }
}

export default Signal;
import React from 'react';
import {Line} from 'react-konva';

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
                    closed={true}
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

export default Signal;
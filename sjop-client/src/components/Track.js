import React from 'react';
import {Line, Rect} from 'react-konva';

class Track extends React.Component {
    // zoom 2, w 12, h 18
    render() {
        if (this.props.type === 1) {
            return (
                <Line
                  points={[
                          this.props.x * 12, this.props.y * 18 + 9,
                          this.props.x * 12 + this.props.length * 12, this.props.y * 18 + 9
                      ]}
                  strokeWidth={2}
                  stroke="gray"
                />
            );
        } else if (this.props.type === 2) {
            return (
                <Line
                points={[
                        this.props.x * 12 + 12, this.props.y * 18 + 9,
                        this.props.x * 12 + 6, this.props.y * 18 + 18
                    ]}
                strokeWidth={2}
                stroke="gray"
                />
            );
        } else if (this.props.type === 15) {
            return (
                <Line
                points={[
                        this.props.x * 12, this.props.y * 18 + 9,
                        this.props.x * 12 + 6, this.props.y * 18
                    ]}
                strokeWidth={2}
                stroke="gray"
                />
            );
        } else if (this.props.type === 18) {
            return (
                <React.Fragment>
                    <Line
                        points={[
                                this.props.x * 12, this.props.y * 18 + 9,
                                this.props.x * 12 + 5, this.props.y * 18 + 9,
                            ]}
                        strokeWidth={2}
                        stroke="grey"
                    />
                    <Line
                        points={[
                                this.props.x * 12 + 8, this.props.y * 18 + 9,
                                this.props.x * 12 + 12, this.props.y * 18 + 9,
                            ]}
                        strokeWidth={2}
                        stroke="grey"
                    />
                </React.Fragment>
            );
        } else {
            // this is not possible
            return (
                <Rect
                points={[
                        this.props.x * 12, this.props.y * 18,
                        this.props.x * 12, this.props.y * 18
                    ]}
                x={this.props.x * 12}
                y={this.props.y * 18 + 4.5}
                width={6}
                height={9}
                strokeWidth={2}
                stroke="red"
                fill="yellow"
                />
            );
        }
    }
}

export default Track;

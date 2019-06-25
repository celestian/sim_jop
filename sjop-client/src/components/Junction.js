import React from 'react';
import {Line, Rect} from 'react-konva';

class Junction extends React.Component {
    // zoom 2, w 12, h 18
    render() {
        if (this.props.type === 1) {
            return (
                <React.Fragment>
                    <Line
                      points={[
                              this.props.x * 12, this.props.y * 18 + 9,
                              this.props.x * 12 + 12, this.props.y * 18 + 9
                          ]}
                      strokeWidth={2}
                      stroke="gray"
                    />
                    <Line
                      points={[
                              this.props.x * 12, this.props.y * 18 + 9,
                              this.props.x * 12 + 6, this.props.y * 18 + 18
                          ]}
                      strokeWidth={2}
                      stroke="gray"
                    />
                </React.Fragment>
            );
        } else {
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
                fill="blue"
                />
            );
        }
    }
}
export default Junction;

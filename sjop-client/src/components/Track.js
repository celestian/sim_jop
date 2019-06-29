import React from 'react';
import {Line, Rect} from 'react-konva';

class Track extends React.Component {
    // zoom 2, w 12, h 18
    render() {

        const point_a = this.props.x * 12;
        const point_b = point_a + 6;
        const point_c = point_a + 12;
        const point_d = this.props.y * 18;
        const point_e = point_d + 9;
        const point_f = point_d + 18;

        if (this.props.type === 12) {
            return (
                <Line
                  points={[point_a, point_e, point_c, point_e]}
                  strokeWidth={2}
                  stroke="gray"
                />
            );
        } else if (this.props.type === 14) {
            return (
                <Line
                points={[point_c, point_e, point_b, point_f]}
                strokeWidth={2}
                stroke="gray"
                />
            );
        } else if (this.props.type === 15) {
            return (
                <Line
                points={[point_a, point_e, point_b,point_d]}
                strokeWidth={2}
                stroke="gray"
                />
            );
        } else if (this.props.type === 16) {
            return (
                <Line
                  points={[point_a, point_e, point_b, point_f]}
                  strokeWidth={2}
                  stroke="gray"
                />
            );
        } else if (this.props.type === 17) {
            return (
                <Line
                  points={[point_b,point_d, point_c, point_e]}
                  strokeWidth={2}
                  stroke="gray"
                />
            );
        } else if (this.props.type === 18) {
            return (
                <React.Fragment>
                    <Line
                        points={[point_a, point_e, this.props.x * 12 + 5, point_e]}
                        strokeWidth={2}
                        stroke="gray"
                    />
                    <Line
                        points={[this.props.x * 12 + 8, point_e, point_c, point_e]}
                        strokeWidth={2}
                        stroke="gray"
                    />
                </React.Fragment>
            );
        } else if (this.props.type === 21) {
            return (
                <Line
                  points={[point_a, point_e, point_b,point_d]}
                  strokeWidth={2}
                  stroke="gray"
                />
            );
        } else {
            // this is not possible
            return (
                <Rect
                points={[point_a,point_d,point_a,point_d]}
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

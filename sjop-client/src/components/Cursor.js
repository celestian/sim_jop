import React from 'react';
import {Rect} from 'react-konva';

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

export default Cursor;
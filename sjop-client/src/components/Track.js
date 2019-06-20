import React from 'react';
import {Rect} from 'react-konva';

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

export default Track;
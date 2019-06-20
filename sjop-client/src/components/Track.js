import React from 'react';
import {Line} from 'react-konva';

class Track extends React.Component {
    // zoom 2, w 12, h 18
    render() {
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
    }
}

export default Track;
import React from 'react';

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

export default ReliefInput;
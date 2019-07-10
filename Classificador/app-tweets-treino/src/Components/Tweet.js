import React from 'react';

class Tweet extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <article>
                    <strong>{ this.props.text }</strong>
                </article>
            </div>
        )
    }
}

export default Tweet;
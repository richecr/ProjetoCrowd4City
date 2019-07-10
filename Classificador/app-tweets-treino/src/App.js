import React from 'react';
import Tweet from "./Components/Tweet.js";

import csvToJson from "convert-csv-to-json";
import Papa from "papaparse";
import axios from 'axios';
import fs from 'fs';

class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			tweets: []
		};
	}

	async componentDidMount() {
		const t = await axios('./tweets.json');
		console.log(t);
	}

	render() {
		return (
			<div>
				<Tweet text="OII"></Tweet>
			</div>
		)
	}
}

export default App;
const axios = require('axios');
require('dotenv/config');

const headers = require('../util/headers');

module.exports = {
    async retweetar(req, res) {
        const id = req.params.id;
        const url = `https://api.twitter.com/1.1/statuses/retweet/${id}.json`;
        console.log(url);
        let response = await axios.post(url, {}, { headers });

        let dados = response.data;
        return res.json(dados);
    },
};
const axios = require('axios');
require('dotenv/config');

const headers = require('../util/headers');

module.exports = {
    async retweetar(req, res) {
        const id = req.params.id;
        const url = 'https://api.twitter.com/1.1/statuses/retweet/'+id+'.json'
        const config = {
            headers,
            params: {
                id: id
            }
        }

        let response = await axios.post(url, config);

        let dados = response.data;
        return res.json(dados);
    },
};
const axios = require('axios');
require('dotenv/config');

const headers = require('../util/headers');

module.exports = {
    async search(req, res) {
        const query = req.params.q;
        const count = req.query.count || "";
        const geocode = req.query.geocode || "";
        const max_id = req.query.max || "";

        const config = {
            headers,
            params: {
                q: query,
                count: count,
                geocode: geocode,
                lang: 'pt',
                tweet_mode: "extended",
            }
        };

        if (max_id != "") {
            config.params['max_id'] = max_id;
        }

        let response = await axios.get(`https://api.twitter.com/1.1/search/tweets.json?`, config);
        let dados = response.data;

        return res.json(dados);
    },
};
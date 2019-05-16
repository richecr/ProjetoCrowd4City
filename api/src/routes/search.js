const axios = require('axios');
require('dotenv/config');

module.exports = {
    async search(req, res) {
        const query = req.params.q;
        const count = req.query.count || "";
        const geocode = req.query.geocode || "";
    
        let headers = {
            Authorization: 'Bearer ' + process.env.TOKEN
        }
    
        let response = await axios.get(`https://api.twitter.com/1.1/search/tweets.json?`,
            {
                headers,
                params: {
                   q: query,
                   count: count,
                   geocode: geocode
                }
            });

        let dados = response.data;
        return res.json(dados);
    },
};
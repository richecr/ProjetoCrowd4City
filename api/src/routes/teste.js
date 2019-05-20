const axios = require('axios');
require('dotenv/config');

const headers = require('./headers');

module.exports = {
    async teste(req, res) {
        const id = req.params.id;
    
        let response = await axios.get(`https://api.twitter.com/1.1/statuses/show.json?`,
            {
                headers,
                params: {
                    id: id
                }
            });
    
        let dados = response.data;
        return res.json(dados['text']);
    }
};
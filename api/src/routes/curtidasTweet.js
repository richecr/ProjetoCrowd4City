const axios = require('axios');
require('dotenv/config');

module.exports = {
    async curtidasTweet(req, res) {
        const id = req.params.id;
    
        let headers = {
            Authorization: 'Bearer ' + process.env.TOKEN
        }
    
        let response = await axios.get(`https://api.twitter.com/1.1/statuses/show.json?`,
            {
                headers,
                params: {
                    id: id
                }
            });
    
        let dados = JSON.parse(JSON.stringify(response.data));
        let r = {
            curtidas: dados['favorite_count']
        };
    
        return res.json(r);
    }
}
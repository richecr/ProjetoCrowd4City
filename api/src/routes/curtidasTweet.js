const express = require('express');
const router = express.Router();

router.get('/:id', async (req, res) => {
    const id = req.params.id;

    let headers = {
        Authorization: 'Bearer ' + token
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

    res.json(r);

});

module.exports = router;
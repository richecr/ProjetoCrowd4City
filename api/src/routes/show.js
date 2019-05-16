const express = require('express');
const router = express.Router();

router.get('/:id', async function (req, res) {
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

    let dados = response.data;
    res.json(dados);
});

module.exports = router;
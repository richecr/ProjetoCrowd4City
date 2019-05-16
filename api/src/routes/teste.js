const express = require('express');
const router = express.Router();

router.get("/", async function (req, res) {
    
    let headers = {
        Authorization: 'Bearer ' + token
    }

    let response = await axios.get(`https://twitter.com/search?q=twitterdev`,
        {
            headers
        });

    let dados = response.data;
    res.json(dados);
});

module.exports = router;
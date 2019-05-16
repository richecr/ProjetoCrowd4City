const express = require('express');
const axios = require('axios');

// Inicializando o express.
var app = express();

// Liberando os cors.
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type,Authorization');
    next();
});

// Avisando ao servidor qual a página root.
app.use(express.static('public'));
app.use(express.json());
app.use(require('./src/routes/routes.js'));


/*
// Rota 'search/:q'. q => texto a ser procurado.
app.get("/search/:q", async function (req, res) {
    const query = req.params.q;

    const count = req.query.count || "";
    const geocode = req.query.geocode || "";

    let headers = {
        Authorization: 'Bearer ' + token
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
    res.json(dados);
});

app.get('/show/:id', async function (req, res) {
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

app.get('/tweet/favorites/:id', async (req, res) => {
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

app.get("/teste", async function (req, res) {
    
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
*/

// Liberando a porta 3001 para o servidor.
app.listen(3001, () => console.log("Servidor rodando na porta mágica: 3001"));
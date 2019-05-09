const express = require('express');
const OAuth2 = require('oauth').OAuth2;
const https = require('https');
const axios = require('axios');

var app = express();

// Liberando os cors.
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type,Authorization');
    next();
});

var config = {
    "consumerKey": "rrUDLNZVqv8DaWX6fkmNrB5V9",
    "consumerSecret": "R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7",
    "accessToken": "2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK",
    "accessTokenSecret": "AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW"
}

var token = null;
var oauth2 = new OAuth2(config.consumerKey, config.consumerSecret, 'https://api.twitter.com/', null, 'oauth2/token', null);
oauth2.getOAuthAccessToken('', {
    'grant_type': 'client_credentials'
  }, function (e, access_token) {
        token = access_token;
});


app.use(express.static('public'));


app.get("/", function (req, res) {
    res.send("Oi");
});

app.get("/search/:q", async function (req, res) {
    const query = req.params.q;

    const count = req.query.count || "";

    let headers = {
        Authorization: 'Bearer ' + token
    }

    let response = await axios.get(`https://api.twitter.com/1.1/search/tweets.json?`,
            {
                headers,
                params: {
                   q: query,
                   count: count
                }
            });
    let dados = response.data;
    res.json(dados);
})


app.listen(3001, () => console.log("Servidor rodando na porta mágica: 3001"));
// Importando bibliotecas.
const Twitter = require('twitter')
const express = require('express');

// Iniciando.
const app = express();
const client = new Twitter({
    consumer_key: 'rrUDLNZVqv8DaWX6fkmNrB5V9',
    consumer_secret: 'R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7',
    access_token_key: '2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK',
    access_token_secret: 'AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW'
});

// Liberando os cors.
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type,Authorization');
    next();
});

// Requisição para o "/".
app.get("/", (req, res) => {
    res.send("OI")
});

// Requisição para o "/search".
app.get('/search/:count', (req, res) => {
    const count = req.params.count;
    client.get('/search/tweets', {q: "lixo rua calçada", count: count}, function (error, tweets, response) {
        res.json(tweets);
    });
});

app.get('/')

// Deixando o servidor online
app.listen(3001);
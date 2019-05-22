const express = require('express');
const routes = express.Router();

const { search } = require('../search.js');
const { show } = require('../show.js');
const { curtidasTweet } = require('../curtidasTweet.js');
const { teste } = require('../teste.js')
const { retweetar } = require('../retweetar.js');

routes.get('/', (req, res) => res.send("Olá!"));
routes.get('/search/:q', search);
routes.get('/show/:id', show);
routes.get('/curtidas/:id', curtidasTweet);
routes.post("/retweetar/:id", retweetar)

routes.get('/textoCompleto/:id', teste)

module.exports = routes;
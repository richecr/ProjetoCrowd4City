const express = require('express');
const routes = express.Router();

const { search } = require('../search.js');
const { show } = require('../show.js');
const { curtidasTweet } = require('../curtidasTweet.js');
const { teste } = require('../teste.js')
const { retweetar } = require('../retweetar.js');
const { unretweetar } = require('../unretweetar.js');

routes.get('/', (req, res) => res.send("Olá!"));
routes.get('/search/:q', search);
routes.get('/show/:id', show);
routes.get('/curtidas/:id', curtidasTweet);
routes.post("/retweetar/:id", retweetar);
routes.post("/unretweetar/:id", unretweetar);

routes.get('/textoCompleto/:id', teste)

module.exports = routes;
const express = require('express');
const routes = express.Router();

const { search } = require('./search.js');
const show = require('./show.js');
const curtidasTweet = require('./curtidasTweet.js');
const teste = require('./teste.js')

routes.get('/search/:q', search);

module.exports = routes;
const OAuth2 = require('oauth').OAuth2;

// Configurando a autenticação.
var config = {
    "consumerKey": "rrUDLNZVqv8DaWX6fkmNrB5V9",
    "consumerSecret": "R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7",
    "accessToken": "2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK",
    "accessTokenSecret": "AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW"
}

var token = "";
var oauth2 = new OAuth2(config.consumerKey, config.consumerSecret, 'https://api.twitter.com/', null, 'oauth2/token', null);
oauth2.getOAuthAccessToken('', {
    'grant_type': 'client_credentials'
  }, function (e, access_token) {
        token = access_token;
        console.log(token);
});

console.log(token);
module.exports = { token };
const OAuth2 = require('oauth').OAuth2;

// Configurando a autenticação.
var config = {
    "consumerKey": "og4SjxhGjBENZw8AxAmQNNOyU",
    "consumerSecret": "c5jPRyoNjCyV5CWdmhxPNwGO27jyg3kltrXDHLhq8MuritDvrg",
    "accessToken": "855074511498170368-zN5YGgGbyZwVPeGdonYTzYuTzdVerNQ",
    "accessTokenSecret": "sa7PG7HBZnZvDBeXbQZKAoqCAqI4UoE9d5lFhA5hyZVgz"
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
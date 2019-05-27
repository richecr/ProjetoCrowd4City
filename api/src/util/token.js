const OAuth2 = require('oauth').OAuth2;

// Configurando a autenticação.
var config = {
    "consumerKey": "5seEmVC04JjQXSIQBIxPLrNsk",
    "consumerSecret": "Zl9ZA4RDidTFbgiZZVCLolV1vzmLuWONIKPn14KLWMSTEWStDZ",
    "accessToken": "855074511498170368-phycV4NNzwpOex7ZHg9d4Eo17N642Xd",
    "accessTokenSecret": "rY093cMYhYccUJ8QH6zCu60nZp6tbT7EzNVgbdoPsobXu"
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
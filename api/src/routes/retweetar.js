require('dotenv/config');
const request = require('request');

module.exports = {
    async retweetar(req, res) {
        const id = req.params.id;
        const url = 'https://api.twitter.com/1.1/statuses/retweet/'+id+'.json';

        var oauth = {
            consumer_key: "5seEmVC04JjQXSIQBIxPLrNsk",
            consumer_secret: "Zl9ZA4RDidTFbgiZZVCLolV1vzmLuWONIKPn14KLWMSTEWStDZ",
            token: "855074511498170368-phycV4NNzwpOex7ZHg9d4Eo17N642Xd",
            token_secret: "rY093cMYhYccUJ8QH6zCu60nZp6tbT7EzNVgbdoPsobXu"
        };
        
        request.post({ url: url, oauth: oauth }, function (err, response, request) {
           res.json(JSON.parse(response.body)); 
        });
    },
};
import Fetcher from './Fetcher.js';

window.teste = teste;

function teste() {

    let twitter = new jso.JSO({
        client_id: "api.twitter.com",
        headers: "Access-Control-Allow-Origin",
        authorization: {
            "oauth_consumer_key":"rrUDLNZVqv8DaWX6fkmNrB5V9",
            "oauth_nonce":"IM4c22xHi9moupN3JPPUzNITg4WscMJx47WLkoCN2E",
            "oauth_signature":"Rlz4Ldf6wZiYZvTsLs3ie%252FB3cFI%253D",
            "oauth_signature_method": "HMAC-SHA1",
            "oauth_timestamp": "1557232247",
            "oauth_token": "NSJ9AQAAAAAAzf8-AAABapINkok",
            "oauth_version": "1.0"
        }
    });

    console.log(twitter);
}
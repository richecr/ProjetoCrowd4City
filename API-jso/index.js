import Fetcher from './Fetcher.js';

window.teste = teste;

function teste() {

    let twitter = new jso.JSO({
        client_id: "api.twitter.com",
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

    let a = "oauth_consumer_key=rrUDLNZVqv8DaWX6fkmNrB5V9&oauth_nonce=IM4c22xHi9moupN3JPPUzNITg4WscMJx47WLkoCN2E&oauth_signature=Rlz4Ldf6wZiYZvTsLs3ie%252FB3cFI%253D&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1557232247&oauth_token=NSJ9AQAAAAAAzf8-AAABapINkok&oauth_version=1.0";

    let h = new Headers();
    h.append('Accept', 'application/json');
    h.append("Authorization", a);

    let uri = "https://api.twitter.com/1.1/search/tweets.json?q=RealMadri";

    let req = new Request(uri, {
        method: "GET",
        mode: "no-cors",
        headers: h,
        credentials: "include"
    });

    let d = fetch(req);

}
import exports from "./oauth.js";

var oauth = exports;

async function search() {
    var urlLink = 'https://api.twitter.com/1.1/search/tweets.json?q=RealMadrid';

    var twitterStatus = "Sample tweet";

    var oauth_consumer_key = "rrUDLNZVqv8DaWX6fkmNrB5V9";
    var consumerSecret = "R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7";

    var oauth_token = "2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK";
    var tokenSecret = "AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW";

    var nonce = oauth.nonce(32);
    var ts = Math.floor(new Date().getTime() / 1000);
    var timestamp = ts.toString();

    var accessor = {
        "consumerSecret": consumerSecret,
        "tokenSecret": tokenSecret
    };

    var params = {
        "q": "Real Madrid",
        "status": twitterStatus,
        "oauth_consumer_key": oauth_consumer_key,
        "oauth_nonce": nonce,
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": timestamp,
        "oauth_token": oauth_token,
        "oauth_version": "1.0"
    };
    var message = {
        "method": "GET",
        "action": urlLink,
        "parameters": params
    };

    //lets create signature
    oauth.SignatureMethod.sign(message, accessor);
    var normPar = oauth.SignatureMethod.normalizeParameters(message.parameters);
    var baseString = oauth.SignatureMethod.getBaseString(message);
    var sig = oauth.getParameter(message.parameters, "oauth_signature") + "=";
    var encodedSig = oauth.percentEncode(sig); //finally you got oauth signature

    let response = await axios.get(urlLink, {
        mode: 'no-cors',
        crossDomain: true,
        headers: {
            "Access-Control-Allow-Origin": "http://localhost:5500",
            "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": "AAAAAAAAAAAAAAAAAAAAAD7%2FzQAAAAAAI8%2FRXWmRrDA8H%2F8%2BkKAYl2y%2BhAg%3DVDO00tkNkdsMPOiqCw31w641eV1a2DZwE3O9b0Ll5nvOMdgjas"
            // "Authorization": "OAuth oauth_consumer_key="+oauth_consumer_key+",oauth_signature_method='HMAC-SHA1',oauth_timestamp=" + timestamp + ",oauth_nonce=" + nonce + ",oauth_version=1.0,oauth_token="+oauth_token+",oauth_signature=" + encodedSig
        }
    });

    /*
    $.ajax({
        url: urlLink,
        type: 'GET',
        headers: {"X-My-Custom-Header": "some value"},
        beforeSend: function (xhr) {
            xhr.setRequestHeader ("Authorization", "Bearer AAAAAAAAAAAAAAAAAAAAAD7%2FzQAAAAAAI8%2FRXWmRrDA8H%2F8%2BkKAYl2y%2BhAg%3DVDO00tkNkdsMPOiqCw31w641eV1a2DZwE3O9b0Ll5nvOMdgjas");
        },
        success: function(data) { 
            // alert("Tweeted!");
            console.log(data);
        },
        error:function(exception){
            alert("Exeption:"+exception);
        }
    });
    */
}

search();
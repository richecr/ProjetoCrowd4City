async function teste() {
    var cb = new Codebird;
    cb.setConsumerKey("rrUDLNZVqv8DaWX6fkmNrB5V9", "R20GkXiu42758yyy5pfykcswYA7Lnn9rBjhQEN25jMCPYO1YS7");
    cb.setToken("2455702491-8jbRT6j6tLv5JHkL7WAac31ZfAAcluFRSDsWXXK", "AuaU4YduVSXtcN1oxrbpYs0E3p3AES0xekg6lCzXEtEHW");
    cb.__call("search_tweets", "q=lixo rua calçada", function(reply) {
        console.log(reply);
    });
}
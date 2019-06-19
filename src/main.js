// Controle de tweets.
var index = 0;
const tweets = [];

// Renderização.
const div = document.getElementById("div-tweet");
const btnSim = document.getElementById("btnSim");
const btnNao = document.getElementById("btnNao");

async function main() {
    await carregaTweets();
}

function proximo() {
    index++;
    render();
}

function render() {
    div.innerHTML = "";
    let h3 = document.createElement("h3");
    let p = document.createElement("p");
    
    h3.innerText = tweets[index]['user']['screen_name'];
    p.innerText = tweets[index]['full_text'];

    div.appendChild(h3);
    div.appendChild(p);
}

function nao() {
}

function sim() {
}


async function carregaTweets() {
    let response = await axios.get(BASE_URL + "/educacao/dados.json");
    tweets = response.data;

    let response1 = await axios.get(BASE_URL + "/lixo/dados.json");
    addTweets(response1.data);

    let response2 = await axios.get(BASE_URL + "/poluicaoSonora/dados.json");
    addTweets(response2.data);

    let response3 = await axios.get(BASE_URL + "/saude/dados.json");
    addTweets(response3.data);

    let response4 = await axios.get(BASE_URL + "/seguranca/dados.json");
    addTweets(response4.data);
}

function addTweets(colecao) {
    colecao.forEach(element => {
        tweets.push(element);
    });
}

main();
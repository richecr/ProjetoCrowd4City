window.search = search;
var html;
// campina grande: geocode=-7.230677,-35.881639,1mi
async function search() {
    
    // Buscando os tweets
    /*
    let response = await axios.get("http://localhost:3001/search/Eu, que nunca tive sorte em nada");
    let dados = response.data;
    console.log(dados);
    */
    
    // Pegando link do meu tweet.
    /*
    let response = await axios.get("http://localhost:3001/show/1126443732839088130");
    let dados = response.data;
    
    let lista = dados['text'].split(" ");
    console.log(lista[lista.length-1]);
    */

    // Pegando curtidas.
    /*
    let response = await axios.get("http://localhost:3001/tweet/favorites/1126444918736596992");
    let dados = response.data;
    console.log(dados['curtidas']);
    */

    // TESTES
    /*
    let response = await axios.get("http://localhost:3001/textoCompleto/1129022426325635073");
    let dados = response.data;
    let res = dados.split(' ');
    let resultado = res[res.length - 1];

    console.log(resultado);
    */

    let response = await axios.post("http://localhost:3001/retweetar/1135528177026183168");
    let dados = response.data;
    console.log(dados);

}

async function search1() {
    let response = await axios.get("http://localhost:3001/search/lixos na rua");
    let dados = response.data;
    console.log(dados);
}

async function search2() {
    let response = await axios.post("http://localhost:3001/unretweetar/1135528177026183168");
    let dados = response.data;
    console.log(dados);
}
var cont = 0;
var tweets = [];

async function buscar(max_id) {
    if (max_id != undefined) {
        let response = await axios.get("http://localhost:3001/search/lixos na rua?max="+max_id);
        let dados = response.data;
        dados.statuses.forEach(element => {
            tweets.push(element);
        });

        if (cont <= 7) {
            cont++;
            let ultimoIndice = dados.statuses.length - 1;
        
            buscar( dados.statuses[ultimoIndice].id_str );
        }
    } else {
        let response = await axios.get("http://localhost:3001/search/lixo na rua");
        let dados = response.data;
        dados.statuses.forEach(element => {
            tweets.push(element);
        });
        let ultimoIndice = dados.statuses.length - 1;
        
        buscar( dados.statuses[ultimoIndice].id_str );
    }
}

async function carregar() {
    const response = await axios.get("./dados/dados.json");
    const dados = response.data;

    console.log(dados);
}
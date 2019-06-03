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
    let response = await axios.get("http://localhost:3001/search/Campina grande");
    let dados = response.data;
    console.log(dados);
}

async function search2() {
    let response = await axios.post("http://localhost:3001/unretweetar/1135528177026183168");
    let dados = response.data;
    console.log(dados);
}
window.search = search;

// campina grande: geocode=-7.230677,-35.881639,1mi
async function search() {
    
    // Buscando os tweets
    /*
    let response = await axios.get("http://localhost:3001/search/campina?count=5&geocode=-7.230677,-35.881639,1mi");
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
    let response = await axios.get("http://localhost:3001/tweet/favorites/1126444918736596992");
    let dados = response.data;
    console.log(dados['curtidas']);
}
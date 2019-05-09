window.search = search;

async function search() {
    //let a = await fetch("http://localhost:3001/search", { mode: 'no-cors'} );
    let response = await axios.get("http://localhost:3001/search/lixo rua calçada?count=5");
    let dados = response.data;

    console.log(dados);
}
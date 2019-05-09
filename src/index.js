window.search = search;

async function search() {
    let response = await axios.get("http://localhost:3001/search/campina?count=5&geocode=-7.230677,-35.881639,1mi");
    let dados = response.data;

    console.log(dados);
}
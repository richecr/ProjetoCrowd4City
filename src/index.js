window.search = search;

// campina grande: geocode=-7.230677,-35.881639,1mi
async function search() {
    // let response = await axios.get("http://localhost:3001/search/campina?count=5&geocode=-7.230677,-35.881639,1mi");
    
    let response = await axios.get("http://localhost:3001/show/1126443732839088130");
    let dados = response.data;

    console.log(dados);
}
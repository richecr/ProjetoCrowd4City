window.search = search;

async function search() {
    //let a = await fetch("http://localhost:3001/search", { mode: 'no-cors'} );
    let a = await axios.get("http://localhost:3001/search/lixo rua calçada?count=5", {mode: 'no-cors'});
    console.log(a.data);
}
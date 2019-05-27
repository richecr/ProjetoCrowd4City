const express = require('express');
const axios = require('axios');

// Inicializando o express.
var app = express();

// Liberando os cors.
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type,Authorization');
    next();
});

// AAAAAAAAAAAAAAAAAAAAADI%2B%2BgAAAAAATg0ZaIKGbfcdNcsjR97sQagkJ7c%3DrMrJ0oAMd373RAwQ4k5YDJm204hsaSkxhg05pmJEH26doMx5Ke

// Avisando ao servidor qual a página root.
app.use(express.static('public'));
app.use(express.json());
app.use(require('./routes/base/routes.js'));

// Liberando a porta 3001 para o servidor.
app.listen(3001, () => console.log("Servidor rodando na porta mágica: 3001"));
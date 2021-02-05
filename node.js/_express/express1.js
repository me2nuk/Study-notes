const express = require('express');
const app = express();

app.get('/', function(req, res){
    console.log('0.0.0.0:80 Connect');
    res.send('hello');
});

app.listen(80,'0.0.0.0');
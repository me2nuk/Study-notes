const express = require('express');
const app = express();
const app2 = express();

app.get('/', function(req, res){
    console.log('0.0.0.0:80 Connect');
    res.send('hello port 80');
});

app2.get('/', function(req, res){
    console.log('0.0.0.0:8080 Connect');
    res.send('hello port 8080');
});

app.listen(80,'0.0.0.0');
app2.listen(8080,'0.0.0.0');
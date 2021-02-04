const express = require('express');
const app = express();
const app2 = express();

app.get('/:id/:user', function(req, res){
    //url => example.com/id1/user2?string=a
    console.log(req.params.id);//id1
    console.log(req.params.user);//user2
    console.log(req.query.string);//a
    res.send('a');
});


app.listen(80,'0.0.0.0');
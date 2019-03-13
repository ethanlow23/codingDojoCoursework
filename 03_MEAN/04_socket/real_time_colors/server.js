var express = require('express');
var app = express();
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
const server = app.listen(8000);
const io = require('socket.io')(server);
var color = 'white';
io.on('connection', function(socket){
    socket.emit('updated', {color});
    socket.on('clicked', function(data){
        color = data.color;
        io.emit('updated', {color});
    });
});
app.get('/', function(req, res){
    res.render('index');
});
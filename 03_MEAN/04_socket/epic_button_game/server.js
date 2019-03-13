var express = require('express');
var app = express();
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
const server = app.listen(6789);
const io = require('socket.io')(server);
var counter = 0;
io.on('connection', function(socket){
    socket.emit('updated_counter', {counter});
    socket.on('count', function(){
        counter++;
        io.emit('updated_counter', {counter});
    });
    socket.on('reset', function(data){
        counter = 0;        
        io.emit('reset_counter', {counter});
    });
});
app.get('/', function(req, res){
    res.render('index');
});

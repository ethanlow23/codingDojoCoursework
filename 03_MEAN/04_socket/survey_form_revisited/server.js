const express = require('express');
const app = express();
app.use(express.static(__dirname + '/public'));
const server = app.listen(1337);
const io = require('socket.io')(server);
var counter = 0;
io.on('connection', function (socket) {
  socket.on('posting_form', function(data){
    var name = data.name;
    var location = data.location;
    var language = data.language;
    var comment = data.comment;
    socket.emit('updated_message', {msg: "name: " + name + " location: " + location + " language: " + language + " comment: " + comment});
    socket.emit('random_number', {rand: Math.floor(Math.random() * 1000 + 1)});
  });
});
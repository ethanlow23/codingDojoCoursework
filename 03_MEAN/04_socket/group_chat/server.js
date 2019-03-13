var express = require('express');
var app = express();
app.use(express.static(__dirname + '/static'));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
const server = app.listen(8000);
const io = require('socket.io')(server);
var current_users = [];
var id = 0;
var messages = [];
io.on('connection', function(socket){
    socket.emit('all_messages', {messages});
    socket.emit('current_users', {current_users});
    socket.on('got_a_new_user', function(data){
        id++;
        var new_user = {id: id, username: data.username};
        current_users.push(new_user);
        io.emit('new_user', {new_user});
        socket.on('disconnect', function(){
            io.emit('disconnect_user', {id: new_user.id});
            for(var i=0; i<current_users.length; i++){
                if(current_users[i].id === new_user.id){
                    current_users.splice(i, 1);
                };
            };
        });
        socket.on('new_msg', function(data){
            var msg_data = {username: new_user.username, msg: data.message};
            messages.push(msg_data);
            io.emit('post_msg', {msg_data});
        });
    });
});
app.get('/', function(req, res){
    res.render('index');
});
var express = require('express');
var session = require('express-session');
var app = express();
app.use(session({
    secret: 'keyboardkitteh',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}))
app.use(express.static(__dirname + '/static'));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.get('/', function(req, res){
    if(req.session.counter === undefined){
        req.session.counter = 0;
    }else{
      req.session.counter++;
    };
    res.locals.counter = req.session.counter;
    res.render('counter');
});
app.post('/plus_two', function(req, res){
    req.session.counter += 1;
    res.locals.counter = req.session.counter;
    res.redirect('/');
});
app.post('/reset', function(req, res){
    req.session.counter = 0;
    res.locals.counter = req.session.counter;
    res.redirect('/');
});
app.listen(8000, function(){
    console.log("listening on port 8000");
});

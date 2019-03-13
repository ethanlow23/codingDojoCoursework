var express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var app = express();
app.use(session({
    secret: 'keyboardkitteh',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}));
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + '/static'));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.post('/result', function(req, res){
    req.session.name = req.body.name;
    req.session.location = req.body.location;
    req.session.language = req.body.language;
    req.session.comment = req.body.comment;
    res.redirect('/result');
});
app.get('/result', function(req, res){
    res.locals.name = req.session.name;
    res.locals.location = req.session.location;
    res.locals.language = req.session.language;
    res.locals.comment = req.session.comment;
    res.render('results');
});
app.listen(8000, function(){
    console.log("listening on port 8000");
});
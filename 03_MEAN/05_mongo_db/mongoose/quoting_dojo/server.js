var express = require('express');
var app = express();
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/quoting_dojo');
var UserSchema = new mongoose.Schema({
    name: {type: String, required: [true, "name cannot be blank"]},
    quote: {type: String, required: [true, "quote cannot be blank"]}
}, {timestamps: true});
mongoose.model('Quote', UserSchema);
var Quote = mongoose.model('Quote');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname + '/static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
var session = require('express-session');
app.use(session({
    secret: 'keyboardkitteh',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}));
const flash = require('express-flash');
app.use(flash());
app.get('/', function(req, res){
    res.render('index');
});
app.get('/quotes', function(req, res){
    Quote.find({}, function(err, quotes){
        if(err){console.log(err)};
        res.render('quotes', {quotes});
    }).sort({createdAt: -1});
});
app.post('/quotes', function(req, res){
    var quote = new Quote(req.body);
    quote.save(function(err){
        if(err){
            console.log("We have errors: ", err.errors);
            for(var key in err.errors){
                console.log(key);
                req.flash('quotes', err.errors[key].message);
            };
            res.redirect('/');
        }else{
            res.redirect('/quotes');
        };
    });
});
app.listen(8000);
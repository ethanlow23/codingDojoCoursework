var express = require('express');
var app = express();
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/login_registration');
var userSchema = new mongoose.Schema({
    email: {type: String, required: [true, 'enter email'], match: [/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/, 'enter a valid email address']},
    first_name: {type: String, required: [true, 'enter first name']},
    last_name: {type: String, required: [true, 'enter last name']},
    password: {type: String, required: [true, 'enter password']},
    birthday: {type: Date}
}, {timestamps: true});
mongoose.model('User', userSchema);
var User = mongoose.model('User');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));
var path = require('path');
app.use(express.static(path.join(__dirname + '/static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
var session = require('express-session');
app.set('trust proxy', 1);
app.use(session({
    secret: 'keyboardkitteh',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}));
const flash = require('express-flash');
app.use(flash());
const bcrypt = require('bcrypt');
app.get('/', function(req, res){
    res.render('index');
});
app.post('/register', function(req, res){
    bcrypt.hash(req.body.password, 10, function(err, hash){
        var user = new User({email: req.body.email, first_name: req.body.first_name, last_name: req.body.last_name, password: hash, birthday: req.body.birthday});
        user.save(function(err){
            if(err){
                console.log(err);
                res.redirect('/');
            }else{
                req.session.email = user.email;
                req.session.first_name = user.first_name;
                res.redirect('/result');
            }
        });
    });
});
app.post('/login', function(req, res){
    User.findOne({email: req.body.email}, function(err, user){
        if(!user){
            res.redirect('/');
        }else{
            bcrypt.compare(req.body.password, user.password, function(err, result){
                if(result){
                    req.session.email = user.email;
                    req.session.first_name = user.first_name;
                    res.redirect('/result');
                }else{
                    res.redirect('/');
                }
            });
        }
    });
});
app.get('/result', function(req, res){
    res.locals.first_name = req.session.first_name;
    res.render('result');
});
app.listen(8000);

var express = require('express');
var app = express();
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/mongoose_dashboard');
var userSchema = new mongoose.Schema({
    name: {type: String, required: [true, 'enter an animal']}
}, {timestamps: true});
mongoose.model('Animal', userSchema);
var Animal = mongoose.model('Animal');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));
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
    Animal.find({}, function(err, animals){
        if(err){console.log(err)}
        res.render('index', {animals});
    });
});
app.get('/animals/new', function(req, res){
    res.render('new');
});
app.get('/animals/:id', function(req, res){
    Animal.findOne({_id: req.params.id}, function(err, animal){
        if(err){console.log(err)}
        console.log(animal);
        res.render('show', {animal});
    });
});
app.post('/animals', function(req, res){
    var animal = new Animal({name: req.body.name});
    animal.save(function(err){
        if(err){
            console.log(err);
            for(var key in err.errors){
                req.flash('animals', err.errors[key].message);
            };
            res.redirect('/animals/new');
        }else{
            res.redirect('/');
        }
    });
});
app.get('/animals/edit/:id', function(req, res){
    var id = req.params.id;
    res.render('edit', {id});
});
app.post('/animals/:id', function(req, res){
    Animal.update({_id: req.params.id}, {$set: {name: req.body.name}}, function(err){
        if(err){
            console.log(err);
            for(var key in err.errors){
                req.flash('animals', err.errors[key].message);
            };
            res.redirect('/animals/edit/' + req.params.id);
        }else{
            res.redirect('/animals/' + req.params.id);
        }
    });
});
app.post('/animals/destroy/:id', function(req, res){
    Animal.remove({_id: req.params.id}, function(err){
        if(err){console.log(err)}
        res.redirect('/');
    });
});
app.listen(8000);
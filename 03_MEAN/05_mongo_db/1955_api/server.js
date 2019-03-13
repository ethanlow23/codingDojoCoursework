const express = require('express');
const app = express();
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/1955_api');
const userSchema = new mongoose.Schema({
    name: String,
}, {timestamps: true});
mongoose.model('User', userSchema);
const User = mongoose.model('User');
const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.get('/', function(req, res){
    User.find({}, function(err, users){
        if(err){
            res.json({message: 'error', error: err});
        }else{
            res.json({message: 'success', users});
        }
    });
});
app.get('/new/:name', function(req, res){
    User.create({name: req.params.name}, function(err, data){
        if(err){
            res.json({message: 'error', error: err});
        }else{
            res.json({message: 'success', data});
        }
    });
});
app.get('/remove/:name', function(req, res){
    User.remove({name: req.params.name}, function(err){
        if(err){
            res.json({message: 'error', error: err});
        }else{
            res.json({message: 'success'});
        }
    });
});
app.get('/:name', function(req, res){
    User.findOne({name: req.params.name}, function(err, user){
        if(err){
            res.json({message: 'error', error: err});
        }else{
            res.json({message: 'success', user})
        }
    });
});
app.listen(8000);
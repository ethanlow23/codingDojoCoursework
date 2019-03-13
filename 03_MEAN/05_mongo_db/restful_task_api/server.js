const express = require('express');
const app = express();
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/restful_routing');
const taskSchema = new mongoose.Schema({
    title: String,
    description: {type: String, default: ""},
    completed: {type: Boolean, default: false}
}, {timestamps: true});
mongoose.model('Task', taskSchema);
const Task = mongoose.model('Task');
const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.get('/tasks', function(req, res){
    Task.find({}, function(err, tasks){
        if(err){
            res.json({error: err});
        }else{
            res.json({tasks});
        }
    });
});
app.get('/tasks/:id', function(req, res){
    Task.findOne({_id: req.params.id}, function(err, task){
        if(err){
            res.json({error: err});
        }else{
            res.json({task});
        }
    });
});
app.post('/tasks', function(req, res){
    Task.create(req.body, function(err, task){
        if(err){
            res.json({error: err});
        }else{
            res.redirect('/tasks/' + task.id);
        }
    });
});
app.put('/tasks/:id', function(req, res){
    Task.update({_id: req.params.id}, {$set: req.body}, function(err){
        if(err){
            res.json({error: err});
        }else{
            res.redirect('/tasks/' + req.params.id);
        }
    });
});
app.delete('/tasks/:id', function(req, res){
    Task.remove({_id: req.params.id}, function(err){
        if(err){
            res.json({error: err});
        }else{
            res.redirect('/tasks');
        }
    });
});
app.listen(8000);
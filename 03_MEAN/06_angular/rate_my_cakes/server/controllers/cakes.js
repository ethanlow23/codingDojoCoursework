const mongoose = require('mongoose'),
Cake = mongoose.model('Cake'),
Rating = mongoose.model('Rating');
module.exports = {
    index: function(req, res){
        Cake.find({}, function(err, data){
            if(err){
                res.json({'error': err});
            }else{
                res.json({'message': 'success', data});
            }
        })
    },
    ratings: function(req, res){
        Cake.find({_id: req.params.id}, function(err, data){
            if(err){
                res.json({'error': err});
            }else{
                res.json({'message': 'success', data});
            }
        })
    },
    create: function(req, res){
        Cake.create(req.body, function(err, data){
            if(err){
                res.json({'error': err});
            }else{
                res.json({'message': 'success', data});
            }
        })
    },
    rating: function(req, res){
        Rating.create(req.body, function(err, data){
            if(err){
                res.json({'error': err});
            }else{
                Cake.findOneAndUpdate({_id: req.params.id}, {$push: {ratings: data}}, function(err, cake){
                    if(err){
                        res.json({'error': err});
                    }else{
                        res.json({'message': 'error', cake});
                    }
                })
            }
        })
    }
}
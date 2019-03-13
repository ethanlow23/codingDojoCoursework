const mongoose = require('mongoose'),
Game = mongoose.model('Game')
module.exports = {
    index: function(req, res){
        Game.find({}, function(err, data){
            if(err){
                res.json({message: 'error', error: err});
            }else{
                res.json(data);
            }
        })
    },
    create: function(req, res){
        Game.create({gold: 0}, function(err, game){
            if(err){
                res.json({message: 'error', error: err});
            }else{
                res.send(game);
            }
        })
    }
} 
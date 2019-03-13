var quotes = require('../controllers/games.js');
module.exports = function(app){
    app.get('/', function(req, res){
        games.index(req, res);
    });
    app.post('/', function(req, res){
        games.create(req, res);
    });
};
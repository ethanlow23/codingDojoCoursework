const cakes = require('../controllers/cakes.js');
module.exports = function(app){
    app.get('/cakes', function(req, res){
        cakes.index(req, res);
    });
    app.get('/cakes/:id', function(req, res){
        cakes.ratings(req, res);
    })
    app.post('/cakes', function(req, res){
        cakes.create(req, res);
    });
    app.post('/cakes/:id', function(req, res){
        cakes.rating(req, res);
    });
}
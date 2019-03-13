const mongoose = require('mongoose');
const Quote = mongoose.model('Quote');
module.exports = {
    index: function(req, res){
        res.render('index');
    },
    display: function(req, res){
        Quote.find({}, function(err, quotes){
            if(err){console.log(err)};
            res.render('quotes', {quotes});
        }).sort({createdAt: -1});
    },
    create: function(req, res){
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
    }
}
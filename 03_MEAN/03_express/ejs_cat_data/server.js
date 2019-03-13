var express = require('express');
var app = express();
app.use(express.static(__dirname + '/static'));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.get('/cats', function(request, response){
    response.render('cats');
});
app.get('/details', function(request, response){
    var cat_array = [
        {name: "cat", food: "cat food", spot: "couch", img: "./images/sleepy_cat.jpg"}
    ];
    response.render('details', {cat: cat_array});
});
app.listen(8000, function() {
    console.log("listening on port 8000");
  });
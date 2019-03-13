const express = require('express');
const app = express();
app.use(express.static(__dirname + '/ninja-gold/dist/ninja-gold'));
require('./server/models/game.js');
const session = require('express-session');
app.use(session({
    secret: 'keyboardkitteh',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
}));
const bodyParser = require('body-parser');
require('./server/config/routes.js')(app);
require('./server/config/mongoose.js')();
app.listen(8000);
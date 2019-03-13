const express = require('express');
const app = express();
app.use(express.static(__dirname + '/angular-app/dist/angular-app'));
require('./server/models/cake.js');
const bodyParser = require('body-parser');
app.use(bodyParser.json());
require('./server/config/routes.js')(app);
require('./server/config/mongoose.js')();
app.listen(8000);
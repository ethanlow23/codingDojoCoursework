const express = require('express');
const app = express();
app.use(express.static(__dirname + '/angular-app/dist/angular-app'));
app.listen(8000);
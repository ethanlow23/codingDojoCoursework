const express = require('express');
const app = express();
app.use(express.static('./pokemon-angular/dist/pokemon-angular'));
app.listen(8000);
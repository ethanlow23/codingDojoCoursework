const mongoose = require('mongoose');
const GameSchema = new mongoose.Schema({
    gold: {type: Number, required: true},
    log: {type: String, default: ''}
})
module.exports = mongoose.model('Game', GameSchema);
const mongoose = require('mongoose');
var UserSchema = new mongoose.Schema({
    name: {type: String, required: [true, "name cannot be blank"]},
    quote: {type: String, required: [true, "quote cannot be blank"]}
}, {timestamps: true});
module.exports = mongoose.model('Quote', UserSchema);
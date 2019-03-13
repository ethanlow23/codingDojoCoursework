const mongoose = require('mongoose')
const ratingSchema = new mongoose.Schema({
    rating: Number,
    comment: {type: String, required: [true, 'write a comment']}
}, {timestamps: true});
const cakeSchema = new mongoose.Schema({
    baker: {type: String, required: [true, 'enter baker'], default: ''},
    image: {type: String, required: [true, 'enter an image'], default: ''},
    ratings: [ratingSchema]
}, {timestamps: true});
module.exports = mongoose.model('Cake', cakeSchema);
module.exports = mongoose.model('Rating', ratingSchema);
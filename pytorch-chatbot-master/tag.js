const mongoose = require("mongoose");
var Schema = mongoose.Schema;

var tagSchema = new Schema({
    agentName: {
        type: String
    },
    intents: [{
        intentName: { type: String },
        trainingPhrase: {type:[String]},
        response: { type: String }
    }],
    entity: [{
        entityName: { type: String },
        entityValue: [String]
    }]
});

module.exports = mongoose.model("chatbot", tagSchema);
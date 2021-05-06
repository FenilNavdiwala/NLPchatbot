// require('./model/index.js');
const connection = require('./model');
const mongoose = require("mongoose")
const express = require('express');
const application = express();
const path = require("path");
const expressHandlerbars = require("express-handlebars");
const bodyParser = require("body-parser");
const tag = require("./model/tag");
const { resolveMx } = require('dns');
// const tag = mongoose.model("tagSchema");
// const router = express.Router();



application.use(bodyParser.urlencoded({
    extended: true
}));
application.use(bodyParser.json());

application.set('views', path.join(__dirname, "/views/"));

application.engine("hbs", expressHandlerbars({
    extname: "hbs",
    defaultLayout: "mainlayout",
    layoutsDir: __dirname + "/views/layouts"
}));
application.set("view engine", "hbs");

application.get("/", (req, res) => {
    // res.send('<h1>Helllo world</h1>')
    res.render("tag/addOrEdit", {
        viewTitle: "insert Records"
    });
});


application.post("/", (req, res) => {
    // res.send('<h1>Helllo world</h1>')
    // console.log(req.body);
    // console.log("Hello");
    insertRecord(req, res)
});


function insertRecord(req, res) {
    // let intents = {
    //     intentName: req.body.intentname,
    //     trainingPhrase: [{
    //         traingPhrase1: req.body.tp_1,
    //         traingPhrase2: req.body.tp_2,
    //         traingPhrase3: req.body.tp_3,
    //         traingPhrase4: req.body.tp_4,
    //         traingPhrase5: req.body.tp_5,
    //     }],
    //     response: req.body.res
    // };
    // let intents = req.body.intents,

    // let entity = {
    //     entityName: req.body.etityname,
    //     entityValue1: req.body.ev_1,
    //     entityValue2: req.body.ev_2,
    //     entityValue3: req.body.ev_3,
    //     entityValue4: req.body.ev_4,
    //     entityValue5: req.body.ev_5,
    // };

    var newTag = new tag({
        agentName: req.body.agentname,
        intents: [{
            intentName: req.body.intentname,
            trainingPhrase: [req.body.tp_1,
            req.body.tp_2,
            req.body.tp_3,
            req.body.tp_4,
            req.body.tp_5],
            response: req.body.res,
        }],
        entity: [{
            entityName: req.body.etityname,
            entityValue: [req.body.ev_1,
            req.body.ev_2,
            req.body.ev_3,
            req.body.ev_4,
            req.body.ev_5]
        }]

    });
    console.log(newTag);
    console.log(tag);
    newTag.save(function (err, doc) {
        if (err) return console.error(err);
        console.log("inserted succussfully!");
        res.end();
    });
}


application.get("./tag/list", (req, res) => {
    res.json('form list');
});

application.listen("3000", () => {
    console.log("Server started");
});






































































// var MongoClient = require('mongodb').MongoClient;
// var url = "mongodb://localhost:27017/";

// MongoClient.connect(url, function(err, db) {
//   if (err) throw err;
//   var dbo = db.db("chatbot");
//   dbo.createCollection("Agent",function(err, res) {
//     if (err) throw err;
//     console.log("Collection created!");
//     db.close();
//   });
// });
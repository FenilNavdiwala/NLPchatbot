// const {MongoClient} = require('mongodb');

const mongoose = require("mongoose")

mongoose.connect("mongodb+srv://admin:admin123@cluster1.ycoy8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    { useNewUrlParser: true, useUnifiedTopology: true }, (error) => {
        if (!error) {
            console.log("Successful connection")
        }
        else {
            console.log("Error Connecting to Database")
        }
    });
const tag = require("./tag");
//  require('./model1');
// mongoose.connect("mongodb://localhost:27017/agent", {useNewUrlParser:true,useUnifiedTopology: true},(error) =>{
//     if (!error)
//     {
//         console.log("Successful connection")
//     }
//     else
//     {
//         console.log("Error Connecting to Database")
//     }
// }); 


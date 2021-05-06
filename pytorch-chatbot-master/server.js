const { RSA_NO_PADDING } = require("constants");
// import express module
const express = require("express");
// set express to variable
const app = express();
// import request module
const axios = require('axios');
const { charsets } = require("mime");
// const http = require('http').createServer(app);
// const port = 3000;
app.listen(3000, function () {
  console.log("server running on port 3000");
});1

app.get("/", (req, res) => {
  res.sendFile("index.html", { root: __dirname });
});

app.use(express.json()) // for parsing application/json
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded


app.post("/", (req, res) => {
  res.sendFile("index.html", { root: __dirname });
});

app.post("/removeletter", callchatbot);
function callchatbot(req, res) {
  console.log("body POST -> ", req.body.query);
  // console.log(req.body)  
  var spawn1 = require("child_process").spawn;
  // var process = spawn1("python3", ["./pytorch-chatbot-master/chat.py","-o" + req.body.query]);
  var process = spawn1("python3", ["/home/fenil/Desktop/API1/pytorch-chatbot-master/chat.py",req.body.query])
  console.log(req.body.query)
  process.stdout.on("data", function (data) {
    console.log("response TO DATA", data.toString());
    // dataTosend = data.toString;
    // send data to browser
    res.send(data.toString());
    // console.log(res);
    console.log("console DATA",data.toString());

  });
}

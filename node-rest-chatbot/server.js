// const http = require('http');

// const app = require('./app');

// const port = process.env.port || 3000;

// const server = http.createServer(app);

// server.listen(port);


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
});

app.get("/", (req, res) => {
  res.sendFile("index.html", { root: __dirname });
});

app.use(express.json()) // for parsing application/json
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

// app.get("/removeletter", callchatbot);
// function callchatbot(req, res) {
//   console.log("body get -> ", req.body);
//   console.log(req.body)
//   var spawn = require("child_process").spawn;
//   var process = spawn("python3", ["./pytorch-chatbot-master/chat.py" + req.body]);
//   process.stdout.on("data", function (data) {
//     console.log("response 1 data", data.toString());
//     // document.getElementById(data.toString());
//     res.send(data.toString());
//   });
// }
app.post("/", (req, res) => {
  res.sendFile("index.html", { root: __dirname });
});

app.post("/removeletter", callchatbot);
function callchatbot(req, res) {
  console.log("body POST -> ", req.body.query);
  // console.log(req.body)
  var spawn1 = require("child_process").spawn;
  // var process = spawn1("python3", ["./pytorch-chatbot-master/chat.py","-o" + req.body.query]);
  var process = spawn1("python3", ["/home/fenil/Desktop/API1/pytorch-chatbot-master/chat.py", "-o" + req.body.query])
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




// app.post("/test", (req, res) => {
//   console.log("body POST -> ", req.body.query);
//   var spawn1 = require("child_process").spawn;
//   var process = spawn1("python3", ["./pytorch-chatbot-master/chat.py","-o", "--Output" + req.body.query]);
//   process.stdout.on("data", function (data) {
//     console.log("response to DATA",data.toString());
//     // document.getElementById(data.toString());
//     res.send(data.toString());
//   });
// });
// app.post('/post-test', (req, res) => {
//   console.log('Got body:', req.body);
//   res.sendStatus(200);
// });


// app.listen(3000);
// var PythonShell = require('python-shell');

// var options = {
//   mode: 'text',
//   args: [asked]
// };

// PythonShell.run('removeletter.py', options, function (err, results) {
//   if (err) throw err;
//   // results is an array consisting of messages collected during execution
//   console.log('results: %j', results);
// });




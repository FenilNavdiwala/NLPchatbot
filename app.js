var express        = require('express'),
    bodyParser     = require('body-parser'),
    http           = require('http'),
    app            = express();


app.use(bodyParser.json());


// set port
app.set('port', process.env.PORT || 3000);

// create a health check endpoint
app.get('/removeletter', function(req, res) {
  res.send('okay');
});

// start the server
http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});
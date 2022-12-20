var http = require('http')
http.createServer(function(request,response){
    response.writeHead(200,{'content_type':'text/plain'});
    response.end('Hello World\n');
}).listen(3000);
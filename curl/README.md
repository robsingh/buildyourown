# Build Your Own - Curl

## Description
For this challenge we're going to build a curl clone that is focused on making HTTP requests we might use for a RESTful API.
Our curl clone will be able to connect to a server and send the HTTP methods : GET, DELETE, POST and PUT.

## Step 1
In this step, your goal is to read the provided URL from the command line and print out the protocol text that would be sent for
a GET request.

You'll need to write the code to parse the URL and extract:
* The protocol - though for the moment we'll assume this is always going to be HTTP, but you should always check.
* The host.
* The port (we can default this to port 80 for HTTP if not provided).
* The path.

When you run your solution you should get some output like this:
```
% cccurl http://eu.httpbin.org/get
connecting to eu.httpbin.org
Sending request GET /get HTTP/1.1
Host: eu.httpbin.org
Accept: */*
```
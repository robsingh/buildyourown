# Build your Own - Load Balancer

## Description
The challenge is to build your own application layer load balancer.

A load balancer performs the following operations:
* Distributes client requests/network load efficiently across multiple servers.
* Ensures high availability and reliability by sending requests only to servers that are online.
* Provides the flexibility to add or subtract servers as demand dictates.

Therefore our goals for this project are:
* Build a load balancer that can send traffic to two or more servers.
* Health check the servers.
* Handle a server going offline (failing a health check).
* Handle a server coming back online (passing a health check).


## Background Information
A load balancer sits in front of a group of servers and routes client requests across all of the servers that are capable of fulfilling those requests. The intention is to minimise response time and maximise utilisation whilst ensuring that no server is overloaded. If a server goes offline, the load balancer redirects the traffic to the remaining servers and when a new server is added it automatically starts sending requests to it.

Load balancers can work at different levels of the OSI seven-layer network model. For example, most cloud providers offer application load balancers (layer seven) and network load balancers (layer four). The focus is on the layer seven - application load balancer, which will route HTTP requests from clients to a pool of HTTP servers.


## Prerequisites
One must have knowledge of multi-threading, concurency and asynchronous programming before jumping into the implementation of this project.


## Notes on Multi-threading, Concurrency and Asynchronous Programming in Python
- **Multi-threading** :
Multi-threading is the capability of a processor to execute multiple threads concurrently within a single process. A thread is a lightweight unit of execution that operates within the context of a process and shares its resources, such as memory.
Tasks that involve significant waiting time waiting for external events, such as I/O operations, are well-suited for multi-threading because they can use this waiting time to execute other threads.

    In Python, while we can initiate multiple threads using the threading module, true parallelism is limited due to Global Interpreter Lock (GIL). The GIL ensures that only thread executes Python bytecode at a time, which means Python threads are better suited for 
    I/O-bound tasks rather than CPU-bound tasks. For CPU-intensive operations, we may consider alternatives like multiprocessing module, which bypasses the GIL by creating separate processes.

- **Concurrency** :



- **Asynchronous Programming**

## Step 1
<!-- In this step your goal is to create a basic server that can start-up, listen for incoming connections and then forward them to a single server.
The first sub-step then is to create a program (I’ll call it ‘lb’) that will start up and listen for connections on on a specified port (i.e. 80 for HTTP).
Next up we want to forward the request made to the load balancer to a back end server. This involves opening a connection to the back end server, making the same request to it that we received, then passing the result back to the client.
In order to handle multiple clients making requests you’ll need to add some concurrency, either with your programming language’s async framework or threads. -->


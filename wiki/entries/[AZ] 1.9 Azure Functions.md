---
tag: Cloud, Azure
---

#### <mark style="background: #ABF7F7A6;">Serverless Computing</mark>

- Serverless computing means is that it's an abstraction of servers.
- Serverless computing is event driven, resources are only allocated from a direct action.
- There are 3 big benefits of using serverless approach.
	1. no infrastructure management, no administrative tasks like installing an operating system. only concern is the code running a service.
	2. scalability : Serverless computers can scale from nothing to tens of thousands of requests without any configuration.
	3. pay for what you use. You are only charged for the time that takes to run your code instead of paying for the resources if they're not being used.

### <mark style="background: #ABF7F7A6;">Azure Functions</mark>

- Functions are a key component of serverless computing. They're also a general compute platform for running any type of code.
- It is an event-driven, serverless, compute option that doesn’t require maintaining virtual machines or containers.
- Functions can be either **stateless** or **stateful**. When they're stateless (the default), they behave as if they're restarted every time they respond to an event. When they're stateful (called Durable Functions), a context is passed through the function to track prior activity.

##### <mark style="background: #ABF7F7A6;">Characteristics of Azure Functions</mark>

-  In Azure Functions, you're only charged for the CPU cycles/time used while your function runs or the number of code executions.
-  Functions are commonly used when you need to perform work in response to an event (often via a REST request), timer, or message from another Azure service, and when that work can be completed quickly, within seconds or less.

###### <mark style="background: #ABF7F7A6;">REST Request</mark>

A REST request (Representational State Transfer request) is an HTTP request made to interact with resources on a web server that follows the principles of REST architecture. REST is an architectural style that defines a set of constraints for creating web services that are scalable, simple, and can be easily maintained.

In a REST request, the client sends an HTTP request to the server to perform specific operations on resources, such as retrieving data, creating new data, updating existing data, or deleting data.

An HTTP request is a message sent by a client (usually a web browser or application) to a web server. It is a fundamental part of the Hypertext Transfer Protocol (HTTP), which is the protocol used for communication between clients and servers on the World Wide Web.

##### <mark style="background: #ABF7F7A6;">Benefits of Azure Functions</mark>

- Functions scale automatically based on demand, so they may be a good choice when demand is variable.
-  If the needs of the developer's app change, you can deploy the project in an environment that isn't serverless. This flexibility allows you to manage scaling, run on virtual networks, and even completely isolate the functions.

##### <mark style="background: #ABF7F7A6;">Application Hosting using VMs and Containers vs Azure Functions</mark>

1. **VMs and Containers**
	- If you build an app using VMs or containers, those resources have to be “running” in order for your app to function.
	- For example, if you have a web application hosted on VMs or containers, the servers need to be up and running all the time, regardless of whether there are users actively using the application or not.
	- This continuous running of resources can lead to potential inefficiencies and higher costs, as you are paying for the resources even when they are idle or not processing any requests.
2. **Azure Functions**
	- In contrast, Azure Functions allow you to write small pieces of code that respond to specific events or triggers. These functions run only when there is an event to process, and they automatically scale out to handle incoming events.
	- When an event occurs, such as an HTTP request, a message arriving in a queue, or a timer, the Azure Function is automatically triggered, and it wakes up to process that event. After the function finishes processing the event, it goes back to a dormant state, ready to be triggered again when the next event comes in.

##### <mark style="background: #ABF7F7A6;">Other Benefits of Azure Functions over VMs and Containers</mark>

- They are cost effective. You do incur some charges of idle VMs and Cont. and also incur charges of underused ones. In Azure Functions, you're only charged for the CPU time used while your function runs.
- Faster.
- More scalable.


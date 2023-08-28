<h3>For every additional element, why you are adding it</h3>
in this infrastructure I add the load balancer and the ssl 
load balancer is used to increase the capacity and reliability of application.
<h3>What distribution algorithm your load balancer is configured with and how it works</h3
>
I USED THE ROUND-ROBIN ALGORITHM.Round-robin is a load balancing algorithm that distributes incoming network traffic across multiple servers in a circular manner, ensuring that no server is overloaded while others are idle.

In this algorithm, each server is assigned a number and incoming requests are distributed to each server in turn, one at a time. When the last server has been reached, the round-robin algorithm starts again at the first server in the list.

This approach ensures that all servers are utilized evenly and that no single server is overwhelmed with requests. Round-robin load balancing is a simple and effective way to distribute traffic across multiple servers and is commonly used in web applications and other network services.
<h3>Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both</h3>
The load balancer is enable Active-Active setup rather than active passive because In an active-passive configuration, the server load balancer recognizes a failed node and redirects traffic to the next available node but in an active-active configuration, the load balancer spreads out the workload's traffic among multiple nodes.
<h3>How a database Primary-Replica (Master-Slave) cluster works</h3>A Primary-Replica (or Master-Slave) database cluster is a setup where one database instance (the Primary or Master) is responsible for handling all write operations, while one or more other instances (the Replicas or Slaves) are responsible for handling read operations and keeping their data in sync with the Primary.

Whenever a write operation is performed on the Primary, it is immediately replicated to all the Replicas. The Replicas then apply the changes to their own copy of the data, ensuring that they remain in sync with the Primary.

Read operations can be performed on any of the Replicas, which can respond with the most up-to-date data they have available. This helps to distribute read traffic across multiple instances, improving performance and scalability.

In the event that the Primary fails or becomes unavailable, one of the Replicas can be promoted to become the new Primary. This ensures that the cluster remains available and that write operations can continue to be performed.
<h3>What is the difference between the Primary node and the Replica node in regard to the application</h3>
In a distributed system, the primary node is responsible for processing the application's requests and maintaining the current state of the system. The replica nodes are copies of the primary node, which provide fault tolerance and redundancy. They can take over if the primary node fails, ensuring that the system continues to operate without interruption.
<h3>SPOF</h3>
when the primary mysql DB server is down,the load balancer etc
<h3>security issues</h3>
the data all over the network  must be encrypted unless it isn't safe 
<h3> No monitoring</h3>
There is No way of knowing if each servers are well fuctioning
 

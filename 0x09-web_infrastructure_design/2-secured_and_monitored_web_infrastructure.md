<h3>For every additional element, why you are adding it</h3>
Firewalls provide protection against outside cyber attackers by shielding your computer or network from malicious or unnecessary network traffic
Server monitoring software facilitates the monitoring and tracking of a server's performance. This enables users to identify and solve any application hosting and performance issues as well as track changes in the server's function.
<h3>What are firewalls for</h3>
Firewalls provide protection against outside cyber attackers by shielding your computer or network from malicious or unnecessary network traffic
<h3>Why is the traffic served over HTTPS</h3>
because it is  the secured version of HTTP. HTTPS is protected by ssl encription
What is SSL?
SSL stands for Secure Sockets Layer, which is a protocol that provides secure communication over the internet. It encrypts the data that is transmitted between a web server and a web browser, ensuring that sensitive information such as login credentials, credit card details, and personal information are kept safe from hackers and other malicious actors.
<h3>How the monitoring tool is collecting data</h3>
The monitoring tool collects data by continuously scanning and analyzing various sources. It can collect data through network monitoring, log files, system metrics, API calls, and other methods depending on the specific tool and its configuration. The tool may also use agents or sensors installed on the monitored systems to gather data and send it back to the central monitoring server.
<h3>Explain what to do if you want to monitor your web server QPS</h3>
To monitor your web server QPS (queries per second), you can follow these steps:

1. Choose a monitoring tool: There are many monitoring tools available that can monitor web server QPS. Some popular options are Nagios, Zabbix, and Prometheus.

2. Install the monitoring tool: Install the chosen monitoring tool on your server or a separate machine that has access to your server.

3. Configure the monitoring tool: Configure the monitoring tool to monitor the QPS metric for your web server. This will usually involve setting up a data source, such as an API or log file, and configuring the tool to collect and analyze the data.

4. Set up alerts: Set up alerts in the monitoring tool to notify you when the QPS metric exceeds a certain threshold. This will allow you to take action before performance issues become critical.

5. Analyze the data: Use the monitoring tool's dashboard or reporting features to analyze the QPS data and identify trends or anomalies. This will help you optimize your web server performance and identify potential issues before they become critical.
<h3>Why terminating SSL at the load balancer level is an issue</h3>
b/c it leaves the network afer the load balancer unencrypted
<h3>Why having only one MySQL server capable of accepting writes is an issue</h3> if this one MyQSL server is down we no longer
can write and it is not scalable 
<h3>Why having servers with all the same components (database, web server and application server) might be a problem</h3>
it make dificult to maintain it ,it can lead to poor performance


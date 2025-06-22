# firewalls

- a firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules
- typically it is configured to allow or deny traffic based on
  - IP addresses
  - ports
  - and protocols

- typically if you set up a web server in the cloud, you will
  - deny all traffic
  - except TCP incoming traffic on port 22 (SSH)
  - and on port 80 (HTTP) and/or port 443 (HTTPS)

any temporary need (join a debug endpoint on port 9000, for example) can be done
through a SSH tunnel

# Prototype of Digital Twin of network including the Edge

Technical features of the deployment of the Demo can be found in this repository. For this use case the scenario is deployed on a container infrastructure using kubernetes as the management tool. Among all the tools that were considered in the first instance, Kubernetes was finally chosen as it allows dynamic working and efficient management of architectures that consume large computational resources.
In order to emulate the aspects of the behaviour of network equipment without actually using any target real-world networking hardware, KNE (Kubernetes Network Emulator by OpenConfig) is used. The selected tools, the integration process and the scenario descriptors are detailed in the following sections.


# Table of Contents

- [Prerequisites](#prerequisites):
  - [KNE](#kne)
  - [L2S-M](#l2s-m)
- [Overview of the Demo](overview-of-the-Demo)
- [Demo](#demo)
- [ NDT Prototype Deployment Procedure](#ndt-prototype-deployment-procedure)

# Prerequisites

### KNE:
- SO Resources: 
  - Ubuntu 20.04.6 LTS, _GNU/Linux 5.4.0-189-generic x86_64_
  - RAM: 10GB
  - vCPUs: 8
-  A Kubernetes cluster, running Kubernetes v1.27.13. or later, that does not already  have network  load-balancing functionality. _Tested on a 4-node cluster, with kubernetes v1.27.3.
    - Network Plugin: Flannel CNI Plugin installed in the Kubernetes cluster.
    - Network Load-Balancing: The cluster should not have network load-balancing functionality already configured.
- **KNE**: [KNE GitHub Repository](https://github.com/openconfig/kne)
- Docker: Docker is used as the CRI. Follow the [Docker installation guide](https://docs.docker.com/engine/install/). _Tested with version 20.10.21._
- Python: _Tested with version 3.8.10._
- Go: _Tested with version 1.20.1._
- Router Images:
  - Arista cEOS-lab: Download from [Arista's software download page](https://www.arista.com/en/support/software-download). The image must be converted and imported as a Docker container image. _Tested with the cEOS-lab-4.29.2F model._

### L2S-M:

- SO Resources: 
  - Ubuntu 20.04.6 LTS, _GNU/Linux 5.4.0-144-generic x86_64_
  - RAM: 4GB
  - vCPUs: 2
- Kubernetes cluster: Version: MicroK8s v1.31.0 or later. _Tested on a single-node cluster._
    - Install the Multus CNI Plugin in the Kubernetes cluster.
 - **L2S-M**: [L2S-M GitHub Repository](https://github.com/Networks-it-uc3m/L2S-M/tree/main/deployments)


# Overview of the Demo
This demonstration aims to showcase the integration and functionality of the KNE and L2S-M tools by simulating a network and edge infrastructure setup. Here’s a detailed overview of the demo:


1. **Objective:**
    - To validate the integration and interoperability of KNE and L2S-M by testing a real-world scenario where HTTP requests are converted to HTTPS by the reverse proxy.
    - To demonstrate the effectiveness of edge-aware NDT (Network Digital Twin) approach by examining the end-to-end request handling from client to server.
    
2. **Deployment of Network and Edge Infrastructures:**
    - **KNE:** Used to simulate the network environment. 
    - **L2S-M:** Used to simulate the edge environment. 

3. **Demo Configuration:**
    - **Edge Setup:** The edge environment deployed with L2S-M includes a client and a reverse proxy.
    - **Network Setup:** The network environment created with KNE includes a web server.

4. **Test Scenario:**
    - **HTTP Request:** The test involves making an HTTP request from the client (at the edge) to the web server (in the network). 
    - **Reverse Proxy:** The request will pass through a reverse proxy at the edge, which is responsible for converting HTTP requests into HTTPS. Consequently, the web server will receive the request as HTTPS, while the edge client will interact with it as HTTP.



# NDT Prototype Deployment Procedure
The following steps provides a guide for deploying the NDT prototype, including the Edge. Follow the steps below:

### 1. Deploy Network using KNE 
Make sure you have your Kubernetes cluster properly configured and KNE installed. For instructions on how to install KNE, refer to the official installation guide in the repository: [KNE Installation Guide](https://github.com/openconfig/kne/blob/main/docs/setup.md).


### 2. Deploy Edge using L2S-M

Ensure that your Kubernetes cluster is set up and L2S-M is installed. For detailed installation instructions, refer to the official guide: [L2S-M Installation Guide](https://github.com/Networks-it-uc3m/L2S-M/tree/main/deployments).





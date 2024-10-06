# First prototype of Network Digital Twin (NDT) including the Edge 

The technical features of the Demo deployment can be found in this repository. For this use case, the scenario is deployed on a container infrastructure using Kubernetes as the management tool.

To emulate the behavioral aspects of the transport network equipment, KNE (Kubernetes Network Emulator by OpenConfig) has been used. Link-Layer Secure connectivity for Microservice platforms (L2S-M) is used to emulate the network edge.


# Table of Contents

- [KNE and L2S-M Installation Guide](#kne-and-l2s-m-installation-guide):
  - [KNE](#kne)
  - [L2S-M](#l2s-m)
- [Overview of the Demo](overview-of-the-Demo)
- [Demo](#demo)
- [ NDT Deployment Guide](#ndt-deployment-guide)

# Prerequisites

## KNE
This guide assumes that a Kubernetes cluster has already been set up. The cluster should adhere to the following restrictions:

- Use a pod networking add-on compatible with **MetalLB**.
- Use **dockerd** as the Container Runtime Interface (CRI).

### Installation

- For installing **KNE**, follow the instructions provided in the official repository: [KNE GitHub Repository](https://github.com/openconfig/kne).

### Tested Environment

This demo was tested on a 4-node cluster with the following configuration:

- **Kubernetes**: v1.27.3
- **Network Plugin**: Flannel CNI
- **Load Balancer**: MetalLB
- **Docker**: Used as the CRI. Refer to the [Docker installation guide](https://docs.docker.com/engine/install/). v20.10.21.
- **Python**: v3.8.10.
- **Go**: v1.20.1.
- **Router Images**: Arista cEOS-lab. Download the image from [Arista's software download page](https://www.arista.com/en/support/software-download).  
  The image must be converted and imported as a Docker container image.  _Tested with the cEOS-lab-4.29.2F model._

### L2S-M:
This guide assumes that a Kubernetes cluster has already been set up.

### Installation

- For installing **L2S-M**, follow the instructions provided in the official repository: [L2S-M GitHub Repository](https://github.com/Networks-it-uc3m/L2S-M/tree/main/deployments)

### Tested Environment

This demo was tested on a microK8s cluster with the following configuration:
- **Kubernetes**: MicroK8s v1.31.0 or later. _Tested on a single-node cluster._
- **Network Plugin**: Multus CNI.



# Overview of the Demo
The purpose of this demo is to showcase the first prototype of a Network Digital Twin, including the Edge, using KNE and L2S-M, which are open-source projects. The demo involves deploying a network with a web server in the network and a client at the Edge, which will make web requests to the server. Additionally, a proxy will be deployed to handle requests from the client and forward them to the server. The main goal is to demonstrate that HTTP requests are visible at the Edge.
    
1. **Components of the NDT:**
    - **KNE:** Used to emulate the Network. 
    - **L2S-M:** Used to emulate the Edge. 

2. **Validation of the Demo**
The demo demonstrates an HTTP request sent from the client at the Edge to the web server in the network. The request passes through a reverse proxy at the Edge, which converts the HTTP request to HTTPS. Consequently, the web server receives only HTTPS requests, while the client at the Edge operates over HTTP, ensuring secure communication between the Edge and the network.



# NDT Deployment Guide
The following steps provides a guide for deploying the NDT prototype, including the Edge. Follow the steps below:
- ###  Deploy Network using KNE 
    To proceed with the next steps, you should have a functional Kubernetes cluster with KNE installed and operational for topology creation. For detailed installation instructions, please refer to the official guide in the repository [KNE](https://github.com/openconfig/kne/blob/main/docs/setup.md)

    1. 
- ###  Deploy Edge using L2S-M

    Make sure your Kubernetes cluster is properly set up and that L2S-M is installed and operational. For comprehensive installation instructions, please refer to the official guide: L2S-M Installation Guide.
    
    1. 
The following steps provide a guide to deploy the NDT prototype (using cluster with Kind), including the Edge (using cluster microk8s). It is necessary to establish the connections between the network machines and the edge before deploying the steps. Follow the steps below:

## Connection Between Machines with KNE and L2S-M
### Configuration on the Machine Hosting KNE Pods:

### 1. Create a VXLAN interface on the host machine where KNE is running:

Run the following commands on the host machine to create and bring up the VXLAN interface:

```
sudo ip link add vxlan-1 type vxlan id 96 dev enp1s0 dstport 47 remote <remote-ip-host-L2S-M>
sudo ip link set vxlan-1 up
```

### 2. Add the vxlan-1 interface to the bridge created by Kind (e.g., br-62xxxx)
```
sudo brctl addif  br-6200aa9847f8 vxlan-1 
```

### 3. Modify the peer_intf field in the gateway2.yaml file:

3.1.  **Update Network Interface (peer_intf)**

In the gateway2.yaml file, update the peer_intf field to use the network interface eth0. This interface corresponds to the host interface created in Kind and enables proper network connectivity for the container.
```
peer_intf: eth0
```
3.2.  **Update Image Pull Policy (imagePullPolicy)**

In the gateway deployment file (gateway2.yaml), add the IfNotPresent image pull policy. This prevents re-downloading the image if it’s already available on the node, saving time and bandwidth for repeated deployments.
```
image: ghcr.io/yennym3/gateway:latest
imagePullPolicy: IfNotPresent
```
    

## Configuration on the Edge Machine:
- #### Create a VXLAN Interface

Create a VXLAN interface with the following command, replacing <remote-ip> with the IP address of the remote host:
```
sudo ip link add vxlan-1 type vxlan id 96 dev enp1s0 dstport 47 remote  <remote-ip-host-KNE>
sudo ip link set vxlan-1 up
```
    
Once you have configured the connection between the machines, you can continue with the guide to proceed with the scenario [deployment](/README.md#scenario-deployment-on-machines-with-kne-and-l2s-m)


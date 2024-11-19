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
In the gateway2.yaml file, update the peer_intf field to eth0 for link 2, which refers to the connection between the pod and its host machine

```
- uid: 2
    peer_pod: localhost
    local_intf: eth2
    local_ip: 10.0.1.20/24
    **peer_intf: eth0**
```
3.2.  **Update Image Pull Policy (imagePullPolicy)**

In the gateway deployment file (gateway2.yaml), add the IfNotPresent image pull policy. This prevents re-downloading the image if it’s already available on the node, saving time and bandwidth for repeated deployments.
```
image: ghcr.io/yennym3/gateway:latest
imagePullPolicy: IfNotPresent
```
### 4. Load images into a kind cluster
It is necessary to load the images used by the server, gateway and cEOS(routers) in the network into a kind cluster there is a 3 step process:

1. Pull the desired images:

    ```bash
    docker pull ghcr.io/yennym3/server:latest
    docker pull ghcr.io/yennym3/gateway:latest
    ```

2. Load the images gatweway/server into the `kind` cluster:

    ```bash
    kind load docker-image ghcr.io/yennym3/server:latest --name=kne
    kind load docker-image ghcr.io/yennym3/gateway:latest --name=kne
    ```

3. Load the cEOS (Arista) image into the kind cluster:

> NOTE: `ceos:latest` is the default image to use for a node of vendor
> `ARISTA`. It's necessary to download the image from the official Arista website to access the cEOS image. In this demo, the tested version is 4.29.2F


```bash
cat cEOS-lab-4.29.2F.tar | docker import - ceos
kind load docker-image ceos:latest --name=kne
```

You can check a full list of images loaded in your `kind` cluster using:

```bash
docker exec -it kne-control-plane crictl images
```

## Configuration on the Edge Machine:
- #### Create a VXLAN Interface

Create a VXLAN interface with the following command, replacing <remote-ip> with the IP address of the remote host:
```
sudo ip link add vxlan-1 type vxlan id 96 dev enp1s0 dstport 47 remote  <remote-ip-host-KNE>
sudo ip link set vxlan-1 up
```
    
Once you have configured the connection between the machines, you can continue with the guide to proceed with the scenario [deployment](/README.md#scenario-deployment-on-machines-with-kne-and-l2s-m)


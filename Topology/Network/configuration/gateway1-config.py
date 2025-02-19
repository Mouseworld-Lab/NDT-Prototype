import subprocess

comando_addr_eth1 = "ip addr add 192.168.15.2/24 dev eth1"
subprocess.run(comando_addr_eth1, shell=True)

comando_addr_eth2 = "ip addr add 12.12.12.2/24 dev eth2"
subprocess.run(comando_addr_eth2, shell=True)

subredes_eth1 = [
    "11.0.1.0/24",
    "192.168.1.0/24",
    "192.168.2.0/24",
    "192.168.3.0/24",
    "192.168.4.0/24",
    "192.168.5.0/24",
    "192.168.6.0/24",
    "192.168.7.0/24",
    "192.168.8.0/24",
    "192.168.9.0/24",
    "192.168.10.0/24",
    "192.168.11.0/24",
    "192.168.12.0/24",
    "192.168.13.0/24",
    "192.168.14.0/24"
    "192.168.15.0/24",
    "192.168.16.0/24"]


subredes_eth2 = [
    "12.12.12.0/24",
    "10.0.1.0/24",
]

puerta_enlace_eth1 = "192.168.15.1"
puerta_enlace_eth2 = "12.12.12.1"

ruta_por_defecto = "default"


comando_verificar_ruta = f"ip route show | grep {ruta_por_defecto}"

resultado = subprocess.run(comando_verificar_ruta, shell=True, stdout=subprocess.PIPE)

if resultado.returncode == 0:
    comando_eliminar_ruta = f"ip route del {ruta_por_defecto}"
    subprocess.run(comando_eliminar_ruta, shell=True)

comando_ruta_por_defecto = f"ip route add {ruta_por_defecto} via {puerta_enlace_eth2} dev eth2"
subprocess.run(comando_ruta_por_defecto, shell=True)


for subred_eth1 in subredes_eth1:
    comando_subred_eth1 = f"ip route add {subred_eth1} via {puerta_enlace_eth1} dev eth1"
    subprocess.run(comando_subred_eth1, shell=True)

for subred_eth2 in subredes_eth2:
    comando_subred_eth2 = f"ip route add {subred_eth2} via {puerta_enlace_eth2} dev eth2"
    subprocess.run(comando_subred_eth2, shell=True)

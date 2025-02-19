import subprocess

comando_addr = "ip addr add 11.0.1.1/24 dev eth1"
subprocess.run(comando_addr, shell=True)

rutas = [
    "10.0.1.0/24",
    "12.12.12.0/24",
    "192.168.6.0/24", 
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
    "192.168.14.0/24",
    "192.168.15.0/24",  
    "192.168.16.0/24"
]

puerta_enlace = "11.0.1.3"
interfaz = "eth1"
 
ruta_por_defecto = "default"

comando_verificar_ruta = f"ip route show | grep {ruta_por_defecto}"

resultado = subprocess.run(comando_verificar_ruta, shell=True, stdout=subprocess.PIPE)

if resultado.returncode == 0:
    comando_eliminar_ruta = f"ip route del {ruta_por_defecto}"
    subprocess.run(comando_eliminar_ruta, shell=True)

comando_ruta_por_defecto = f"ip route add {ruta_por_defecto} via {puerta_enlace} dev {interfaz}"
subprocess.run(comando_ruta_por_defecto, shell=True)

subprocess.run(comando_addr, shell=True)

for ruta in rutas:
    comando = f"ip route add {ruta} via {puerta_enlace} dev {interfaz}"
    subprocess.run(comando, shell=True)

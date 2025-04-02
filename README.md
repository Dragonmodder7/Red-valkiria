# Red valkiria 

## Descrição:
Este é um script simples e eficaz desenvolvido para realizar testes de fragmentação de pacotes ICMP em sites. A ferramenta envia pacotes ICMP fragmentados para um IP de destino para testar sua capacidade de lidar com tráfego fragmentado, ideal para análise de desempenho de servidores ou testes de segurança.

## Features:

Envia pacotes ICMP fragmentados para o alvo especificado.

Interface simples e interativa no terminal.

Configuração fácil de IP, porta e quantidade de pacotes a serem enviados.

Desenvolvido em Python usando a poderosa biblioteca Scapy.


## Instalação:
Para rodar o script no Termux ou Linux, siga os seguintes passos:

1. Instale o Python e a biblioteca Scapy:

### pkg install python
### pip install scapy


2. Baixe o script:

### git clone https://github.com/Dragonmodder7/Red-Valkiria.git
### cd Red-Valkiria


3. Execute o script:

### python Red-Valkiria.py



## Como usar:

1. Digite o IP do site que você deseja testar.


2. Insira a porta do site (a ferramenta usa ICMP, então a porta é apenas um parâmetro de entrada, sem impacto real no teste).


3. Defina a quantidade de pacotes a serem enviados.


4. O script começará a enviar pacotes ICMP fragmentados para o alvo, exibindo um status de cada envio.



## Exemplo de uso:

IP do site: 192.168.1.1  
Porta do site: 80  
Quantidade de packets: 100

## O desenvolvedor não se responsabiliza por qualquer uso inadequado desta ferramenta.

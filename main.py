import psutil
import tkinter
from tkinter import ttk
import argparse
import signal
import sys
import logging
import time
from uuid import getnode as get_mac
mac = get_mac()
mymacaddr = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
routerip = "192.168.0.1"
addrs = psutil.net_if_addrs()
interface = list(addrs.keys())
def networksearch():
    return 0
#--------------------------------------------------------------
window = tkinter.Tk()
window.title("ARP-Spoofer")
window.geometry("600x600+100+100")
combointerface = tkinter.ttk.Combobox(window, values=interface)
combointerface.current(0)
combointerface.pack()
#---------------------------------------------------------------
combobutton = tkinter.Button(window, text="장치검색", overrelief="solid", width=15, command= networksearch, repeatdelay=1000, repeatinterval=100)
combobutton.pack()
#---------------------------------------------------------------
treeview=tkinter.ttk.Treeview(window, columns=["1", "2"], displaycolumns=["2", "1"])
treeview.pack()

treeview.column("#0", width=70)
treeview.heading("#0", text="host")

treeview.column("1", width=100, anchor="center")
treeview.heading("1", text="ip", anchor="e")

treeview.column("2", width=100, anchor="w")
treeview.heading("2", text="manufacturer", anchor="center")
#---------------------------------------------------------------
killbutton = tkinter.Button(window, text="kill device ", overrelief="solid", width=15, command= networksearch, repeatdelay=1000, repeatinterval=100)
killbutton.pack()
spoofbutton = tkinter.Button(window, text="spoof device", overrelief="solid", width=15, command= networksearch, repeatdelay=1000, repeatinterval=100)
spoofbutton.pack()
wiresharkbutton = tkinter.Button(window, text="open wireshark (after spoof)", overrelief="solid", width=15, command= networksearch, repeatdelay=1000, repeatinterval=100)
wiresharkbutton.pack()
#--------------------------------------------------------------
window.mainloop()
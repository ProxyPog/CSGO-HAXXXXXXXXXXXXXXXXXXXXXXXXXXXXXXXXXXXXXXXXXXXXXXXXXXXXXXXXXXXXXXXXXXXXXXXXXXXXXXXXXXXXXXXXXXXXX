import pymem
import pymem.process
import keyboard
import time

m_iObserverMode = (0x3378)
dwLocalPlayer = (0xD3DD14)

switch = 0



print ("██████╗  █████╗ ██████╗ ██████╗  ██████╗ ████████╗     ██████╗ ███╗   ██╗    ████████╗ ██████╗ ██████╗ ██╗")
print ("██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝    ██╔═══██╗████╗  ██║    ╚══██╔══╝██╔═══██╗██╔══██╗██║")
print ("██████╔╝███████║██████╔╝██████╔╝██║   ██║   ██║       ██║   ██║██╔██╗ ██║       ██║   ██║   ██║██████╔╝██║")
print ("██╔═══╝ ██╔══██║██╔══██╗██╔══██╗██║   ██║   ██║       ██║   ██║██║╚██╗██║       ██║   ██║   ██║██╔═══╝ ╚═╝")
print ("██║     ██║  ██║██║  ██║██║  ██║╚██████╔╝   ██║       ╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝██║     ██╗")
print ("╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝        ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝ ╚═╝     ╚═╝")


pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
while True:
    localplayer = pm.read_int(client + dwLocalPlayer)

    if keyboard.is_pressed("z") and switch == 0:
        pm.write_int(localplayer + m_iObserverMode, 1)
        switch = 1
        time.sleep(0.5)
    elif keyboard.is_pressed("z") and switch == 1:
        pm.write_int(localplayer + m_iObserverMode, 0)
        switch = 0
        time.sleep(0.5)
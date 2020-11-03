import pymem
import pymem.process
import keyboard

dwEntityList = (0x4D523AC)
m_iDefaultFOV = (0x332C)

def main():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    
    while True:
    
        player = pm.read_int(client + dwEntityList)
        iFOV = pm.read_int(player + m_iDefaultFOV)
        
        print(iFOV)
        
        if keyboard.is_pressed("end"):
            pm.write_int(player + m_iDefaultFOV, 100)
            exit(0)
        
        if keyboard.is_pressed("page up"):
            pm.write_int(player + m_iDefaultFOV, 140)
            
        if keyboard.is_pressed("page down"):
            pm.write_int(player + m_iDefaultFOV, 100
            
            
if __name__ == '__main__':
    main()
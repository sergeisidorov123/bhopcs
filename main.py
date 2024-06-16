import pymem.process
import keyboard


pm = pymem.Pymem('cs2.exe')
client = pymem.process.module_from_name(pm.process_handle, 'client.dll').IpbaseOfDll


def bhop():
    while True:
        player = pm.read_uint(client + 0xdea964)
        flags = 0x104
        jump = (client + 0x52bbc7c)
        rjump = pm.read_int(jump)
        if keyboard.is_pressed('space'):
            if player:
                ground_touch = pm.read_int(player + flags)
                if ground_touch == 257 and rjump != 5:
                    pm.write_int(jump, 5)
                else:
                    pm.write_int(jump, 4)


bhop()

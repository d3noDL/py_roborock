
from miio import RoborockVacuum
from micloud import MiCloud
from pynput.keyboard import Events, Listener
from flask import Flask
from flask import request
import asyncio
import websockets

isListening = True;


def setup():
    username = "dino.ctrd@gmail.com" #input("Xiaomi username: ")
    password = "H3e5dkHT!" #input("Xiaomi password: ")

    print("Connecting to Xiaomi cloud...")

    cloud = MiCloud(username, password)
    cloud.login()

    devices = cloud.get_devices()

    print (devices)

    name = str()
    ip = str()
    token = str()
    status = str()

    for device in devices:
        name = device["name"]
        ip = device["localip"]
        token = device["token"]
        status = device["isOnline"]

    rbr = RoborockVacuum(ip, token)

    print ("")
    print ("Connected to Xiaomi cloud")
    print ("")
    print ("Vacuum name: " + name)
    print ("Vacuum ip: " + ip)
    print ("Vacuum token: " + token)
    print ("Is vacuum online: " + str(status))
    print ("")

    # print ("Connecting to " + name + "...")
    # try:
        
    #     rbr.set_sound_volume(1)
    #     print ("Connected to " + name + "!")
    # except:
    #     print ("Connection failed... Is " + name + " on and available?")
    #     quit()
    
    
    return rbr

def clamp(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n

# rbr = setup()

###################################################################

import socket

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 8888  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print (f"Waiting for connections on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"\nConnected by {addr}")
        print()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            print (data)


###################################################################



# app = Flask("Roborock Listener")

# @app.route("/<command>", methods=["POST"])
# def index(command):
    

#     fw_bk = float(request.values.get("fw_bk"))
#     rot = -float(request.values.get("rot"))
    
    
#     match command:
#         case "move":
#             print (fw_bk)
#             print (rot)
#             rbr.manual_control(rot, clamp(fw_bk, -0.3, 0.3))
#             return "Moving"
#         case "start":
#             rbr.manual_start()
#             return "Starting"
#         case "stop":
#             rbr.manual_stop()
#             return "Stopping"
#         case "dock":
#             rbr.home()
#             return "Returning to dock"

#     return "OK"
# app.run(host="0.0.0.0", port=8888)
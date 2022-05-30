from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *
from wakeonlan import send_magic_packet
import time

send_magic_packet('XX.XX.XX.XX.XX.XX')

time.sleep(3)

store = {'client_key': 'YOUR KEY'}

client = WebOSClient("YOUR TV IP")
client.connect()

for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("Please accept the connect on the TV!")
    elif status == WebOSClient.REGISTERED:
        print("Registration successful!")

app = ApplicationControl(client)
apps = app.list_apps()

control = InputControl(client)
control.connect_input()

hulu = [x for x in apps if "hulu" in x["title"].lower()][0]

launch_info = app.launch(hulu)
time.sleep(11)

control.down()
time.sleep(1)
control.down()
time.sleep(1)
control.down()
time.sleep(1)

control.ok()
time.sleep(2)

control.ok()
time.sleep(20)

control.ok()
time.sleep(1)








from pypresence import Presence
import time

client_id = "1116338529509842944"

RPC = Presence(client_id)

RPC.connect()


RPC.update(
    state="Il omor pe acela care o pus examenul pe 15",
    large_image="gnome_face"
)



while True:
    time.sleep(60)
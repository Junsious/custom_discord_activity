from pypresence import Presence
import time

client_id = 'ID' #Сюда вставляем ID вашего приложения, берется он в General Information

RPC = Presence(client_id)
RPC.connect()

print(RPC.update(state="TEXT", details="TEXT", large_image="your_image", small_image="your_image", large_text="TEXT", start=time.time()))  # Set the presence

while True:
    time.sleep(15)

# custom_discord_activity

_В целом как я заметил, на очень много гайдов на эту тему на русском языке, так что начнем_


**Итак, для начала вам стоит зайти на сайт [разработчика discord](https://discord.com/developers/applications)**

**1. Теперь создаем New application**

 ![image](https://github.com/user-attachments/assets/1bdc5155-3e98-4f50-9e7f-6b7e1024f759)


**2. Настройка**

**Далее задаете переходим в Rich Presence**

![image](https://github.com/user-attachments/assets/0d3ca9f3-8a10-4bbe-9a62-be42501fd154)

**И тут выбираете все на свое усмотрение, после чего вам понадобится Show Codde**

![image](https://github.com/user-attachments/assets/560a839c-8b9f-4b42-beb2-75b6255def45)

**Тут смотрим параметры которые у нас получились, но данный код копировать не требуется, мы все же сделаем чуть по другому**

**3. Переходим в удобную IDE**

**Надеюсь у вас уже стоит discord.py и теперь записываем этот код** 


```
from pypresence import Presence
import time

client_id = 'ID' #Сюда вставляем ID вашего приложения, берется он в ![image](https://github.com/user-attachments/assets/ac39841d-bcc0-403c-aab5-37a86a49f5b2)

RPC = Presence(client_id)
RPC.connect()

print(RPC.update(state="Looking like I'm tip-top", details="Tick-tock heavy like a Brinks truck", large_image="image_18_", small_image="photo_2025-01-17_17-44-54", large_text="Получил, дурень?", start=time.time()))  # Set the presence

while True:
    time.sleep(15)
```

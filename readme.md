# Bot-auto-click-Tap-Wizard-2

<p align="center"><img src="https://media.discordapp.net/attachments/585069498986397707/1031894337761595442/unknown.png?width=996&height=535"></p>
<p align="center"><img src="https://media.discordapp.net/attachments/585069498986397707/1031478804507533322/Skin6B_2.png"></p>

# ฟีเจอร์
- เปลี่ยนขนาดหน้าจอเกม
- โหมดป้องกันการ afk
- ตรวจจับ eye of vision
- ตรวจจับ obelisk shard
- การเปิดใช้งาน Totem Spirit
- ปุ่ม Enchant เพียงแค่คลิกปุ่มเดียว
- ปุ่มออกจากโหมด Lantern
- ปุ่มเปิดเกม (ท่านต้องติดตั้งลงในค่าเริ่มต้นของ steam)

# ความต้องการ
- Era 4 
- ปรับ UI ให้เป็นดังนี้ 

<img src="https://cdn.discordapp.com/attachments/585069498986397707/1031475854901006398/unknown.png">

- ปรับในหน้ากระเป๋าให้เป็นแบบนี้ เพื่อใช้งานการเปิด totem อัตโนมัติ

<img src="https://media.discordapp.net/attachments/585069498986397707/1031890519468552242/unknown.png">

ปล.หากเปิดแล้วไม่ทำงานให้คลิกปุ่ม เปลี่ยนขนาดเกม อีกครั้ง

# Install
```cmd
git clone https://github.com/watchakorn-18k/Bot-auto-click-Tap-Wizard-2
cd Bot-auto-click-Tap-Wizard-2
pip install -r requirements.txt
```
`requirements.txt`
```requirements.txt
altgraph==0.17.3
beartype==0.11.0
certifi==2022.9.24
charset-normalizer==2.1.1
cx-Freeze==6.12.0
cx-Logging==3.0
flet==0.1.62
future==0.18.2
idna==3.4
importlib-metadata==5.0.0
keyboard==0.13.5
lief==0.12.2
MouseInfo==0.1.3
oauthlib==3.2.1
packaging==21.3
pefile==2022.5.30
Pillow==9.2.0
PyAutoGUI==0.9.53
PyGetWindow==0.0.9
pyinstaller==5.5
pyinstaller-hooks-contrib==2022.10
PyMsgBox==1.0.9
pyparsing==3.0.9
pyperclip==1.8.2
PyRect==0.2.0
PyScreeze==0.1.28
pytweening==1.0.4
pywin32-ctypes==0.2.0
repath==0.9.0
requests==2.28.1
six==1.16.0
urllib3==1.26.12
watchdog==2.1.9
websocket-client==1.4.1
zipp==3.9.0

```

# Build
```
pyinstaller main.py --noconsole --noconfirm --onefile -n windows-x64-v.0.3-bot-tap-wizard-2
```
```
-n ชื่อไฟล์
```

# Contribute
สามารถเข้ามามีส่วนร่วมได้เลยหากท่านจอยากจะเพิ่มอะไรลงไปจากนั้นสามารถ Pull request ส่งมาได้เลยหากไม่มีส่วนใดขัดข้องกันกับโค้ดเดิม
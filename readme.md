# Bot-auto-click-Tap-Wizard-2

<p align="center"><img src="https://media.discordapp.net/attachments/585069498986397707/1031894337761595442/unknown.png?width=996&height=535"></p>
<p align="center"><img src="https://media.discordapp.net/attachments/585069498986397707/1031478804507533322/Skin6B_2.png"></p>

# ฟีเจอร์
- เปลี่ยนขนาดหน้าจอเกม
- โหมดป้องกันการ afk
- ตรวจจับ eye of vision
- ตรวจจับ obelisk shard
- การเปิดใช้งาน Totem Spirit ทุกๆ 1 ชั่วโมง
- ปุ่ม Enchant เพียงแค่คลิกปุ่มเดียว
- ปุ่มออกจากโหมด Lantern
- ปุ่มเปิดเกม (ท่านต้องติดตั้งลงในค่าเริ่มต้นของ steam)
- awaken อัตโนมัติ
- สุ่ม spell อัตโนมัติหลัง awaken เสร็จ
- เลือกของใน Runic Table อัตโนมัติโดยจะเลือก Jagged Totem และ Gem และ Magic die ตามลำดับ

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
poetry install
```

# Build
```
pyinstaller main.py --noconsole --noconfirm --onefile -n bot-tap-wizard-2 --icon icon.png
```
```
-n ชื่อไฟล์
```

# Poetry Command
```
poetry run start
```

# Flet Hot-Reload
```
poetry shell
flet bot_auto_click_tap_wizard_2/main.py -d
```

# Contribute
สามารถเข้ามามีส่วนร่วมได้เลยหากท่านจอยากจะเพิ่มอะไรลงไปจากนั้นสามารถ Pull request ส่งมาได้เลยหากไม่มีส่วนใดขัดข้องกันกับโค้ดเดิม
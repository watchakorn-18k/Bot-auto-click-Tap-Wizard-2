poetry shell 
pyinstaller bot_auto_click_tap_wizard_2/main.py --noconsole --noconfirm --onefile -n windows-x64-v.0.6-bot-tap-wizard-2 --icon bot_auto_click_tap_wizard_2/icon.png
gh release create v.0.6.1-bot-tap-wizard-2 'dist/windows-x64-v.0.6-bot-tap-wizard-2.exe' --title "windows-x64-v.0.6-bot-tap-wizard-2"

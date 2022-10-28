import os
import itertools
import cmd
file = open("versions.dat", "r")
version_all = list(itertools.chain.from_iterable([x.split() for x in file]))
version_old = float(version_all[-1][2:])
version_last = f"v.{round(version_old + 0.1,1)}"


os.system(f"pyinstaller bot_auto_click_tap_wizard_2/main.py --noconsole --noconfirm --onefile -n windows-x64-{version_last}-bot-tap-wizard-2 --icon bot_auto_click_tap_wizard_2/icon.png")
os.system(f"gh release create {version_last}-bot-tap-wizard-2 dist/{os.listdir('dist')[-1]} --title windows-x64-{version_last}-bot-tap-wizard-2")

file = open("versions.dat", "a") 
file.write(f"{version_last}\n") 
file.close() 





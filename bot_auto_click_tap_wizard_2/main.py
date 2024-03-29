"""
bot game Tap Wizard 2 by wk18k
"""
import flet
from flet import (
    Page,
    Text,
    colors,
    Theme,
    Row,
    Column,
    Container,
    AppBar,
    icons,
    Icon,
    ElevatedButton,
    KeyboardEvent,
    alignment,
    AnimatedSwitcher,
    Image,
    margin,
    Switch,
    TextField,
    Tab,
    Tabs,
    GridView,
)
import pyautogui as auto
import threading
import time
import math
from datetime import datetime, date
import pygetwindow
import os
import random

count_dead = 0
count_enchant = 0
time_sec = 0
state_totem = 0
state_runic = 0
Start_thead_sub_run_bot = False


auto.FAILSAFE = False


def main(page: Page):
    page.title = "บอทเกม"
    page.appbar = AppBar(
        title=Text("TAP WIZARD 2"),
        center_title=True,
        bgcolor=colors.BLUE_GREY_900,
        color=colors.WHITE,
    )
    # auto.screenshot("",region=(0,0, 300, 400))

    def update(func):
        """
        decorator page.update()
        """

        def function_wrapper():
            func()
            return page.update()

        return function_wrapper

    page.scroll = "adaptive"
    page.theme = Theme(font_family="Kanit")
    page.dark_theme = Theme(font_family="Kanit")
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }

    @update
    def change_size():
        """
        chage size window game tap wizard 2
        """
        win = (
            pygetwindow.getWindowsWithTitle("Tap Wizard 2")[0]
            or pygetwindow.getWindowsWithTitle("Lantern Active")[0]
        )
        win.size = (267, 1039)
        win.moveTo(1662, 1)

        change_text.content = text_show
        page.update()
        time.sleep(3)
        change_text.content = Text("")

    @update
    def open_game():
        """
        open game tap wizard 2
        """
        path = os.getlogin()
        try:
            os.startfile(
                r"C:\Users\{0}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Tap Wizard 2.url".format(
                    path
                )
            )
        except:
            alert2.value = r"ไม่พบตัวเกมอยู่ใน C:\Users\{0}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Tap Wizard 2.url".format(
                path
            )
            log_display.controls.append(alert2)

    @update
    def check_postion():
        """
        check position of mouse
        """
        print(auto.position(), auto.pixel(auto.position().x, auto.position().y))
        log.value = (
            f"{auto.position()} {auto.pixel(auto.position().x,auto.position().y)}"
        )
        log.color = colors.ORANGE_500

    def check_postion_current():
        """
        check position of mouse current
        """
        return auto.position().x, auto.position().y  # return x,y

    def update_spell():
        """
        update spell fix freeze spell
        """
        auto.click(1766, 957)
        auto.click(1905, 102)

    @update
    def click_anti_afk():
        """
        anti afk and show amount dead of player all
        """
        x = 1913
        y = 620
        global count_dead
        current_x, current_y = check_postion_current()
        auto.click(x, y) if auto.pixel(x, y) == (119, 0, 112) else None
        count_dead += 1
        text_dead_all.value = f"{count_dead}  ครั้ง"
        text_dead_all_.value = f"{count_dead}  ครั้ง"
        change_deadall.content = (
            text_dead_all
            if change_deadall.content == text_dead_all_
            else text_dead_all_
        )
        update_spell()
        auto.moveTo(current_x, current_y)

    @update
    def change_afk():
        """
        toggle on/off click_anti_afk
        """
        global Is_click_anti_afk
        Is_click_anti_afk = True if Is_click_anti_afk == False else False
        toggle_afk.label = (
            "ปิดโหมดป้องกันการ AFK"
            if Is_click_anti_afk == False
            else "เปิดโหมดป้องกันการ AFK"
        )

    def check_eye_of_vision():
        """
        check eye of vision for get damage and xp more
        """
        x = 1871
        y = 958
        current_x, current_y = check_postion_current()
        auto.click(x, y) if auto.pixel(x, y) == (156, 36, 41) else None
        x_1 = 1849
        y_1 = 186
        time.sleep(0.2)  # deley
        auto.click(x_1, y_1) if auto.pixel(x_1, y_1) == (6, 6, 8) else None
        time.sleep(0.2)  # deley
        auto.click(1902, 104)  # close
        auto.moveTo(current_x, current_y)

    @update
    def change_eye_vision():
        """
        toggle on/off change_eye_vision()
        """
        global Is_eye_of_vision
        Is_eye_of_vision = True if Is_eye_of_vision == False else False
        toggle_eye_vision.label = (
            "ปิดโหมดตรวจจับ Eye Of Vision"
            if Is_eye_of_vision == False
            else "เปิดโหมดตรวจจับ Eye Of Vision"
        )

    @update
    def check_eye_of_vision_ui():
        """
        adjustment for eye of vision beautiful
        """
        text_eye_of_vison.value = "เปิดเนตรแล้ว"
        text_eye_of_vison.color = colors.GREEN_ACCENT_700
        group_eye_vision_img.bgcolor = colors.GREEN_ACCENT_700
        eye_vision_img.src = "https://media.discordapp.net/attachments/585069498986397707/1031371946996277308/AdGiver.png"

    def dead_speed_after_enchant():
        """
        speed up wave after enchant
        """
        x_icon, y_icon = (1807, 954)
        global count_dead
        while True:
            if count_dead % 3 == 0 and count_dead > 20:
                for i in range(3):
                    auto.click(x_icon, y_icon)  # icon
                    time.sleep(0.3)
                    auto.click(1816, 140)  # drink
                    auto.click(1907, 103)  # close
                    time.sleep(40)

    @update
    def check_obelisk_shard():
        """
        check obelisk shard for enchant wave amount
        """
        x_first = 1752
        y_first = 995
        x_two = 1804
        y_two = 261
        x_close, y_close = (1905, 102)
        if count_dead % 3 == 0 and count_dead > 0:
            global count_enchant
            count_enchant += 1
            current_x, current_y = check_postion_current()
            auto.click(x_first, y_first) if auto.pixel(x_first, y_first) == (
                35,
                127,
                133,
            ) else None
            amount_enchant.content = Text(count_enchant)
            page.update()
            time.sleep(0.3)
            auto.click(x_two, y_two) if auto.pixel(x_two, y_two) == (6, 6, 8) else None
            time.sleep(0.1)
            auto.click(x_close, y_close)
            auto.moveTo(current_x, current_y)

    @update
    def click_obelisk_shard():
        """
        Open obelisk shard for enchant
        """
        x_first = 1752
        y_first = 995
        x_two = 1804
        y_two = 261
        x_close, y_close = (1905, 102)
        global count_enchant
        count_enchant += 1
        current_x, current_y = check_postion_current()
        auto.click(x_first, y_first) if auto.pixel(x_first, y_first) == (
            35,
            127,
            133,
        ) else None
        amount_enchant.content = Text(count_enchant)
        page.update()
        time.sleep(0.3)
        auto.click(x_two, y_two) if auto.pixel(x_two, y_two) == (6, 6, 8) else None
        time.sleep(0.1)
        auto.click(x_close, y_close)
        auto.moveTo(current_x, current_y)

    @update
    def change_obelisk():
        """
        toggle on/off change_obelisk()
        """
        global Is_obelisk_shard
        Is_obelisk_shard = True if Is_obelisk_shard == False else False
        toggle_obelisk.label = (
            "ปิดโหมดตรวจจับ Obelisk Shard"
            if Is_obelisk_shard == False
            else "เปิดโหมดตรวจจับ Obelisk Shard"
        )

    @update
    def timer_grime():
        """
        Timer for drink grime potion
        """
        global time_sec
        while True:
            time_sec += 1 if time_sec <= 40 else 40
            time.sleep(1)
            btn_grim.disabled = False if time_sec >= 40 else True
            btn_grim.tooltip = f"ทำให้ตัวละครในเกม Tap Wizard 2 ตายทันทีจะใช้ได้ใน {40-time_sec if time_sec < 40 else 0} วินาที"
            page.update()

    @update
    def dead_now():
        """
        Use Grime Potion
        """
        global time_sec
        x_icon, y_icon = (1807, 954)
        current_x, current_y = check_postion_current()
        auto.click(x_icon, y_icon)  # icon
        time.sleep(0.3)
        auto.click(1816, 140)  # drink
        auto.click(1907, 103)  # close
        auto.moveTo(current_x, current_y)
        time_sec = 0

    def exit_lantern():
        """
        Remove Lantern Mode
        """
        current_x, current_y = check_postion_current()
        auto.click(1794, 876)
        auto.moveTo(current_x, current_y)

    def open_totem_spirit():
        """
        Open totem spirit in game
        """

        def run_open_totem_spirit():
            """
            Function build in
            """
            x = 1714
            y = 379
            adder = 32
            for i in range(6):
                auto.click(x, y)
                time.sleep(0.3)
                auto.click(1794, 470) if i == 0 else auto.click(1797, 486)
                x += adder
            auto.click(1905, 373)  # for exit

        global state_totem
        if state_totem == 0:
            x, y = (1701, 389)
            current_x, current_y = check_postion_current()
            auto.click(1863, 995)
            time.sleep(0.2)
            auto.click(1863, 138)
            time.sleep(0.2)
            state_totem = 1
            run_open_totem_spirit() if auto.pixel(x, y) == (35, 127, 133) else None
            auto.click(1911, 283)
            auto.moveTo(current_x, current_y)
        else:
            if (
                float("%.2f" % math.modf(int(datetime.now().strftime("%H%M")) / 100)[0])
                == 0.01
            ):
                state_totem = 0

    def awakening():
        """
        auto click for awaken character
        """
        current_x, current_y = check_postion_current()
        global wizard

        def check_awaken_btn():
            auto.click(1826, 955) if auto.pixel(1838, 951) == (255, 161, 161) else None
            time.sleep(0.1)
            auto.click(1800, 275) if auto.pixel(1800, 275) == (3, 147, 3) else None
            time.sleep(3)
        
        def check_btn_human_white(): 
            auto.click(1775, 230)
            auto.click(1731,959) 

        def check_charactor_and_select():
            global wizard
            auto.click(1725, 167) if auto.pixel(1735, 252) != (15, 18, 45) else None
            list_wizard = []
            x_wizard, y_wizard = (1697, 287)
            range_wizard = 35
            for i in range(7):
                list_wizard.append((x_wizard, y_wizard))
                x_wizard += range_wizard
            random_wizard = random.choice(list_wizard)
            auto.click(random_wizard)
            wizard = list_wizard.index(random_wizard)
            print("Postion Wizard: ",wizard)
        
        def check_trait():
            auto.click(1762, 164)
            list_trait = []
            x_trait, y_trait = (1760, 271)
            range_trait = 20
            for i in range(3):
                list_trait.append((x_trait, y_trait))
                x_trait += range_trait
            auto.click(random.choice(list_trait))
        
        def check_fate():
            postion_fate = {"Perk_Fairy":(1864, 300)}
            auto.click(1794, 205)
            auto.click(postion_fate["Perk_Fairy"])

        def confirm():
            #btn rember
            auto.click(1788, 167)
            time.sleep(0.2)
            #btn rember
            auto.click(1788, 167)
            time.sleep(0.2)
            #btn confirm
            auto.click(1796, 220)
            time.sleep(0.2)
            #btn confirm
            auto.click(1796, 220)
            #exit
            auto.click(1895, 340)

        def check_procress():

            # start check charactor
            check_charactor_and_select() if auto.pixel(1771, 175) != (29, 39, 99) else None
            #end check charactor

            time.sleep(0.1)
            # start check trait
            check_trait() if auto.pixel(1776, 220) != (29, 39, 99) else None
            #end check trait
            check_fate()
            time.sleep(0.2)
            confirm()


        check_awaken_btn() if auto.pixel(1838, 951) == (255, 161, 161) else None
        # end check click first

        # start check btn human white
        check_btn_human_white() if auto.pixel(1731,959) == (237, 247, 252) else None
        # end check btn human white
        check_procress() if auto.pixel(x=1801, y=222) != (2, 159, 3) else auto.click(x=1801, y=222)
        auto.moveTo(current_x, current_y)

    def choice_spell():
        """
        auto choice spell
        """
        current_x, current_y = check_postion_current()
        
        
        def method_select_spell(wizard_index):
            global wizard
            list_spells = []
            if wizard == 4:
                list_spells = []
                x_spell, y_spell = (1750, 224)
                range_spell = 30
                for i in range(4):
                    list_spells.append((x_spell, y_spell))
                    x_spell += range_spell

                x_spell, y_spell = (1750, 260)
                range_spell = 30
                for f in range(4):
                    list_spells.append((x_spell, y_spell))
                    x_spell += range_spell

                list_spells = random.sample(list_spells, 4)
            else:
                x_spell, y_spell = (1711, 224)
                range_spell = 35
                for i in range(6):
                    list_spells.append((x_spell, y_spell))
                    x_spell += range_spell
                list_spells = random.sample(list_spells, 4)
            return list_spells
        
        def check_space():
            list_space = []
            x_space, y_space = (1739, 152)
            range_space = 35
            for s in range(4):
                list_space.append((x_space, y_space))
                x_space += range_space
            return list_space

        auto.click(1727, 955) if auto.pixel(1707, 116) != (15, 18, 45) else None
        global wizard
        list_spells = method_select_spell(wizard)
        list_space = check_space()

        for f in range(4):
            auto.click(list_spells[f])
            auto.dragTo(list_space[f], button='left', duration=0.15)
        auto.click(1902, 101)
        auto.moveTo(current_x, current_y)

    def choice_runic():
        """ "
        auto choice runic
        """
        global state_runic
        if state_runic == 0:
            current_x, current_y = check_postion_current()
            auto.click(1828, 994) if auto.pixel(1895, 265) != (19, 23, 58) else None

            def loop_choice_runic(x: int, y: int, amount: int):
                for i in range(amount):
                    auto.click(x, y)

            time.sleep(0.2)

            if auto.pixel(1852, 247) == (44, 49, 60):
                """
                jagged Totem
                """
                auto.click(1852, 247)
                loop_choice_runic(1799, 317, 1)

            elif auto.pixel(1852, 246) == (141, 0, 241):
                """
                Gems
                """
                auto.click(1852, 246)
                loop_choice_runic(1799, 317, 6)

            elif auto.pixel(1837, 248) == (255, 253, 245):
                """
                Magic Die
                """
                auto.click(1837, 248)
                loop_choice_runic(1799, 317, 1)
            state_runic = (
                1
                if float(
                    "%.2f" % math.modf(int(datetime.now().strftime("%H%M")) / 100)[0]
                )
                != 0.03
                else 0
            )

            auto.click(1686, 464)
            auto.moveTo(current_x, current_y)

    @update
    def sub_run_bot():
        """
        sub run bot auto click
        """
        global Is_click_anti_afk
        global Is_eye_of_vision
        global Is_obelisk_shard
        global Start_thead_sub_run_bot

        Start_thead_sub_run_bot = True
        while True:
            (
                toggle_afk.disabled,
                toggle_eye_vision.disabled,
                toggle_obelisk.disabled,
            ) = (False, False, False)
            toggle_afk.value = Is_click_anti_afk
            toggle_eye_vision.value = Is_eye_of_vision
            toggle_obelisk.value = Is_obelisk_shard
            click_anti_afk() if auto.pixel(1913, 620) == (
                119,
                0,
                112,
            ) and Is_click_anti_afk == True and auto.pixel(1730, 960) != (
                237,
                247,
                252,
            ) else None
            check_eye_of_vision() if auto.pixel(1871, 958) == (
                156,
                36,
                41,
            ) and Is_eye_of_vision == True else check_eye_of_vision_ui()
            check_obelisk_shard() if auto.pixel(1752, 995) == (
                35,
                127,
                133,
            ) and Is_obelisk_shard == True else None
            awakening() if auto.pixel(1838, 951) == (255, 161, 161,) or auto.pixel(
                1730, 960
            ) == (237, 247, 252) else None
            check_postion()

    @update
    def run_bot():
        """
        run bot auto click
        """
        global Is_click_anti_afk
        global Is_eye_of_vision
        global Is_obelisk_shard
        global Start_thead_sub_run_bot
        threading.Thread(target=timer_grime).start()
        threading.Thread(target=dead_speed_after_enchant).start()
        while True:
            if (
                pygetwindow.getWindowsWithTitle("Tap Wizard 2") != []
                or pygetwindow.getWindowsWithTitle("Lantern Active") != []
            ):
                try:
                    win = pygetwindow.getWindowsWithTitle("Tap Wizard 2")[0]
                    log.value = "ตรวจสอบพบเกม Tap Wizard 2 !"
                    log.color = colors.GREEN_ACCENT_400
                    page.update()
                    break
                except:
                    current_x, current_y = auto.position()
                    try:
                        win = pygetwindow.getWindowsWithTitle("Lantern Active")[0]
                        auto.click(1794, 876)
                        auto.click(current_x, current_y)
                        log.value = "ตรวจสอบพบเกม Tap Wizard 2 !"
                        log.color = colors.GREEN_ACCENT_400
                        page.update()
                    except IndexError:
                        log.value = "ตรวจสอบไม่พบเกมกรุณาเปิดเกม Tap Wizard 2 !"
                        log.color = colors.RED_ACCENT_200
                        toggle_afk.value = Is_click_anti_afk = False
                        toggle_eye_vision.value = Is_eye_of_vision = False
                        toggle_obelisk.value = Is_obelisk_shard = False
                        (
                            toggle_afk.disabled,
                            toggle_eye_vision.disabled,
                            toggle_obelisk.disabled,
                        ) = (True, True, True)
                        change_size_btn.disabled = True
                        page.update()

            else:
                log.value = "ตรวจสอบไม่พบเกมกรุณาเปิดเกม Tap Wizard 2 !"
                log.color = colors.RED_ACCENT_200
                toggle_afk.value = Is_click_anti_afk = False
                toggle_eye_vision.value = Is_eye_of_vision = False
                toggle_obelisk.value = Is_obelisk_shard = False
                (
                    toggle_afk.disabled,
                    toggle_eye_vision.disabled,
                    toggle_obelisk.disabled,
                ) = (True, True, True)
                change_size_btn.disabled = True
                page.update()

        toggle_afk.value = Is_click_anti_afk = True
        toggle_eye_vision.value = Is_eye_of_vision = True
        toggle_obelisk.value = Is_obelisk_shard = True
        while True:
            try:
                if win.width == 267 and win.height == 1039:
                    
                    frac, full = math.modf(int(datetime.now().strftime("%H%M")) / 100)
                    log_display.controls.pop(-1) if len(
                        log_display.controls
                    ) > 2 else None
                    threading.Thread(
                        target=sub_run_bot
                    ).start() if Start_thead_sub_run_bot == False else None

                    choice_spell() if auto.pixel(1742, 952) == (255, 161, 161) else None
                    
                    open_totem_spirit() if frac == 0.0 else None
                    choice_runic() if float(
                        "%.2f"
                        % math.modf(int(datetime.now().strftime("%H%M")) / 100)[0]
                    ) == 0.02 else None
                    exit_lantern() if pygetwindow.getWindowsWithTitle(
                        "Lantern Active"
                    ) != [] else None

                elif win.width != 267 and win.height != 1039:
                    log.value = "ขนาดจอเกมไม่ถูกต้อง กรุณากดปุ่ม เปลี่ยนขนาดเกม"
                    log.color = colors.RED_ACCENT_200
                    toggle_afk.value = Is_click_anti_afk = False
                    toggle_eye_vision.value = Is_eye_of_vision = False
                    toggle_obelisk.value = Is_obelisk_shard = False
                    change_size_btn.disabled = False
                    page.update()
                else:
                    toggle_afk.value = Is_click_anti_afk = False
                    toggle_eye_vision.value = Is_eye_of_vision = False
                    toggle_obelisk.value = Is_obelisk_shard = False
                    (
                        toggle_afk.disabled,
                        toggle_eye_vision.disabled,
                        toggle_obelisk.disabled,
                    ) = (True, True, True)
            except pygetwindow.PyGetWindowException:
                log.value = "ตรวจสอบไม่พบเกมกรุณาเปิดเกม Tap Wizard 2 !"
                log.color = colors.RED_ACCENT_200
                toggle_afk.value = Is_click_anti_afk = False
                toggle_eye_vision.value = Is_eye_of_vision = False
                toggle_obelisk.value = Is_obelisk_shard = False
                (
                    toggle_afk.disabled,
                    toggle_eye_vision.disabled,
                    toggle_obelisk.disabled,
                ) = (True, True, True)
                change_size_btn.disabled = True

                page.update()

    def on_keyboard(e: KeyboardEvent):
        """
        debug
        """
        import pyperclip

        print(
            f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
        )
        check_postion() if e.key == "P" and e.ctrl == True else None
        awakening() if e.key == "A" and e.ctrl == True else None
        choice_spell() if e.key == "T" and e.ctrl == True else None
        pyperclip.copy(
            f"{check_postion_current()}"
        ) if e.key == "C" and e.ctrl == True else None

    page.on_keyboard_event = on_keyboard
    change_size_btn = ElevatedButton(
        "เปลี่ยนขนาดเกม",
        icon=icons.MONITOR,
        on_click=lambda x: change_size(),
        tooltip="เปลี่ยนขนาดหน้าจอเกม Tap Wizard 2 ให้เป็นค่าเริ่มต้น",
    )
    text_show = Text(
        "ปรับขนาดเรียบร้อย", color=colors.GREEN_ACCENT_700, size=12, no_wrap=True
    )
    change_text = AnimatedSwitcher(
        Text(""),
        transition="scale",
        duration=500,
        reverse_duration=100,
        switch_in_curve="bounceOut",
        switch_out_curve="bounceIn",
    )

    text_dead_all = Text("0", color=colors.RED_ACCENT_200)
    text_dead_all_ = Text("0", size=20, color=colors.RED_ACCENT_200)
    change_deadall = AnimatedSwitcher(
        Text("0  ครั้ง"),
        transition="scale",
        duration=500,
        reverse_duration=100,
        switch_in_curve="bounceOut",
        switch_out_curve="bounceIn",
    )

    text_eye_of_vison = Text("ปิดอยู่", color=colors.RED_ACCENT_200)
    eye_vision_img = Image(
        src="https://media.discordapp.net/attachments/585069498986397707/1031371695157674014/AdGiverClosed.png"
    )
    group_eye_vision_img = Container(
        eye_vision_img, bgcolor=colors.RED_ACCENT_400, padding=5
    )

    group_obelisk_img = Container(
        Image(
            src="https://media.discordapp.net/attachments/585069498986397707/1031377037702737941/Obelisk.png"
        ),
        padding=5,
    )
    amount_enchant = AnimatedSwitcher(
        Text("0"),
        transition="scale",
        duration=500,
        reverse_duration=100,
        switch_in_curve="bounceOut",
        switch_out_curve="bounceIn",
    )

    btn_grim = ElevatedButton(
        "ดื่ม Grime Potion",
        icon=icons.COFFEE,
        on_click=lambda x: dead_now(),
        tooltip=f"ทำให้ตัวละครในเกม Tap Wizard 2 ตายทันที",
    )
    toggle_afk = Switch(label="ปิดโหมดป้องกันการ AFK", on_change=lambda x: change_afk())
    toggle_eye_vision = Switch(
        label="ปิดโหมดตรวจจับ Eye Of Vision", on_change=lambda x: change_eye_vision()
    )
    toggle_obelisk = Switch(
        label="ปิดโหมดตรวจจับ Obelisk Shard", on_change=lambda x: change_obelisk()
    )

    log = Text("กำลังตรวจสอบหาเกม...", text_align="center", color=colors.YELLOW_500)
    btn_open_totem = ElevatedButton(
        "เปิดใช้งาน Totem Spirit",
        on_click=lambda x: open_totem_spirit(),
        icon=icons.TRAFFIC,
    )
    btn_enchant = ElevatedButton(
        "Enchant ตัวละคร",
        on_click=lambda x: click_obelisk_shard(),
        icon=icons.DIAMOND,
    )
    alert2 = Text("", size=20, text_align="center", color=colors.RED_ACCENT_200)
    log_display = Column(
        [Text("ข้อมูลทั่วไป", text_align="center"), log],
        horizontal_alignment="center",
    )
    page.add(
        Container(
            Row(
                [
                    Text("🤖 บอท TAP WIZARD 2", size=15, text_align="center"),
                    Text("โดย WK18K", size=15, text_align="center"),
                    Text("DISCORD 18K SERVER", size=15, text_align="center"),
                ],
                alignment="center",
                vertical_alignment="center",
            ),
            alignment=alignment.center,
        )
    )
    page.add(
        Container(
            Column(
                [
                    Row(
                        [
                            group_eye_vision_img,
                            Text("Eve of Vision"),
                            text_eye_of_vison,
                        ],
                        vertical_alignment="center",
                        alignment="center",
                    ),
                    Row(
                        [
                            Row(
                                [
                                    Text(
                                        f"💀 ตัวละครตายทั้งหมด",
                                        text_align="start",
                                    ),
                                    change_deadall,
                                ],
                                vertical_alignment="center",
                                alignment="center",
                            ),
                            Row(
                                [log_display],
                            ),
                            Row(
                                [
                                    group_obelisk_img,
                                    Text("Obelisk Shard Enchant"),
                                    amount_enchant,
                                    Text("ครั้ง"),
                                ],
                                animate_opacity=300,
                                vertical_alignment="center",
                                alignment="center",
                            ),
                        ],
                        alignment="spaceAround",
                    ),
                ],
                horizontal_alignment="center",
            ),
            alignment=alignment.center,
        )
    )
    page.add(
        Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                Tab(
                    icon=icons.ROCKET_LAUNCH,
                    text="ฟังค์ชั่นบอท",
                    content=Column(
                        [
                            Row(
                                [Text("ฟังค์ชั่นบอท", text_align="start")],
                                vertical_alignment="center",
                                alignment="center",
                            ),
                            GridView(
                                [
                                    btn_grim,
                                    ElevatedButton(
                                        "ออกจาก Lantern",
                                        on_click=lambda x: exit_lantern(),
                                        icon=icons.LOCK_CLOCK,
                                    ),
                                    btn_open_totem,
                                    btn_enchant,
                                    ElevatedButton(
                                        "เปิดตัวเกม",
                                        on_click=lambda x: open_game(),
                                        icon=icons.OPEN_IN_NEW,
                                    ),
                                ],
                                runs_count=4,
                                child_aspect_ratio=5.0,
                                spacing=25,
                                run_spacing=25,
                            ),
                        ]
                    ),
                ),
                Tab(
                    icon=icons.ACCESS_TIME,
                    text="บอทอัตโนมัติ",
                    content=Column(
                        [
                            Row(
                                [Text("บอทอัตโนมัติ", text_align="center")],
                                vertical_alignment="center",
                                alignment="center",
                            ),
                            Row(
                                [
                                    Column(
                                        [
                                            toggle_afk,
                                            toggle_eye_vision,
                                            toggle_obelisk,
                                        ],
                                    ),
                                ],
                                spacing=100,
                                run_spacing=100,
                            ),
                        ]
                    ),
                ),
                Tab(
                    text="ตั้งค่าบอท",
                    icon=icons.SETTINGS,
                    content=Column(
                        [
                            Row(
                                [Text("ตั้งค่าบอท", text_align="center")],
                                vertical_alignment="center",
                                alignment="center",
                            ),
                            GridView(
                                [
                                    Container(
                                        Column(
                                            [
                                                change_size_btn,
                                                change_text,
                                            ]
                                        )
                                    )
                                ],
                                runs_count=4,
                                child_aspect_ratio=5.0,
                                spacing=4,
                                run_spacing=50,
                            ),
                        ]
                    ),
                ),
            ],
            expand=1,
        )
    )
    page.update()

    t = threading.Thread(target=run_bot)

    t.start()


def start():
    flet.app(target=main)


if __name__ == "__main__":
    import cProfile

    # cProfile.run("start()")

    flet.app(target=main)

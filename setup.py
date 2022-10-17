from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pyautogui","time","threading","keyboard","flet","pygetwindow"], "excludes": ["tkinter"]}

target = Executable(
    script="main.py",
    base="Win32GUI",
)
setup(
    name="บอทเกม",
    version="0.2",
    description="Bot Tap Wizard 2",
    author = "wk18k",
    executables=[target],
    options={"build_exe": build_exe_options},
)
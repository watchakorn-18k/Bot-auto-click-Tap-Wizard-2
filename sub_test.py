import pyautogui as auto
import random
import time


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


list_space = []
x_space, y_space = (1739, 152)
range_space = 35
for s in range(4):
    list_space.append((x_space, y_space))
    x_space += range_space

for f in range(4):
    auto.click(list_spells[f])
    auto.dragTo(list_space[f], button='left', duration=0.25)
import keyboard
from playsound import playsound
import threading
import random
import sys
import os

def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 播放声音
def play():
    result = random.randint(0,len(sound_list) - 1)
    playsound(os.path.join(sound_path ,sound_list[result]))

# 按下键盘
def Press(x):
    if x.event_type == 'down':
      threading.Thread(target=play).start()

sound_path = resource_path('sound')
# 入口函数
if __name__ == '__main__':

    sound_list  = os.listdir(sound_path)
    keyboard.hook(Press)
    keyboard.wait()
  



from pynput.mouse import Listener
from Imanipulation import tools
from Imanipulation import statments


def on_click(x, y, button, pressed):

    if pressed:
      t1,t2 = tools.ans()
      t1 = t1.replace('\n','')
      print(t1.replace('Question',''))
      print(statments.classify(t2))
      print('deli  : '+t2)
    if not pressed:
        print('realse')


# Collect events until released
with Listener(on_click=on_click) as listener:
    listener.join()

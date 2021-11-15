import tkinter as tk
from random import randint
from time import sleep
from threading import Thread


root = tk.Tk()
root.wm_title('Balloon game - Jiusoft')

fullscreen = False
def enter_fullscreen():
    global fullscreen
    fullscreen = True
    fullscreen_button['text'] = 'Exit fullscreen'
    root.attributes('-fullscreen', True)
def exit_fullscreen():
    global fullscreen
    fullscreen = False
    fullscreen_button['text'] = 'Enter fullscreeen'
    root.attributes('-fullscreen', False)
def enter_or_exit_fullscreen():
    if fullscreen:
        exit_fullscreen()
    elif not fullscreen:
        enter_fullscreen()
fullscreen_button = tk.Button(master=root, text='', command=enter_or_exit_fullscreen)
fullscreen_button.pack(side=tk.RIGHT, anchor=tk.NE)
enter_fullscreen()

score_label = tk.Label(master=root, text='Score: 0')
def set_score(score: int):
    score_label['text'] = f'Score: {score}'
score_label.pack(side=tk.TOP, fill=tk.X)

play_area = tk.Canvas(master=root, bg='snow', width=750, height=750)
play_area.pack(side=tk.TOP)

score = 0
def increase_score(evt):
    global score
    score += 1
    set_score(score)

def create_rectangle_in_random_spot():
    previous_rectangle = None
    try:
        for _ in range(20):
            if previous_rectangle is not None:
                play_area.delete(previous_rectangle)
            base = randint(0, 600)
            rectangle = play_area.create_rectangle(base, base + 50, base + 100, base + 150, fill='red',
                                                   outline='red')
            play_area.tag_bind(rectangle, '<Button-1>', increase_score)
            previous_rectangle = rectangle
            sleep(1.5)
        for _ in range(30):
            play_area.delete(previous_rectangle)
            base = randint(0, 600)
            rectangle = play_area.create_rectangle(base, base + 50, base + 100, base + 150, fill='red',
                                                   outline='red')
            play_area.tag_bind(rectangle, '<Button-1>', increase_score)
            previous_rectangle = rectangle
            sleep(1)
        while True:
            play_area.delete(previous_rectangle)
            base = randint(0, 600)
            rectangle = play_area.create_rectangle(base, base + 50, base + 100, base + 150, fill='red',
                                                   outline='red')
            play_area.tag_bind(rectangle, '<Button-1>', increase_score)
            previous_rectangle = rectangle
            sleep(0.5)
    except RuntimeError:
        pass
Thread(target=create_rectangle_in_random_spot).start()
root.mainloop()

import tkinter as tk
from random import randint
from time import sleep
from threading import Thread


root = tk.Tk()
root.attributes('-fullscreen', True)
root.wm_title('Balloon game - Jiusoft')

score_label = tk.Label(master=root, text='Score: 0')
def set_score(score: int):
    score_label['text'] = f'Score: {score}'
score_label.pack(side=tk.TOP, fill=tk.X)

play_area = tk.Canvas(master=root, bg='snow', width=1000, height=1000)
increase_score_command = None
def set_increase_score_command(command):
    global increase_score_command
    increase_score_command = command
play_area.pack(side=tk.TOP)

def main():
    def create_rectangle_in_random_spot():
        previous_rectangle = None
        try:
            for _ in range(20):
                if previous_rectangle is not None:
                    play_area.delete(previous_rectangle)
                base = randint(0, 850)
                rectangle = play_area.create_rectangle(base, base + 50, base + 100, base + 150, fill='red',
                                                       outline='red')
                play_area.tag_bind(rectangle, '<Button-1>', increase_score_command)
                previous_rectangle = rectangle
                sleep(1.5)
            for _ in range(30):
                play_area.delete(previous_rectangle)
                base = randint(0, 850)
                rectangle = play_area.create_rectangle(base, base + 50, base + 100, base + 150, fill='red',
                                                       outline='red')
                play_area.tag_bind(rectangle, '<Button-1>', increase_score_command)
                previous_rectangle = rectangle
                sleep(1)
            while True:
                play_area.delete(previous_rectangle)
                base = randint(0, 850)
                rectangle = play_area.create_rectangle(base, base + 50, base + 100, base + 150, fill='red',
                                                       outline='red')
                play_area.tag_bind(rectangle, '<Button-1>', increase_score_command)
                previous_rectangle = rectangle
                sleep(0.5)
        except RuntimeError:
            pass

    Thread(target=create_rectangle_in_random_spot).start()
    root.mainloop()

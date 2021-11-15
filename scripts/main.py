import gui


score = 0
def increase_score(evt):
    global score
    score += 1
    gui.set_score(score)

gui.set_increase_score_command(increase_score)
gui.main()

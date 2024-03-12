import turtle as t
from random import random

for i in range(10):
    steps = int(random()*100)
    angle = int(random()*360)
    t.right(angle)
    t.fd(steps)

t.mainloop()

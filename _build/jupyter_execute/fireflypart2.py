#!/usr/bin/env python
# coding: utf-8

# # Fireflies part 2

# # what to do?

# - We want to create virtual fireflies using multiple micro:bits (each micro:bit acts as a firefly)

# # Code the firefly

# In[1]:


# Add your Python code here. E.g.
from microbit import *
import radio


# the clock ticker
clock = 0
radio.on()
radio.config(power=1,group=12)

# Create the "flash" animation frames.
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

while True:
    incoming = radio.receive()
    if incoming == 'flash':
        # If a nearby firefly just flashed, increment this firefly's clock to nudge it closer to flashing also
        clock += 1

    if clock >= 8:
        radio.send("flash")
        #flash
        #display.show(flash, delay=100, wait=False)
        display.show(flash, delay=100, wait=False)
        sleep(200)
        clock = 0
    else:
        sleep(100)
        clock += 1


# In[ ]:


# Video


# In[2]:


from IPython.display import YouTubeVideo

YouTubeVideo('ZGvtnE1Wy6U', width=800, height=300)


# # Image

# ![alternative text]![](firefly.jpg)

# # python editor

# In[1]:


from IPython import display
display.HTML('<iframe src="https://jackbonk.github.io/editor/" allow="usb;serial"  width=800 height=500></iframe>')


# # link

# [firefliespart2](https://makecode.microbit.org/projects/fireflies)

# In[ ]:





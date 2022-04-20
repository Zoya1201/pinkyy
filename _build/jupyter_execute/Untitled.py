#!/usr/bin/env python
# coding: utf-8

# # Fireflies part 2

# # what to do?

# - We want to create virtual fireflies using multiple micro:bits (each micro:bit acts as a firefly)

# # Code the firefly

# In[1]:


# the clock ticker
clock = 0

def on_received_number(receivedNumber):
    global clock
    # advance clock to catch up neighbors
    clock += 1
radio.on_received_number(on_received_number)

def on_forever():
    global clock
    # if clock hits noon, flash the screen
    if clock >= 8:
        # notify neighbors
        radio.send_number(0)
        # flash
        game.add_score(1)
        # wait for 2 ticks
        basic.pause(200)
        # reset the clock
        clock = 0
    else:
        # just wait a bit
        basic.pause(100)
        # increment the clock
        clock += 1
basic.forever(on_forever)

radio.set_transmit_power(1)
radio.set_group(12)


# # Video

# In[2]:


from IPython.display import YouTubeVideo

YouTubeVideo('ZGvtnE1Wy6U', width=800, height=300)


# # Image

# ![alternative text]![](firefly.jpg)

# # python editor

# In[5]:


from IPython import display
display.HTML('<iframe src="https://python.microbit.org/" allow="usb;serial"  width=800 height=500></iframe>')


# In[ ]:





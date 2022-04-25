#!/usr/bin/env python
# coding: utf-8

# # Fireflies

# # Step1: make it

# - The program uses radio communication to send a message 'flash' when you press button A on one of the micro:bits.
# 
# - When each micro:bit receives the message, it waits a random amount of time between 50 and 350 milliseconds. It then makes the LED display flash bright then gradually dim to mimic the glow of a firefly.
# 
# - Next it generates a random number between 0 and 9. If the number is 0, it then sends its own 'flash' radio message, triggering more micro:bit fireflies to glow. So it has a one in ten chance of triggering more glows in other micro:bits.

# ```{note} 
# this is step 1,you can make it by this step
# ```

# # Step 2: code

# ``` {toggle} click to view code
# :show:
# 
#     # A micro:bit Firefly.
#     # By Nicholas H.Tollervey. Released to the public domain.
#     import radio
#     import random
#     from microbit import display, Image, button_a, sleep
# 
#     # Create the "flash" animation frames. Can you work out how it's done?
#     flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
# 
#     # The radio won't work unless it's switched on.
#     radio.on()
# 
#     # Event loop.
#     while True:
#         # Button A sends a "flash" message.
#         if button_a.was_pressed():
#             radio.send('flash')  # a-ha
#         # Read any incoming messages.
#         incoming = radio.receive()
#         if incoming == 'flash':
#             # If there's an incoming "flash" message display
#             # the firefly flash animation after a random short
#             # pause.
#             sleep(random.randint(50, 350))
#             display.show(flash, delay=100, wait=False)
#             # Randomly re-broadcast the flash message after a
#             # slight delay.
#             if random.randint(0, 9) == 0:
#                 sleep(500)
#                 radio.send('flash')  # a-ha
#  ```     

# In[1]:


from IPython import display
import warnings
warnings.filterwarnings('ignore')
display.HTML('<iframe src="https://jackbonk.github.io/editor/" allow="usb;serial"  width=800 height=500></iframe>')


# # Image

# ![display image](fireflies.gif)

# # Video

# In[2]:


from IPython.display import YouTubeVideo

YouTubeVideo('XzZeB4yYnEw', width=800, height=300)


# In[ ]:





# In[1]:





# In[5]:





# # Step 3: Improve it

# - Change the image that's displayed when the display flashes
# - Experiment with changing the power of the radio signal.
#   Use the 'radio set transmit power' block in MakeCode.
#   In Python use radio.config(power=7)
#   Pick a number between 0 (weakest radio signal) and 7 (strongest).
#   What effect does changing the radio power have?

# ```{note} 
# this is step 3, you can improve it by this step
# ```

# # Link

# In[ ]:





# 

# ```{note} 
# [firefliespart1](https://microbit.org/projects/make-it-code-it/fireflies/?editor=makecode) this is the link for your references
# ```

# In[ ]:





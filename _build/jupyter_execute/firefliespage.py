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

# # Step2: Image

# ![display image](fireflies.gif)

# # Video

# In[1]:


from IPython.display import YouTubeVideo

YouTubeVideo('XzZeB4yYnEw', width=800, height=300)


# In[ ]:





# In[2]:


from IPython import display
import warnings
warnings.filterwarnings('ignore')
display.HTML('<iframe src="https://jackbonk.github.io/editor/" allow="usb;serial"  width=800 height=500></iframe>')


# In[3]:


from ruamel.yaml import YAML

config_document_1 = """
title                       : teaching IoT with microbit  # The title of the book
logo                        : "./microbitFirefly2.png"  # Path to the book logo


"""

# Save our _config.yml in the book path
yaml = YAML()
config_file = open('../ibsp/_config.yml', 'w')
yaml.dump(yaml.load(config_document_1), config_file)


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





# [firefliespart1](https://microbit.org/projects/make-it-code-it/fireflies/?editor=makecode)

# ```{note} 
# this is the link for better understanding of fireflies
# ```

# In[ ]:





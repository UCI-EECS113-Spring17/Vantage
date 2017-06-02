
# coding: utf-8

# # Initialize

# In[18]:

from pynq import Overlay
from pynq.drivers.video import HDMI

# Download bitstream
Overlay("base.bit").download()

# Initialize HDMI
hdmi_in = HDMI('in')
hdmi_out = HDMI('out')


# # Start Stream from HDMI IN to OUT

# In[19]:

hdmi_in = HDMI('in', init_timeout = 10, frame_list=hdmi_out.frame_list)
hdmi_out.mode(4)
hdmi_in.start()
hdmi_out.start()


# # Check State

# In[20]:

stateout = hdmi_out.state()
statein = hdmi_in.state()
width = hdmi_in.frame_width()
height = hdmi_in.frame_height()

print('Input resolution: ')
print('{}x{}'      .format(width,height))
print('Input state: ')
print(statein)
print('')
print('Outout resolution: ')
print(hdmi_out.mode())
print('Output state: ')
print(stateout)


# # Stop Everything

# In[21]:

hdmi_out.stop()
hdmi_in.stop()
del hdmi_out
del hdmi_in


# In[ ]:




from genie import testbed
from genie.conf.base import Testbed, Device, Interface, Link

# Look at the bottom for an example of a testbed file
testbed = testbed.load('tbed2.yml')

#Load Testbed
device = testbed.devices['R2']

# Connect to ios device R2
device.connect()

#Create an Interface Object for Loopback100 assigned to device R2

R2_interface = Interface(device=device, name='Loopback100')
# Add some configuration
R2_interface.ipv4 = '200.1.1.2'
R2_interface.ipv4.netmask ='255.255.255.0'
R2_interface.shutdown = False
# Verify configuration generated
print(R2_interface.build_config(apply=False))
R2_interface.build_config() # To apply on the device
R2_interface.build_unconfig() # To remove configuration

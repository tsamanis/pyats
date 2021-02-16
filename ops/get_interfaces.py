import pprint
# Import Genie
from genie import testbed
from genie.libs.ops.interface.nxos.interface import Interface

# Look at the bottom for an example of a testbed file
testbed = testbed.load('tbed2.yml')

# Find the device I want to connect to
device = testbed.devices['R2']

# Connect to it
device.connect()

# Instantiate the OPS object
interface = Interface(device=device)

# This will send many show command to learn the operational state
# of interfaces for this device
interface.learn()

cr="\n"
for inf in interface.info:
 if interface.info[inf]["oper_status"]=="up":
    pprint.pprint(f"Interface {inf} Counters: {interface.info[inf]} ")

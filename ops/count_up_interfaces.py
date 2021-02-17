import pprint
# Import Genie
from genie import testbed
from genie.libs.ops.interface.ios.interface import Interface
from genie.utils import Dq

# Look at the bottom for an example of a testbed file
testbed = testbed.load('tbed2.yml')

# Find the device I want to connect to
device = testbed.devices['R1']

# Connect to it
device.connect()

# Parse output
output = device.parse("show interfaces")

#Count interfce in up state
active_interfaces=output.q.contains_key_value('enabled',True).count()
print(f"Number of active interfaces {active_interfaces}")



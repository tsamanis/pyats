import pprint
# Import Genie
from genie import testbed

# Look at the bottom for an example of a testbed file
testbed = testbed.load('tbed2.yml')

# Find the device I want to connect to
device = testbed.devices['R2']

# Connect to it
device.connect()

# Parse device output
output = device.parse('show version')

# Print it nicely
pprint.pprint(output["version"]["os"])
pprint.pprint(output["version"]["version"])
pprint.pprint(output["version"]["main_mem"])

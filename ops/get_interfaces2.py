import pprint
# Import Genie
from genie import testbed
from genie.libs.ops.interface.ios.interface import Interface
from genie.utils import Dq

# Look at the bottom for an example of a testbed file
testbed = testbed.load('tbed2.yml')

# Find the device I want to connect to
device = testbed.devices['R2']

# Connect to it
device.connect()

# Instantiate the OPS object
output = device.parse("show interfaces")
for inf in output:
 inter=output[inf]
 val=Dq(output).contains('in_errors').get_values('in_errors')
 if val!=0:
   print(f"Interface {inter} input Errors: {val}")
#print(Dq(output).contains('in_errors'))


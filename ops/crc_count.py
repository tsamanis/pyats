from genie import testbed
from genie.utils import Dq

# load testbed file
testbed = testbed.load('tbed2.yml')

# connect to all devices in the testbed file
for i in testbed.devices:
 device = testbed.devices[i]
 device.connect(log_stdout=False)
# Parse "show interfaces" command 
 output = device.parse("show interfaces")
# find interfaces with non-zero input errors
 in_errors=output.q.value_operator('in_errors','>',0).reconstruct()
 print("Device:", device.hostname)
# Print input errors if in_errors>0 for each interface
 for i in in_errors:
  print("Interface ",i," Input Errors: ", in_errors[i]["counters"]["in_errors"])




# The OS choices are - nxos; iosxr; iosxe; ios - For this example, we will be
# using ios
from genie import testbed
from genie.libs.ops.interface.ios.interface import Interface

# Load Genie testbed
testbed = testbed.load('tbed2.yml')
uut = testbed.devices['R2']
uut.connect()

# Learn all interface which has duplex mode as a key
interface = Interface(device=uut, attributes=['info[(.*)][duplex_mode]'])

interface.learn()

import pprint
pprint.pprint(interface.info)

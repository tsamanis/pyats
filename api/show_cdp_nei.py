'''
All available device APIs 
https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis

Genie has a set of built in API functions that can be used to perform 
various actions including config, verify, get, analyze, and more on the 
device. They can be accessed directly with the device.apis method. To use 
them, simply find the API name you need, then call the API with it’s 
argument as: device.api.api_name(args_1, args_2, ....)

'''
import pprint
# Import Genie
from genie import testbed

# Look at the bottom for an example of a testbed file
testbed = testbed.load('tbed2.yml')

# Find the device I want to connect to
device = testbed.devices['R2']

# Connect to it
device.connect()
# get cdp neighbors in a dictionary for further parsing 
cdp=device.api.get_cdp_neighbors_info()

device_id=cdp["index"][1]["device_id"]
local_if=cdp["index"][1]["local_interface"]
remote_if=cdp["index"][1]["port_id"]

print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f" Device id: {device_id} Local If: {local_if} Remote if: {remote_if}")
 

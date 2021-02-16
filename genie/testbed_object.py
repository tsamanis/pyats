# Import Genie
from genie import testbed
from genie.conf.base import Testbed, Device, Interface, Link
from pyats.datastructures.logic import And, Not, Or

# Look at the bottom for an example of a testbed file
testbed = testbed.load('tbed2.yml')

for dev in testbed.devices:
 device = testbed.devices[dev]
 device.connect()
 output = device.parse('show version')

'''
https://pubhub.devnetcloud.com/media/genie-docs/docs/userguide/Conf/user/topology.html?highlight=testbed%20yaml%20file
+--------------------------------------------------------------------------+
| Testbed object                                                           |
+==========================================================================+
| Attributes            | Description                                      |
|-----------------------+--------------------------------------------------|
| name                  | Testbed name, should be unique                   |
| devices               | Dict of testbed devices                          |
| interfaces            | Tuple of all interfaces in this testbed          |
| links                 | Set of testbed links                             |
| features              | List of all the features in this testbed         |
| ipv4_cache            | Available ipv4 address                           |
| ipv6_cache            | Available ipv6 address                           |
| mac_cache             | Available mac address                            |
+==========================================================================+
| Methods               | Description                                      |
|-----------------------+--------------------------------------------------|
| add_device            | Adds a device (Device object) to this testbed.   |
| remove_device         | Removes a device (Device object) from this       |
|                       | testbed.                                         |
| find_devices          | Returns device objects of this testbed with      |
|                       | specific requirements.                           |
| find_links            | Return links objects of this testbed with        |
|                       | specific requirements.                           |
| find_interface        | Returns interface objects of this testbed with   |
|                       | requirements. It appends all the interfaces into |
|                       | the same list.                                   |
| find_features         | Returns features objects of this testbed with    |
|                       | specific requirements. It appends all the        |
|                       | features into the same list.                     |
| build_config          | Builds and configures the whole testbed. Loops   |
|                       | through each device, features, and link to       |
|                       | configure it.                                    |
| build_unconfig        | Builds and unconfigures the whole testbed.       |
|                       | Loops through each device, features and list to  |
|                       | configure it.                                    |
| object_instances      | Returns a frozenset of all the instances of a    |
|                       | particular type.                                                        | set_active_objects    | Froms a list of interfaces, set attributes       |
|                       | `obj_state` of all devices, interfaces and       |
|                       | and link as `active` and `inactive`.             |
| squeeze               | Removes all unwanted devices, interfaces         |
|                       | and links from this testbed.                     |
+==========================================================================+

'''


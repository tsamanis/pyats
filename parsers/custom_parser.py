'''
Parsing tabular data for the ios command show interface summary
ref: https://pubhub.devnetcloud.com/media/genie-docs/docs/parsergen/tabular/tabular.html
ref: https://pubhub.devnetcloud.com/media/genie-docs/docs/parsergen/apidoc/parsergen.html
ref: https://pubhub.devnetcloud.com/media/genie-docs/docs/parsergen/apidoc/parsergen.html#genie.parsergen._parsergen.oper_fill_tabular
classgenie.parsergen._parsergen.oper_fill_tabular(device=None, show_command=None, refresh_cache=True, header_fields=None, table_terminal_pattern=None, index=0, skip_header=None, table_title_pattern=None, right_justified=False, label_fields=None, is_run_command=False, skip_line=None, device_conn_alias=None, device_output=None, device_os=None, delimiter='')

'''

#import testbed & parsegen
from genie import testbed
from genie import parsergen
import pprint

#load testbed file
testbed = testbed.load('tbed2.yml')
#choose IOS device and connect
device = testbed.devices['R2']
device.connect()

#Execute show interface summary command
output = device.execute('show interface summary')

# Parse tabular data
result = parsergen.oper_fill_tabular(header_fields=["Interface", "IHQ", "IQD", "OHQ", "OQD", "RXBS", "RXPS", "TXBS", "TXPS", "TRTL"], label_fields=["INTERFACE", "IHQ", "IQD", "OHQ", "OQD", "RXBS", "RXPS", "TXBS", "TXPS", "TRTL"], index=[0], delimiter="*",device_output=output, device_os='ios')

#Print the result
pprint.pprint(result.entries)

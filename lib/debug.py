
#!/usr/bin/env python3
# lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Call the correct method name and pass no arguments
Department.create_table()
Department.create_table()

management =Department("Management","Kisumu")
agriculture =Department.create("Agriculture,Nandi")
hr = Department.creareate("HR","Nairobi")

ipdb.set_trace()

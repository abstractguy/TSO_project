# File: generate_BOM.py
# By:   Samuel Duclos
# For:  TSO_project

import pandas as pd

#BOM = pd.read_excel('/home/samuel/school/Project/ESP-EYE_V2.1_Reference_Design/04_BOM List/ESP-EYE_V2.1_BOM_list.xlsx', 
#                    header=1, index_col=0)

BOM = pd.DataFrame(data=[['ESP32', 2, 'ESP32-D0WD', 'https://www.digikey.ca/en/products/detail/espressif-systems/ESP32-D0WD/8028403?s=N4IgTCBcDaIIwE4AMAWAtHJSDMG0DkAREAXQF8g'], 
                         ['', '', ''], 
                         ['', '', '']], 
                   columns=['part_name', 
                            'quantity', 
                            'part_number', 
                            'hyperlink'])

BOM.to_excel('./BOM.xls')

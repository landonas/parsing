import pandas as pd
excel_file= 'vulns.xls'
vulns = pd.read_excel(excel_file)

vulns.head()
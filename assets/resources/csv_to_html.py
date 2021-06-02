# First table had an extra index column not needed
# Adding index=False so that it is not included in the table

import pandas as pd
pd.read_csv('cities.csv').to_html('../../visualizations/table.html', index=False)
import pandas as pd
from io import StringIO

csv = """
name;age
Maria;93
John;24
Peter;19
Cassandra;46
"""

file = StringIO(csv)

df = pd.read_csv(file)
df.to_parquet('data.parquet')
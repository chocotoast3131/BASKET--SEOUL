from Detailed_price import Detailed_graph, df_drop
import pandas as pd

df_graph = df_drop[df_drop.marketname == '경동']
print(df_graph)
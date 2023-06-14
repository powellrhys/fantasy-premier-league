import plotly.express as px
from functions.support_functions import read_csv

player_data_df = read_csv('data/fixtures.csv')

print(player_data_df)

player_data_df.pivot(index='Team', columns='GW', values='Diff')
print(player_data_df)

df = px.data.medals_wide(indexed=True)
print(df.head())
# fig = px.imshow(df)
# fig.show()
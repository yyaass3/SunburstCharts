import plotly.express as px
import pandas as pd
# 1
df1 = px.data.iris()
fig1 = px.sunburst(df1, path=['sepal_length', 'sepal_width', 'petal_length'], values='petal_width')
fig1.show()

# 2
df2 = px.data.tips()
fig2 = px.sunburst(df2, path=['day', 'sex'], values='total_bill', color='total_bill')
fig2.show()

# 3
A = ['A', 'B', 'C', 'D', None, 'E', 'F', 'G', 'H', None]
B = ['A1', 'A1', 'B1', 'B1', 'N', 'A1', 'A1', 'B1', 'B1', 'N']
C = ['N', 'N', 'N', 'N', 'N', 'S', 'S', 'S', 'S', 'S']
D = [1, 13, 21, 14, 1, 12, 25, 1, 14, 1]
df3 = pd.DataFrame(dict(A=A, B=B, C=C, D=D))
fig3 = px.sunburst(df3, path=['C', 'B', 'A'], values='D')
fig3.show()

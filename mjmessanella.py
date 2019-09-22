import pandas as pd
import matplotlib.pyplot as plt

## The plots from the dataset share the same x-axis but have completely different y-axis. I therefore
## used two y-axis on both sides of the plot, color-coded them and indexed boths y-axis starting from 0 to
## give a better picture of their supposed correlation.

data = pd.read_csv("istherecorrelation.csv")
x = data["Year"]
y1 = data["WO [x1000]"]
y2 = data["NL Beer consumption [x1000 hectoliter]"]

fig, axis_1 = plt.subplots()

color = 'tab:red'
axis_1.set_xlabel('Year')
axis_1.set_ylabel('Number of WO students x1000', color=color)
axis_1.plot(x, y1, color=color)
axis_1.tick_params(axis='y', labelcolor=color)
plt.axis([None, None, 0, 300])

axis_2 = axis_1.twinx()

color = 'tab:blue'
axis_2.set_ylabel('NL beer consumption x1000 hectoliter', color=color)
axis_2.plot(x, y2, color=color)
axis_2.tick_params(axis='y2', labelcolor=color)
plt.axis([None, None, 0, 14000])

plt.title('Beer consumption and number of WO students between 2006 and 2018')
fig.tight_layout()
plt.show()


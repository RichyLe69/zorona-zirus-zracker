# zorona zirus zracker
![Alpha status](https://img.shields.io/badge/Project%20status-Alpha-red.svg)

 Corona virus Statistics Tracker
 
Uses python and pyecharts for data visualization

Getting Started:

Install Pyechart, a python visualization package. I am using version 1.7.1 which was released on March 12th 2020.

```
pip install pyecharts==1.7.1
pip install pandas
```

Step 1: import libraries

#import libraries
```
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
```

Step 2: Get covid-19 Data. I'm using Our World in Data's covid-19 dataset in json format. - https://ourworldindata.org/coronavirus

# import data
```
dataset = pd.read_json('owid-covid-data.json')
```

# Important lines
```
map_1.render()  # render the map in a local html file.
```

# Example of Render
![Alt Text](https://raw.githubusercontent.com/richardle17/zorona-zirus-zracker/master/zorona%20zirus%20demo.gif)
Map is interactable and specific countries can be hovered over for specific case data. 

Population legend of left side can be toggled to highlight countries of specified total case count.


# Todo
- [ ] utilize json data instead of csv
- [ ] Have a way to select date of data
- [ ] Other stuff to be added

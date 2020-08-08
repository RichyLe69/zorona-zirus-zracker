# zorona zirus zracker
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


# Todo
- [ ] utilize json data instead of csv
- [ ] Have a way to select date of data
- [ ] Other stuff to be added
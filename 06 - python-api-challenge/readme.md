## Python API Homework - What's the Weather Like?

#### *Table of Contents*:
1. Folder Structure
2. WeatherPy Observations
3. Noteworthy


#### 1. *Folder Structure*:
1. **Output**: All png and csv output files can be found here.  
- WeatherPy scatter and linear regression charts all outputted individually as png files here.  
- Multiple csv files of the retrieved data at various points in time outputted here as well. 
- Heatmap png stored here as well titled: my_ideal_vacation_heatmap.png
2. **WeatherPy**: WeatherPy.ipynb and config file stored here.
3. **VacationPy**: VacationPy.ipynb and config file stored here.

#### 2. *WeatherPy Observations*
1. **Observation #1**: There is a visible correlation between Temperature and Latitude further supported with a moderate linear regression r-value.  Temperature increases as we approach the equater and decreaes as we move away from the equator to the North Pole and South Pole.
2. **Observation #2**: There is a visible correlation between Humidity and Latitude within a very small latitude band between -10 and 10 which makes sense since high humidity is a result of the presence of high temperature and moisture from nearby large bodies of water (ie the ocean). 
3. **Observation #3**:  There is no visible correlation between latitude with either wind speed or cloudiness.  A third variable may need to be considered to determine correlation such as longitude.

#### 3. *Noteworthy*
- I was unable to retrieve my API keys consistently when my config file resided anywhere outside of the folders the respective jupyter notebooks were.  Hence you will see the presence of the config file in both the WeatherPy and VacationPy folders.
- There exists some miscellaneous checkpoint and cache file folders in both WeatherPy and VacationPy folders.  Please ignore, next time I will implement GIT ignore so the files don't get pushed to this main repository.
- Did not have opportunity to consider the full range of latitudes when I was retrieving the city data from the API to minimize bias in my dataset.  Assuming I would define some lat and lon ranges and ensure I get equal city records in each section when I run my for loop. Also was unable to date stamp the outputted files and the chart title (dynamically?). Next time...



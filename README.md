# Surfs_up
Surf Shop feasibility study using SQLite, SQLalchemy, Flask, and jupyter notebook.

## Overview
A client has asked us to analyze several years of temperature data for the months of June and December to determine if the weather in Oahu is ideal for a surf and shake shop. The client is worried that too much fluctuation in the temperatures could lead to several months of low customer numbers.

## Results

### June temperatures
The analysis looks at weather station data from 2010 to 2018. We obtained 1700 temperature readings from various weather stations for the month of June in this 8 year period. The mean temperature was just shy of 75 degrees Fahrenheit. The minimum was 64 and the maximum 85. The temperature range is pretty tight during this month staying mainly between 73 and 77 degrees.

![june_stats.png](https://github.com/Brooks2210/surfs_up/blob/main/June_temps.png)

### December temperatures

During the same period described above, there were 1517 observations for the month of December. The mean temperature for this month was 71.04 degrees with a minimum of 56 degrees and a maximum of 83. Most days in this month fall between 69 and 74 degrees.

![dec_stats.png](https://github.com/Brooks2210/surfs_up/blob/main/Dec_temps.png)

### Takeaway
1. The average temperature and standard deviation between the temperatures in June and December are remarkably close together. June is slightly warmer by about three degrees Fahrenheit. 
2. One interesting finding was that while the high temperatures in June and December are only different by a few degrees, the low temperatures are nearly 10 degrees apart. 
3. The preliminary data suggest that the weather is ideal in both June and December for a surf and shake shop.

## Conclusion

While the analysis looked at temperatures for both June and December, further analysis needs to be done in regard to other factors. One potential factor not analyzed was precipitation. How many rainy days does Oahu have? Another factor that should be examined is wind speed. Extremely windy days can have just as much of a negative impact as rainy days. Is there a storm season in Oahu that was not captured in just analyzing two months of data? All these factors should be examined before the surf shop is green lighted. 


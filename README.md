# Motivate Bikeshare Analysis
Python was used to understand and analyze U.S. bikeshare data from Motivate. Statistics were calculated and an interactive environment was built in which a user chooses the data and filters a dataset to analyze.

## Bikeshare Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, data was provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. The system usage between three large cities will be compared: Chicago, New York City, and Washington DC.

## The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57) 
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave) 
* End Station (e.g., Sedgwick St & North Ave) 
* User Type (Subscriber or Customer) 

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

## **Statistics Computed**
A variety of descriptive statistics will be computed for New York, Washington, and Chicago. In this project, I wrote code to provide the following information:

#### 1. Popular Times of Travel (i.e., occurs most often in the start time)

* Most common month 
* Most common day of week 
* Most common hour of day

#### 2. Popular Stations and Trip

* Most common start station 
* Most common end station
* Most common trip from start to end (i.e., most frequent combination of start station and end station)

#### 3. Trip Duration

* Total travel time 
* Average travel time

#### 4. User Information

* Counts of each user type
* Counts of each gender (only available for NYC and Chicago)
* Earliest, most recent, most common year of birth (only available for NYC and Chicago)


## The Files
A template along with three city dataset files were provided:

* chicago.csv
* new_york_city.csv
* washington.csv

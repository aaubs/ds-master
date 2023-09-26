# About Dataset

## Introduction

Data for this study was extracted using the Octoparse scraping tool from the "Ease My Trip" website. The dataset was collected in two parts, focusing on economy class tickets and business class tickets respectively. A total of 300261 distinct flight booking options were extracted. The data collection spanned 50 days, from February 11th to March 31st, 2022. The dataset comprises secondary data obtained exclusively from the "Ease My Trip" website.

## Dataset Overview

The dataset encompasses information about flight booking options available on the "Easemytrip" website, covering flight travels between India's top 6 metro cities. The cleaned dataset consists of 300261 datapoints and 11 features.

## Features

The cleaned dataset is characterized by the following features:

1) **Airline**: This categorical feature stores the name of the airline company, encompassing 6 different airlines.
2) **Flight**: Stores the plane's flight code information and is a categorical feature.
3) **Source City**: Represents the city from which the flight departs. This categorical feature comprises 6 unique cities.
4) **Departure Time**: A derived categorical feature created by binning time periods, which holds information about the departure time and has 6 unique time labels.
5) **Stops**: A categorical feature indicating the number of stops between the source and destination cities, with 3 distinct values.
6) **Arrival Time**: This is another derived categorical feature, created by grouping time intervals into bins. It encompasses six distinct time labels and holds information about the arrival time.
7) **Destination City**: Represents the city where the flight will land. This is a categorical feature with 6 unique cities.
8) **Class**: Contains information on seat class and is a categorical feature with two distinct values: Business and Economy.
9) **Duration**: A continuous feature representing the total travel time between cities in hours.
10) **Days Left**: A derived feature calculated as the difference between the trip date and the booking date.
11) **Price**: This feature is the target variable and stores information on the ticket price.



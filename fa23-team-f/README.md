# Boston Bus Performance Team F

## Project Description

The Massachusetts Bay Transportation Authority (MBTA) is not just a transit system, but a crucial lifeline for over a million daily commuters in the Boston area, significantly contributing to the region's economy with an estimated annual value of $11.5 billion. Yet, the quality of bus service and its performance varies across different neighborhoods, raising concerns about equitable access to transportation. This disparity has implications for economic opportunities, environmental sustainability, and social equity. To address this, there is a need for a comprehensive, data-driven analysis of MBTA's bus service performance trends, with a focus on geographic and demographic disparities. This project, in collaboration with BU Spark!, aims to uncover these trends, highlight potential inequities, and inform decision-making to enhance transit accessibility for all Boston residents. 

In general, we collected data from various sources including MBTA open data portal, Boston Analyze website, National Weather Service, etc. to help construct a multi-view analysis. Besides doing data analysis using multiple data science tools, we decided to move forward and incorporate the usage of Machine Learning model from the lecture to create a prediction system for potentially benefiting the passengers of MBTA bus. 

The project's big picture revolves around leveraging technology and data science to improve public transportation, ultimately striving to make Boston a more connected and equitable city. By analyzing and addressing the disparities in MBTA bus service, this initiative not only enhances daily commuting experiences but also contributes to broader goals of social justice, economic growth, and environmental sustainability in the region.



## Summary of Our Work

### Base questions:

We mainly collected data from the MBTA Open Data Portal and Analyze Boston website. The datasets that we processed are Boston Neighborhoods Boundaries data from 2020, Bus Network Redesign Draft Bus Routes, Rapid Transit and Bus Prediction Accuracy, Commuter Rail Reliability, MBTA Bus Arrival Departure time, and Bus Ridership. For certain questions, we analyzed certain dataset solely. And for certain questions such as the third one, we used combinations of several datasets in order to present a specific result.

### Extension analysis:

We propose to extend our current geospatial analysis of Boston's transit systems by integrating additional datasets that consider factors like service disruptions and accessibility features. This effort aims to provide a more inclusive story of the city's transit dynamics, particularly focusing on the distribution and development of resources for disabled accessibility around bus stops. We also propose to delve deeper into the intersection of public transit data, specifically focusing on Blue Bike and bus data in Boston. The goal is to uncover insights into how different modes of transit interplay and affect urban mobility. In addition to analysis, we decided to move further by doing a practical move, which is a delay prediction system based on route ID and temperature inputs. With the use of this system, the passengers could gain real benefits.

The reason for doing this extension to the base project is that we aim to extend the geospatial analysis of Boston's transit systems, integrating data on service disruptions and accessibility, especially focusing on disabled access at bus stops. This approach seeks to provide a comprehensive view of the city's transit dynamics and improve urban mobility by analyzing how different modes, like Blue Bikes and buses, interact. Additionally, we plan to develop a practical delay prediction system based on route ID and temperature, offering direct benefits to passengers by enhancing their commuting experience



## How to Navigate Through the Folders

* data
  *  base
          Boston_Neighborhood_Boundaries_Approximated_by_2020_Census_Tracts
          Bus_Network_Redesign_Draft_Bus_Routes
          bus_routes_race_data.csv
          MBTA_bus_reliability_2023.csv   
  * extension
          Updated_Blue_Bike_Stations_with_Stops.geojson
          current_bluebikes_stations.csv
          Community_Centers.csv
          Hospitals.csv
          boston_income_by_zipcode.csv
          stops.csv
* deliverables
  * deliverables 1+2
  * extension



## Running Instructions

### Base questions: 

While running the notebooks for the base questios, go to the `notebooks` folder under the directory `deliverable 1+2`. The original data we used for base question is under the `data` folder. When reporducing our results, please change the file path in the code accordingly.

* `eda1.ipynb`: our data analysis for base questions 1-5
* `service_reliability.ipynb`: our visualization of the bus stops and service reliability for each neighborhood on a map.
* `visualization_race.ipynb`: Visualization of the racial distribution along the bus routes.

### Extension questions:

To reproduce our results for the extension questions, please nagivage to the `notebooks` folder under the extension directory. The original data for our extension project is stored under `data/extension`. We also stored some of the intermediate results under this folder for reference and quicker reproduction of our results. While running the notebooks, change the file path in the code accordingly.

* `bluebikes_user_pattern.ipynb `: Usage analysis on BlueBikes riders
* `visualize_bus_with_bikes.ipynb`: Visualization of bus stops and BlueBikes stations.
* `disable_access.ipynb`: Diability facility coverage analysis on all bus stops
* `income_eda.ipynb`: Elementary analysis on income level of neighborhood
* `income_analysis.ipynb`: Visualization of correlation between neighborhood income and service reliability
* `delay_predictions.ipynb`: Our delay prediction system for bus route under certain weather condition
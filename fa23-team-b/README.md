## What Our Project Is:
- Base Project<br>
This project aims to perform a detailed, data-driven analysis of the Massachusetts Bay Transportation Authority (MBTA) bus system's performance in 2022. The main focus is to explore service quality trends across different geographical areas and demographic groups in Boston. The study will identify any disparities in bus service quality among neighborhoods and provide insights that are valuable for policymakers, city planners, and the MBTA. Our insights will shed light on potential disparities among neighborhoods, providing a basis for informed decision-making. By examining the geographical distribution of bus performance, the analysis will offer valuable information to policymakers, city planners, and the MBTA itself, facilitating the identification of opportunities for targeted improvements.<br>
- Extension Project: <br>
Accessibility of Boston Bus Transit System

## What We Did:

For the base project, we began by collecting arrival & departure times over the entire year of 2022 from the MBTA Historical Data Archive as well as copies of the routes’ schedules. We also pulled data on the stations in the network via calls to the V3 API - their locations, routes served, accessibility information, etc. After cleaning the data, we successfully discovered an overall passenger demographic, disparities in service levels of different routes, etc. Those results intrigued us to discover more about the accessibility of the Boston Bus Transit System, which is our extension project.<br>
For the extension project, we investigated the relationship between accessibility and the number of disabled individuals by generating a heatmap, utilizing Census Data available on the government website. Additionally, we employed MarkerCluster in Folium, combined with Boston's neighborhood GeoJSON data, to generate an interactive map that displays the number of bus stops. For each bus stop, we included labels indicating its accessibility score, which correlates with factors such as sidewalk width, condition, material, and the presence of a shelter. The labels also show whether the stop is wheelchair accessible and the bus routes that serve each stop.

## How to navigate the different files in the repo
- scrum_report: weekly reports
- Deliverable_3: contain files needed for heatmap, json generation, and interactive map.
- ...

## Information any future users would need to have to get the code running
- In order to get the code running, these dataset below are needed.

- Deliverable 1 <br>
    end-to-end time from Jan to Dec in 2022<br>
    https://mbta-massdot.opendata.arcgis.com/datasets/mbta-bus-arrival-departure-times-2022/about
    
- Deliverable 2 <br>
    end-to-end time from Jan to Dec in 2022<br>
    https://mbta-massdot.opendata.arcgis.com/datasets/mbta-bus-arrival-departure-times-2022/about
    Census Data<br>
    https://data.boston.gov/dataset/2020-census-for-boston/resource/5800a0a2-6acd-41a3-9fe0-1bf7b038750d?inner_span=True
    MBTA_Systemwide_GTFS_Map.csv<br>
    https://drive.google.com/drive/folders/1EA87Ptx1WPhAnJDURf6XGj01BXKjwMsN
    redistricting_data_tract20_nbhd_hhpopsize_ab-1.csv<br>
    https://drive.google.com/drive/folders/19DA3f1Cq6ErofPZnMFoQEuBqInwizivP

- Deliverable 3
    MBTA_Systemwide_GTFS_Map.csv<br>
    https://drive.google.com/drive/folders/1EA87Ptx1WPhAnJDURf6XGj01BXKjwMsN
    redistricting_data_tract20_nbhd_hhpopsize_ab-1.csv<br>
    https://drive.google.com/drive/folders/19DA3f1Cq6ErofPZnMFoQEuBqInwizivP
    https://youtu.be/7HQHEy1p99c
    

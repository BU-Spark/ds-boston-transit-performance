What Our Project Is:
- Base Project
This project aims to perform a detailed, data-driven analysis of the Massachusetts Bay Transportation Authority (MBTA) bus system's performance in 2022. The main focus is to explore service quality trends across different geographical areas and demographic groups in Boston. The study will identify any disparities in bus service quality among neighborhoods and provide insights that are valuable for policymakers, city planners, and the MBTA. Our insights will shed light on potential disparities among neighborhoods, providing a basis for informed decision-making. By examining the geographical distribution of bus performance, the analysis will offer valuable information to policymakers, city planners, and the MBTA itself, facilitating the identification of opportunities for targeted improvements.
- Extension Project: Accessibility of Boston Bus Transit System

What We Did:
For the base project, we began by collecting arrival & departure times over the entire year of 2022 from the MBTA Historical Data Archive as well as copies of the routes’ schedules. We also pulled data on the stations in the network via calls to the V3 API - their locations, routes served, accessibility information, etc. After cleaning the data, we successfully discovered an overall passenger demographic, disparities in service levels of different routes, etc. Those results intrigued us to discover more about the accessibility of the Boston Bus Transit System, which is our extension project.
For the extension project, we investigated the relationship between accessibility and the number of disabled individuals by generating a heatmap, utilizing Census Data available on the government website. Additionally, we employed MarkerCluster in Folium, combined with Boston's neighborhood GeoJSON data, to generate an interactive map that displays the number of bus stops. For each bus stop, we included labels indicating its accessibility score, which correlates with factors such as sidewalk width, condition, material, and the presence of a shelter. The labels also show whether the stop is wheelchair accessible and the bus routes that serve each stop.

How to navigate the different files in the repo


Information any future users would need to have to get the code running

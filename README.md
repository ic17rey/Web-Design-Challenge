# Web Design Challenge - Latitude Dashboard

A visualization dashboard is created from data and images from a past project where weather conditions at different latitudes were analyzed.  
* The data is stored within the resources folder in assets, in the cities.csv file
* The landing page created (index.html) includes a summary of the project and also displays in a section called Visualizations the plots that were created  

  * The plots displayed in Visualizations include 
    * Max Temperature
    * Humidity
    * Cloudiness
    * Wind Speed
* The landing page also includes navigation across the top to the additional pages involved  
 
  * There is a dropdown where the four plots can be selected plus two additional pages, Comparisons and Data
  * When choosing a plot from the dropdown or by clicking an image on the landing page, details about the plot are displayed
  * For Comparisons, choose from any of the four plots to see more information
  * For Data, cities.csv is read to an html file using pandas (table.html) and the resulting table is displayed
  * For viewing on smaller screens the landing page is still available as a button on the upper left, but other navigation is done through a menu on the top right-hand side
     
### Pages
There are seven total pages - a landing page, a page for each of the four visualizaitons, the comparisons page and the page displaying the data

Each page has navigation at the top to allow the user to return the landing page using the Latitude button at the far left or to choose from options at the top right to route to any other page  

Other than index.html, all html files are found in the visualizations folder



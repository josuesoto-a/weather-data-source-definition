# weather-data-source-definition
## Data Source Description
This data source provides high-resolution global weather forecasts. It includes real-time variables and hourly predictions of temperature, humidity, wind, atmospheric pressure, and different types of precipitation (rain/snow).
## Data Provider
Open-Meteo
## Access Method
REST API
HTTP GET 
## Example  Request
https://api.open-meteo.com/v1/forecast?latitude=9.93&longitude=-84.08&current_weather=true
## Data Fields
-time: Report time.
-temperature: Temperature in °C.
-windspeed: Wind speed.
-winddirection: Wind direction.
-weathercode: Weather condition code.
## Update Frequency
Data is updated every 60 minutes (hourly), based on the latest runs of global meteorological models.
## Data format 
JSON
## Potencial use cases
Smart Agriculture: Automation of irrigation systems based on rainfall probability and soil temperature.
Logistics and Transportation: Optimization of delivery routes to avoid storms or dangerous wind conditions.
Energy Management: Production forecasting for solar farms (using radiation data) or wind farms.
Consumer Applications: Creation of personal dashboards or mobile apps that send real-time weather alerts.

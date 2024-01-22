
import sys
from weather_au import api

loc = '4051'
w = api.WeatherApi(search=loc, debug=0)

location = w.location()

# check if the search produced a result (other methods will also return None if the search fails).
if location is None:
    sys.exit('Search failed for location ' + loc)

print(f"\nLocation: {location['name']} {location['state']}, timezone:{location['timezone']}\n")

for warn in w.warnings():
    print(f"Warning short title:  {warn['short_title']}")

    warning = w.warning(id=warn['id'])
    print(f"Warning title:        {warning['title']}")

observations = w.observations()
print(f"\nObservations (temp): {observations['temp']:2}")

forecast_rain = w.forecast_rain()
print(f"Forecast Rain:      amount:{forecast_rain['amount']}, chance:{forecast_rain['chance']}")

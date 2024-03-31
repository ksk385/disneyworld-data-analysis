import pandas as pd
import json

def get_park_name(park_id, locations):
    for location in locations:
        if location['id'].split(';')[0] == park_id:
            return location['title']
    return None

# Provided JSON data
# Read JSON file
with open('raw-activities-response.json', 'r') as file:
    data = json.load(file)
    activities = data['results']
    locations = data['locations']

    # Initialize lists to store extracted data
    attraction_names = []
    park_names = []
    timings = []
    location_lat = []
    location_lng = []
    height_restrictions = []

    # Extract data from JSON
    for entry in activities:
        attraction_names.append(entry['name'])
        park_id = entry['parkIds'][0].split(';')[0]
        park_names.append(get_park_name(park_id, locations))
        
        # Extracting timings
        schedule = entry.get('schedule', {})
        schedules = schedule.get('schedules', [])
        timings.append(', '.join([f"{schedule['startTime']} to {schedule['endTime']}" for schedule in schedules]))
        
        # Extracting location
        location_lat.append(entry.get('marker', {}).get('lat', None))
        location_lng.append(entry.get('marker', {}).get('lng', None))

        facet = entry.get('facets', {})
        height_restrictions.append(facet.get('height', None))

    # Create DataFrame
    df = pd.DataFrame({
        'Attraction Name': attraction_names,
        'Park Name': park_names,
        'Timings': timings,
        'Height Restrictions': height_restrictions,
        'Location Lat': location_lat,
        'Location Lng': location_lng
    })
    df.to_csv("attractions.csv", index=False)
    print("DataFrame written to attractions.csv")

    # Display DataFrame
    print(df.columns)
    print(df.info())
    print(df['Park Name'].value_counts())  

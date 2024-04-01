import pandas as pd
import json

disney_base_url = 'https://disneyworld.disney.go.com'

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
    activity_names = []
    activity_types = []
    park_ids = []
    park_names = []
    timings = []
    location_lat = []
    location_lng = []
    height_restrictions = []
    urls = []

    # Extract data from JSON
    for entry in activities:
        activity_names.append(entry['name'])
        activity_types.append(entry['entityType'])
        park_id = entry['parkIds'][0].split(';')[0]
        park_ids.append(park_id)
        park_names.append(get_park_name(park_id, locations))
        
        # Extracting timings
        schedule = entry.get('schedule', {})
        schedules = schedule.get('schedules', [])
        timings.append(', '.join([f"{schedule['startTime']} to {schedule['endTime']}" for schedule in schedules]))
        
        # Extracting location
        location_lat.append(entry.get('marker', {}).get('lat', None))
        location_lng.append(entry.get('marker', {}).get('lng', None))

        facet = entry.get('facets', {})
        if 'height' in facet:
            height_restrictions.append(facet.get('height')[0])
        else:
            height_restrictions.append('')

        if 'url' in entry:
            urls.append(disney_base_url + entry['url'])
        else:
            urls.append(None)

    # Create DataFrame
    df = pd.DataFrame({
        'Activity Name': activity_names,
        'Activity Type': activity_types,
        'Park ID': park_ids,
        'Park Name': park_names,
        'Timings': timings,
        'Height Restrictions': height_restrictions,
        'URL': urls,
        'Location Lat': location_lat,
        'Location Lng': location_lng
    })
    df.to_csv("activities.csv", index=False)
    print("DataFrame written to activities.csv")

    # Display DataFrame
    print(df.columns)
    print(df.info())
    print(df['Park Name'].value_counts())  

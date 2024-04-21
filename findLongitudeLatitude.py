import pandas as pd
from fuzzywuzzy import process
import json

# Load the shelter data from JSON
with open('updated_shelter_data_with_all_locations.json', 'r') as file:
    shelter_data = json.load(file)

# Read the CSV file
df = pd.read_csv('03-12.csv')

# Prepare a dictionary to map destinations to coordinates
destination_coordinates = {}
for shelter, coords in shelter_data.items():
    destination_coordinates[shelter] = (coords['cordinates']['longitude'], coords['cordinates']['latitude'])

# Function to find the best match above a similarity threshold
def get_coordinates(destination, threshold=87):
    if pd.isna(destination):
        return (None, None)  # Return None values if destination is NaN
    result = process.extractOne(str(destination), destination_coordinates.keys(), score_cutoff=threshold)
    if result:
        match, score = result
        return destination_coordinates[match]
    return (None, None)  # Return a tuple of None values if no match is found

# Apply the function to each destination in the DataFrame
df['Longitude'], df['Latitude'] = zip(*df['Destination'].apply(get_coordinates))

# Save the updated DataFrame to a new CSV file
df.to_csv('MorvaSatty_-3-12_Longitude_Latitude_data.csv', index=False)

print("Output file has been saved with longitude and latitude data where matches were found.")

import requests
import openpyxl

# Replace with your own Geonames API username
geonames_username = "your_geonames_username"

# Define the country code you're interested in (e.g., "FR" for France)
target_country_code = "FR"  # Change if you're working with locations in other countries

# Open the Excel file
wb = openpyxl.load_workbook('extract_locations_experiments.xlsx')
sheet = wb.active


# Function to query Geonames API
def get_geoname_info(location):
    # Construct the URL for the Geonames API
    url = f'http://api.geonames.org/searchJSON?q={location}&maxRows=1&username={geonames_username}'

    # Make the API request
    response = requests.get(f'http://api.geonames.org/searchJSON?q={location}&maxRows=1&username={geonames_username}')

    # Parse the response
    data = response.json()

    # Check if we received any results
    if data['geonames']:
        return data['geonames'][0]['name']  # Return the name of the first result
    else:
        return 'Not found'


# Iterate over the locations in column B and get the Geonames result for each
for row in range(2, sheet.max_row + 1):  # Starting from row 2 to skip header
    location = sheet[f'B{row}'].value  # Get location from column B
    if location:
        geoname_result = get_geoname_info(location)  # Get Geonames result
        sheet[f'C{row}'] = geoname_result  # Write the result to the "Geonames Results" column (C)

# Save the modified Excel file
wb.save('output_with_geonames_results.xlsx')

print("Geonames API results have been added to the file.")

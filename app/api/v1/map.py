from fastapi import APIRouter
from google.cloud import bigquery
import json
from shapely import wkt
from geojson import Feature


# disasters: https://public.emdat.be/data

# most geojson from https://datahub.io/core/geo-countries#data
# add/create missing geojson https://geojson.io/



router = APIRouter( tags=["Map"])


@router.get("/earthquakes")
async def get_earthquakes():
    return {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [145.616, 19.246]
            },
            "properties": {
                "Date": "01/02/1965",
                "Time": "13:44:18",
                "Type": "Earthquake",
                "Depth": 131.6,
                "Magnitude": 6,
                "Magnitude Type": "MW",
                "ID": "ISCGEM860706",
                "Source": "ISCGEM",
                "Location Source": "ISCGEM",
                "Magnitude Source": "ISCGEM",
                "Status": "Automatic"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [127.352, 1.863]
            },
            "properties": {
                "Date": "01/04/1965",
                "Time": "11:29:49",
                "Type": "Earthquake",
                "Depth": 80,
                "Magnitude": 5.8,
                "Magnitude Type": "MW",
                "ID": "ISCGEM860737",
                "Source": "ISCGEM",
                "Location Source": "ISCGEM",
                "Magnitude Source": "ISCGEM",
                "Status": "Automatic"
            }
        }
    ]
}

@router.get("/countries")
async def get_countries():
    client = bigquery.Client()

    # Define the query.
    query = """
        SELECT Country
        FROM `personal-website-610c4.locations.countries`
        LIMIT 1000
    """

    # Run the query.
    query_job = client.query(query)  # Make an API request.

    # Fetch the results.
    countries = query_job.result()

    countries = [country.Country for country in countries]
    return countries

@router.get("/country/{country}")
async def get_country(country: str):
    client = bigquery.Client()

    # Define the query.
    query = """
        SELECT *
        FROM `personal-website-610c4.locations.countries`
        WHERE Country = @country
        LIMIT 1000
    """

    # Set up the query parameters.
    query_params = [
        bigquery.ScalarQueryParameter("country", "STRING", country)
    ]
    
    # Set up the job configuration.
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params

    # Run the query.
    query_job = client.query(query, job_config=job_config)  # Make an API request.

    # Fetch the results.
    result = query_job.result()

    # Convert the result to a list of dictionaries to make it JSON serializable.
    rows = [dict(row) for row in result]

    
        
    # Get the first row (if any).
    if len(rows) > 0:
        # Convert it to GeoJSON.
        data = rows[0]

        # Assume `geometry` is a string in WKT format.
        geometry_wkt = data.pop('geometry')

        # Parse the WKT string into a Shapely geometry object.
        geometry_obj = wkt.loads(geometry_wkt)

        # Convert the Shapely geometry object to a GeoJSON-compatible dict.
        geometry_geojson = Feature(geometry=geometry_obj).geometry

        geojson = {
            "type": "Feature",
            "properties": data,
            "geometry": geometry_geojson
        }
        return geojson
    else:
        return {"detail": "Country not found"}

# @router.get("/test")
# async def test():
#     import geopandas as gpd
#     import pandas as pd

#     # Load GeoJSON file into a GeoDataFrame
#     geo_data = gpd.read_file('countries.geojson')

#     # Convert the GeoDataFrame to a DataFrame
#     df_geo = pd.DataFrame(geo_data)  # drop the geometry column because it cannot be stored in a CSV

#     # Load CSV file into a DataFrame
#     df_csv = pd.read_csv('countries.csv')

#     # Merge the DataFrames on the country column
#     df = pd.merge(df_csv, df_geo, left_on='Country', right_on='ADMIN', how='outer', indicator=True)

    

#     # Get list of countries from original CSV that were not included in the merge
#     unmatched_countries = df[df['_merge'] == 'left_only']['Country'].tolist()

#     # Save the merged data to a new CSV file
#     df = df[df['_merge'] == 'both']
#     df = df.drop(columns=['ADMIN', 'ISO_A3', '_merge'])

#     print(df.head())


#     df.to_csv('merged_data.csv', index=False)  # only include rows where merge was successful

#     print(f'These countries were not matched during the merge: {unmatched_countries}')



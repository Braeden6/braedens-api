from fastapi import APIRouter, Depends, HTTPException
from google.cloud import bigquery


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
        FROM `personal-website-610c4.locations.country_data`
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
        FROM `personal-website-610c4.locations.country_data`
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
    
    return rows


@router.get("/countries/fix")
async def fix_countries():
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Define the query.
    query = """
        UPDATE `personal-website-610c4.locations.country_data`
        SET Country = TRIM(Country)
    """

    # Run the query.
    query_job = client.query(query)  # Make an API request.

    # Wait for the job to finish.
    query_job.result()

    print("Updated country names successfully.")

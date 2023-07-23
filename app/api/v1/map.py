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
    client = bigquery.Client()

    # Define the query to fetch countries not in the joined table.
    query = """
        SELECT *
        FROM `personal-website-610c4.locations.country_data` AS loc
        LEFT JOIN `personal-website-610c4.locations.joined_country_data` AS joined
        ON TRIM(loc.Country) = joined.Country
        WHERE joined.Country IS NULL
    """

    # Run the query.
    query_job = client.query(query)  # Make an API request.

    # Fetch the results.
    not_in_joined = [row for row in query_job]

    row = not_in_joined[0]

    latitude = 25.025885
    longitude = -78.035889
    
    if row.Country != "Bahamas, The":
        print(row.Country)
        return 

    query = f"""
        INSERT INTO `personal-website-610c4.locations.joined_country_data`
        (Country, Region, Population, Area__sq__mi__, Pop__Density__per_sq__mi__, Coastline__coast_area_ratio_, Net_migration, Infant_mortality__per_1000_births_, GDP____per_capita_, Literacy____, Phones__per_1000_, Arable____, Crops____, Other____, Climate, Birthrate, Deathrate, Agriculture, Industry, Service, latitude, longitude)
        VALUES ('{'The Bahamas' if row.Country else 'Unknown'}', '{row.Region if row.Region else 'Unknown'}', {row.Population if row.Population else 0}, {row.Area__sq__mi__ if row.Area__sq__mi__ else 0}, {row.Pop__Density__per_sq__mi__ if row.Pop__Density__per_sq__mi__ else 0}, {row.Coastline__coast_area_ratio_ if row.Coastline__coast_area_ratio_ else 0}, {row.Net_migration if row.Net_migration else 0}, {row.Infant_mortality__per_1000_births_ if row.Infant_mortality__per_1000_births_ else 0}, {row.GDP____per_capita_ if row.GDP____per_capita_ else 0}, {row.Literacy____ if row.Literacy____ else 0}, {row.Phones__per_1000_ if row.Phones__per_1000_ else 0}, {row.Arable____ if row.Arable____ else 0}, {row.Crops____ if row.Crops____ else 0}, {row.Other____ if row.Other____ else 0}, {row.Climate if row.Climate else 0}, {row.Birthrate if row.Birthrate else 0}, {row.Deathrate if row.Deathrate else 0}, {row.Agriculture if row.Agriculture else 0}, {row.Industry if row.Industry else 0}, {row.Service if row.Service else 0}, {latitude}, {longitude})
    """

    print(query)
    
    # Run the insert query.
    query_job = client.query(query)  # Make an API request.
    
    # Wait for the job to finish.
    query_job.result()

    print(not_in_joined[0])
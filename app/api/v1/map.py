from fastapi import APIRouter, Depends, HTTPException


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

var express = require('express');
var router = express.Router();
var getContainer = require('../public/javascripts/getContainer');

/* GET home page. */
router.get('/getEarthquakeData', async (req, res, next) =>  {
    const querySpec = {
        query: `SELECT e.type, e.geometry, e.properties
                FROM earthquakes e`
    }

    const container = getContainer("mapContent", "earthquakes");
    const { resources } = await container.items.query(querySpec).fetchAll();

    responseMessage = {reply: "data found", earthquakes: resources}
  
    
    res.json(responseMessage);
  });

  router.get('/getLocations', async (req, res, next) =>  {
    const querySpec = {
        query: `SELECT c.name, c.type, c.coordinates
                FROM countries c`
    }

    const container = getContainer("mapContent", "countries");
    const { resources } = await container.items.query(querySpec).fetchAll();

    responseMessage = {reply: "data found", locations: resources}
  
    
    res.json(responseMessage);
  });


  router.get('/getCountryBorder', async (req, res, next) =>  {
    const querySpec = {
        query: `SELECT  "Feature" as type,
                        {"name": c.name} as properties ,
                        { "type": c.geometry_type, "coordinates" : c.border} as geometry
                FROM countries c`
    }
    const container = getContainer("mapContent", "countries");
    const { resources } = await container.items.query(querySpec).fetchAll();
    responseMessage = {reply: "data found", borders: resources}
    res.json(responseMessage);
  });


module.exports = router;
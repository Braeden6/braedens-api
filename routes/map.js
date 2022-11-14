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
        query: `SELECT l.name, l.type, l.coordinates
                FROM locations l`
    }

    const container = getContainer("mapContent", "locations");
    const { resources } = await container.items.query(querySpec).fetchAll();

    responseMessage = {reply: "data found", locations: resources}
  
    
    res.json(responseMessage);
  });


module.exports = router;
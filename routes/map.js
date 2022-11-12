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

    if (resources.length > 0) {
        responseMessage = {reply: "data found", earthquakes: resources, }
    }
    
    res.json(responseMessage);
  });


module.exports = router;
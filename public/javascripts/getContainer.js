const CosmosClient = require("@azure/cosmos").CosmosClient

module.exports = function (databaseID, containerID) {
    const endpoint = process.env.WEBSITE_DATABASE_ENDPOINT
    const key = process.env.WEBSITE_DATABASE_KEY
    
    const client = new CosmosClient({endpoint, key})

    const database = client.database(databaseID)
    return database.container(containerID)
}
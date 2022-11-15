const getContainer = require("./getContainer");


module.exports = async function (email) {
    const container = getContainer("UserData", "users")
    const querySpec = {
        query: "SELECT * FROM users u where u.id=@id",
        parameters: [
            {
                name: "@id",
                value: email
            }
        ]
    }
    const {resources} = await container.items.query(querySpec).fetchAll();
    return resources;
}
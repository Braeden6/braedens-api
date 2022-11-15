var express = require('express');
var router = express.Router();
const validateJWT = require('../public/javascripts/verifyUser').validateJWT
const getDecodedToken = require('../public/javascripts/verifyUser').getDecodedToken
const findUser = require('../public/javascripts/findUser');
const getContainer = require('../public/javascripts/getContainer');

router.post('/addUser',  async (req, res, next) =>  {
    let responseMessage = {reply:"something went wrong"};
    const users = await findUser(req.body.email)

    if (users.length > 0) {
        responseMessage = {reply: "account found"};
        try {
            await validateJWT(req.body.token, users[0].oid);
        } catch (e) {
            console.log(e)
            res.json({reply:"Account Found, but could not verify user"});
            return;
        }    
    } else {
        let decodedToken = await getDecodedToken(req.body.token);
        let item = {
            "id" : req.body.email,
            "name" : req.body.name,
            "savedResumes" : [],
            "oid" : decodedToken.payload.oid
        }
        const container = getContainer("UserData", "users");
        await container.items.create(item);
        responseMessage = {reply: "account created"};
    }

  res.json(responseMessage);
});

router.delete('/deleteResume', async (req, res, next) => {
    // body has token (tokenID), email (of user related to token id), saveName (name the resume will be saved under), resume
    let responseMessage = {reply:"something went wrong"};
    const users = await findUser(req.body.email)

    if (users.length > 0) {
        try {
            validateJWT(req.body.token, users[0].oid);
        } catch (e) {
            console.log(e)
            res.json({reply:"could not verify user"});
            return;
        }
        

        let resumeList =  []
        for( const resume of users[0].savedResumes) {
            resumeList[resumeList.length] = resume.name;
        }
        const container = getContainer("UserData", "users")

        if (resumeList.includes(req.body.deleteName)) {
            users[0].savedResumes.splice(resumeList.indexOf(req.body.deleteName),1)
            container.item(req.body.email).replace(users[0])
            responseMessage = {reply:`deleted ${req.body.deleteName}`};
        } else {
            responseMessage = {reply:`did not delete ${req.body.deleteName}`};
        }

    }

    res.json(responseMessage);
});

router.get('/getMyResume', async (req, res, next) => {
    // nothing required
    let responseMessage = {reply:"something went wrong"};

    const querySpec = {
        query: `SELECT c.resume
                FROM users u
                JOIN c in u.savedResumes
                WHERE u.id = @email and c.name = @saveName`,
        parameters: [
            {
                name: "@email",
                value: "bnorman11@live.com"
            },
            {
                name: "@saveName",
                value: "main"
            }
        ]
    }
    const container = getContainer("UserData", "users");
    const { resources } = await container.items.query(querySpec).fetchAll();
    if (resources.length > 0) {
        responseMessage = {reply: "found resume", resume: resources[0].resume}
    }
    res.json(responseMessage);
});

router.get('/getResume', async (req, res, next) => {
    // query token (tokenID), email (of user related to token id), saveName (name of the resume you are getting)
    let responseMessage = {reply:"something went wrong"};
    const users = await findUser(req.query.email)

    if (users.length > 0) {
        try {
            validateJWT(req.query.token, users[0].oid);
        } catch (e) {
            console.log(e)
            res.json({reply:"could not verify user"});
            return;
        }

        const querySpec = {
            query: `SELECT c.resume
                    FROM users u
                    JOIN c in u.savedResumes
                    WHERE u.id = @email and c.name = @saveName`,
            parameters: [
                {
                    name: "@email",
                    value: req.query.email
                },
                {
                    name: "@saveName",
                    value: req.query.saveName
                }
            ]
        }
        const container = getContainer("UserData", "users");
        const { resources } = await container.items.query(querySpec).fetchAll();
        if (resources.length > 0) {
            responseMessage = {reply: "found resume", resume: resources[0].resume}
        }
        res.json(responseMessage);
    }
    
    
});

router.get('/getResumeList', async (req, res, next) => {
    let responseMessage = {reply:"something went wrong"};
    let users = await findUser(req.query.email)

    if (users.length > 0) {
        try {
            validateJWT(req.query.token, users[0].oid);
        } catch (e) {
            console.log(e)
                res.json({reply:"could not verify user"});
            return;
        }
        let resumeList =  []
        for( const resume of users[0].savedResumes) {
            resumeList[resumeList.length] = resume.name;
        }
        responseMessage = { reply : "found resumes", resumes: resumeList}
    } 
    res.json(responseMessage);
});

router.post('/saveResume', async (req, res, next) => {
    // body has token (tokenID), email (of user related to token id), saveName (name the resume will be saved under), resume
    let responseMessage = {reply:"something went wrong"};
    console.log(req.body.email)
    const users = await findUser(req.body.email)

    if (users.length > 0) {
        try {
            validateJWT(req.body.token, users[0].oid);
        } catch (e) {
            console.log(e)
            res.json({reply:"could not verify user"});
            return;
        }

        let resumeList =  []
        for( const resume of users[0].savedResumes) {
            resumeList[resumeList.length] = resume.name;
        }
        const container = getContainer("UserData", "users")
        
        if (resumeList.includes(req.body.saveName)) {
            users[0].savedResumes[resumeList.indexOf(req.body.saveName)] = {name: req.body.saveName , resume : req.body.resume}
            responseMessage = {reply:`updated ${req.body.saveName}`};
        } else {
            users[0].savedResumes.push({name: req.body.saveName , resume : req.body.resume})
            responseMessage = {reply:`saved ${req.body.saveName}`};
        }
        container.item(req.body.email).replace(users[0])
    }
    res.json(responseMessage);
});




module.exports = router;

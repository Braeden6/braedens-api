const jwt = require('jsonwebtoken');
const jwkToPem = require('jwk-to-pem');
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));


async function getJwkByKid(kid) {
    let issResponse =  await fetch("https://login.microsoftonline.com/common/discovery/keys?appid=" + process.env.AZURE_AD_LOGIN_CLIENT_ID);
    let response = await issResponse.json()

    for (let index = 0; index < response.keys.length; index++) {
        const key = response.keys[index];
        if (key.kid === kid) {
          return key
        }
      }
      throw new Error("Key Not in Iss")
}



async function validateJWT(accessToken, oid) {
    const decodedToken = await jwt.decode(accessToken, { complete:true});

    if (!decodedToken) {
        throw new Error("Invalid Token");
    }

    if (oid !== decodedToken.payload.oid) {
       throw new Error("Could Not Identify User")
    }
    
    //if("https://sts.windows.net/e270fdd0-eeee-4abf-b7de-3ad68044f500/" !== decodedToken.payload.iss) {
     //   throw new Error ("Not Trusted Token Issuer")
    //}

    //await getJwkByKid(decodedToken.header.kid);
    // TODO: update validation to 100% confirm this is all that is needed

    return decodedToken;
}

async function getDecodedToken(accessToken) {
    return await jwt.decode(accessToken, { complete:true});
}


module.exports = {validateJWT, getDecodedToken};
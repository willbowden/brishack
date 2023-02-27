import userPool from "./config.js";

// Authenticate a user
var authenticationData = {
    Username: 'user@example.com',
    Password: 'password'
};
var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);
var userData = {
    Username: 'user@example.com',
    Pool: userPool
};
var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
cognitoUser.authenticateUser(authenticationDetails, {
    onSuccess: function (result) {
        console.log('Access token:', result.getAccessToken().getJwtToken());
    },

    onFailure: function(err) {
        console.error(err);
    }
});

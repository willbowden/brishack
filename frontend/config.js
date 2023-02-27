// Import the necessary Amazon Cognito SDK modules
import { CognitoUserPool, AuthenticationDetails, CognitoUser } from '@aws-sdk/client-cognito-identity-provider';

// Set up the Amazon Cognito user pool object
const poolData = {
    UserPoolId: 'your_user_pool_id',
    ClientId: 'your_client_id'
};
const userPool = new CognitoUserPool(poolData);

// Authenticate a user with their username and password
async function authenticateUser(username, password) {
    try{
        const authenticationData = {
        Username: username,
        Password: password
        };
        const authenticationDetails = new AuthenticationDetails(authenticationData);
        const userData = {
            Username: username,
            Pool: userPool
        };
        const cognitoUser = new CognitoUser(userData);

        const authenticatedUser = 
        await cognitoUser.authenticateUser(authenticationDetails, {
            onSuccess: (result) => {
                const accessToken = result.getAccessToken().getJwtToken();
                console.log('Access token:', accessToken);
            },
            onFailure: (err) => {
                console.error(err);
            }
        });
        return authenticatedUser;
    } catch(error) {
        return error
    }
};

export default authenticateUser;



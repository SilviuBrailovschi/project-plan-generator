# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

## Installing pip dependencies:
* cd server
* run `pip install -r requirements.txt`

## Huggingface API authentication :
* navigate to the server folder from root
* run `jupyter notebook` : this will open a jupyter notebook instance in the browser
* go to Toolbar -> File -> New -> Console 
* paste 
```
  from getpass import getpass
  from huggingface_hub import notebook_login

    def login_with_token():
    token = getpass("Token: ")
    notebook_login(token=token)
    
    login_with_token()
```
 into the terminal input
* execute script pressing shift + enter
* paste the token and click login button
* Check if you are authenticated `huggingface-cli whoami ` you should see you huggingface username as output

## Starting server :
 * cd server
 * run `uvicorn app:app --reload`
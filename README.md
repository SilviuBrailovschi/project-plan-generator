# Project Documentation

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Client Setup

### Installing Dependencies
Install the required dependencies:

###   ` npm install`

### Available Scripts

In the project directory, you can run:

#### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

#### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

## Server Setup

### Prerequisites

Make sure you have Python and pip installed locally. If not, install them from the following links:
- [Python](https://www.python.org/downloads/)
- [pip](https://phoenixnap.com/kb/install-pip-windows)

### Installing pip dependencies

1. Navigate to the server directory:
    ```bash
    cd server
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Huggingface API Authentication

1. Navigate to the server folder from the project root:
    ```bash
    cd server
    ```
2. Start a Jupyter notebook instance:
    ```bash
    jupyter notebook
    ```
3. In the Jupyter notebook interface, go to `Toolbar -> File -> New -> Console`.
4. Paste the following code into the terminal input:
    ```python
    from getpass import getpass
    from huggingface_hub import notebook_login

    def login_with_token():
        token = getpass("Token: ")
        notebook_login(token=token)

    login_with_token()
    ```
5. Execute the script by pressing `Shift + Enter`.
6. Paste your token when prompted and click the login button.
7. Verify authentication:
    ```bash
    huggingface-cli whoami
    ```
   You should see your Huggingface username as the output.

### Starting the Server

1. Navigate to the server directory:
    ```bash
    cd server
    ```
2. Start the server using Uvicorn:
    ```bash
    uvicorn app:app --reload
    ```
# Project Documentation

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Client Setup

### Prerequisites
Make sure you have Node.js and npm installed locally. If not, install them from the following links:
- [Node.js](https://nodejs.org/)
- npm is included with Node.js installation.

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

### Starting the Server

1. Navigate to the server directory:
    ```bash
    cd server
    ```
2. Start the server using Uvicorn:
    ```bash
    uvicorn app:app --reload
    ```
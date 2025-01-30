# Getting Started with Create React Website Application

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

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.




**Backend:**
This project is designed to help you build and deploy a Flask API to generate text-based responses using Google’s Generative AI models.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.6 or above
Flask
Flask-CORS
Google’s Generative AI library
You’ll also need a Google API key with permissions to access Google Generative AI.

Installation
Clone the repository:

git clone https://github.com/JukalAdhitya/NLP-to-SQL.git

cd NLP-to-SQL

Install dependencies: Use pip to install the required packages.

pip install Flask Flask-CORS google-generativeai
Set up your API Key: Replace the placeholder API key in the code with your actual Google API key.

Usage
Run the Flask server:

python app.py
This will start the server on http://127.0.0.1:5000.

Send a request: To generate a response, send a POST request to http://127.0.0.1:5000/generate with a JSON payload that includes a prompt

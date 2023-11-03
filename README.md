# AtliQ Brand Store Stocke Management Using LangChain LLM 
### [https://brandstorellm.streamlit.app/](https://brandstorellm.streamlit.app/)

## Overview

The **AtliQ Brand Store Management Database Q&A Tool** is a web application designed to provide users with a convenient way to interact with a clothing store database. Developed by Shubham Khairmode, this project leverages a powerful stack of technologies, including **Google Cloud APIs**, **GoogleMakesuite API**, **GooglePalm**, **Google-GenerativeAI**, **Streamlit**, **Flask**, and a **MySQL database**. It offers users the ability to ask questions related to the clothing inventory and receive informative responses.

### Key Features

- **Intuitive Querying**: Users can simply type questions in natural language, and the tool interprets and processes these queries to extract meaningful information from the database.

- **Fast Response Times**: The tool employs advanced language models and efficient data processing to provide quick and accurate answers to user queries.

- **Informative Answers**: Users receive detailed responses, including relevant data and explanations, ensuring a thorough understanding of the queried information.

- **Modern User Interface**: The tool features a user-friendly interface powered by Streamlit and Flask, making it easy for users to interact with the database.

## Technologies Used 

1. **GoogleMakesuite API**: This API is employed to access Google's suite of cloud services, which provides essential functionality for the project, including language processing and data retrieval.

2. **GooglePalm**: GooglePalm is a powerful language model from Google that assists in processing user queries and generating informative responses.

3. **Google-GenerativeAI**: This technology, likely associated with Google, contributes to the generation of human-like text, which is crucial for providing detailed answers to user queries.

4. **Streamlit**: The web application's user interface is built using Streamlit, a popular Python library for creating interactive and user-friendly data applications.

5. **Flask**: Flask is used as a web framework for routing and handling user requests, allowing for a smooth user experience.

6. **MySQL Database**: The project integrates with a MySQL database to store and manage the clothing store's inventory data.

## Prerequisite

- [langchain](https://python.langchain.com/docs/get_started/introduction)
- [streamlit](https://docs.streamlit.io/)

## Create the Environment

    conda create -p venv python=3.10 -y

## Activate the environment 

    conda activate venv/

## Install the requirements

    pip install -r requirements.txt

## create the GooglePalm API key

1. Login you gmail account in 

- [makersuite](https://makersuite.google.com/)

```http
  GET GooglePalm API
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

## create the api key and copy paste in your .env file

        GOOGLE_API_KEY = 'Your API key'

## run the app 
#### using streamlit
```http
  streamlit run main.py
```
#### using Flask
```http
  python app.py
```
## Database 
For sql data contact me on Linkedin
- [Linkedin](https://www.linkedin.com/in/shubhambkhairmode)

## Contact

- **Developer**: Shubham Khairmode
- **Email**: shubhambkhairmode@gmail.com

## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

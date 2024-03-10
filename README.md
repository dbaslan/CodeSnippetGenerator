# CodeSnippetGenerator
A web application that leverages an LLM to generate code snippets based on user inputs. Code snippets can be improved through user feedback.

Tools Used:
- Python
- FastAPI
- Docker
- HTML, CSS, JavaScript
- GPT 3.5 Turbo

The application is Dockerized an deployed on Microsoft Azure: [Link](http://csgdba.accgacdfabgph5ed.japaneast.azurecontainer.io)

The deployment is online as of 10 March 2024, but will be taken offline eventually. Note that the application uses a personal API key, so it cannot be used indefinitely.

In order to run it locally, follow the instructions below.

ChatGPT and Copilot were used for identifying and fixing bugs.

![Screenshot](https://raw.githubusercontent.com/dbaslan/CodeSnippetGenerator/main/Screenshot.png)

## Usage Instructions

The user interface is simple and straightforward. Type in your prompt in the text box, then click the "Generate Code Snippet" button. Once the model generates and displays your code, you will have the option to provide feedback in a new text box. You may rewrite and submit feedback as many times as you like, and the model will rewrite its output as per your instructions.

## Deployment Instructions

### 1. Run locally
0. Install Python 3.10
1. Download the source code.
2. Create a .env file in the same directory as main.py
3. Put your OpenAI API key within the .env file, like so:

![Screenshot3](https://github.com/dbaslan/CodeSnippetGenerator/assets/66262500/4c29ce42-bbd1-46ad-982e-1704ae53e812)

4. Open the terminal and go to the project directory.
5. Install dependencies by executing the following command in the terminal:
```
pip install -r requirements. txt
```
6. Run the application by executing the following command in the terminal:
```
uvicorn main:app --reload
```
7. Use the application by going to 'localhost:8000' on your browser.

### 2. Deploy through Docker
0. Install Docker
1. Download the source code.
2. Create a .env file in the same directory as main.py
3. Put your OpenAI API key within the .env file
4. Open the terminal and go to the project directory.
5. Build Docker image by executing the following command in the terminal:
```
docker build -t csg .
```
6. Deploy Docker image by executing the following command in the terminal:
```
docker run -d --name csgc -p 80:80 csg
```
7. Use the application by going to 'localhost:80' on your browser.

## Modification Instructions

Code Snippet Generator, as it is, makes use of OpenAI's GPT 3.5 Turbo Instruct model through their API. However, it is possible to pick a different model and change the parameters to one's liking. These settings can be found in main.py, specifically under the call_openai_api() function:

![Screenshot2](https://github.com/dbaslan/CodeSnippetGenerator/blob/main/Screenshot2.png)

Simply browse [OpenAI's documentation](https://platform.openai.com/docs/models) to pick your ideal model, and replace the model parameter which is set to "gpt-3.5-turbo-instruct" by default. It is also possible to fine-tune the model's output by changing the max_tokens and temperature parameters. Experiment with the parameters until you find an ideal configuration.

## Requirements and Versioning

The application was built with Python 3.10.9, and should be compatible with any version >= 3.10. Below is the full list of required packages, as listed in requirements.txt:

- ﻿annotated-types==0.6.0
- ﻿anyio==4.3.0
- ﻿certifi==2024.2.2
- ﻿click==8.1.7
- ﻿colorama==0.4.6
- ﻿distro==1.9.0
- ﻿exceptiongroup==1.2.0
- ﻿**fastapi==0.110.0**
- ﻿greenlet==3.0.3
- ﻿h11==0.14.0
- ﻿httpcore==1.0.4
- ﻿httpx==0.27.0
- ﻿idna==3.6
- ﻿Jinja2==3.1.3
- ﻿MarkupSafe==2.1.5
- ﻿**openai==1.13.3**
- ﻿pydantic==2.6.3
- ﻿pydantic_core==2.16.3
- ﻿python-dotenv==1.0.1
- ﻿python-multipart==0.0.9
- ﻿sniffio==1.3.1
- ﻿starlette==0.36.3
- ﻿tqdm==4.66.2
- ﻿typing_extensions==4.10.0
- ﻿**uvicorn==0.27.1**

## Limitations

The application is a personal project with a small scope. As such, it does not have persistent storage and instead stores your input in memory. Once you close the application, your data will be deleted. If you are a developer and wish to implement permanent storage, consider installing the required packages and creating a SQLite or PostgreSQL database, which you can integrate through main.py.

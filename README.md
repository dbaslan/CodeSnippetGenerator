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

In order to run it locally, install Python, clone the repo, create a .env file in the same directory as main.py with your OpenAI API key in it, install the requirements, and then run the server with the command 'uvicorn main:app --reload'.

Alternatively, install Docker, use the Dockerfile to build a Docker image with 'docker build -t csg .' and then run it with 'docker run -d --name csgc -p 80:80 csg'.

ChatGPT and Copilot were used for identifying and fixing bugs.

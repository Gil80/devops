## Description
This project runs a flask app that prints the IP address of the container its running on, and an Nginx webserver that acts as a round-robin load balancer.

The `docker-compose.yml` is configured to run three instances (containers) of the same flask app.

## Local usage without Nginx LB
1. run the app.py locally to validate it running and exposing IP address of the flask server on port 5000. Make sure you have flask module installed.
2. build a container from the dockerfile using `docker build -t flask .` 
3. run the container using `docker run -it -u gil -p 5000:5000 flask bash`
4. within the bash of the running container, run: `python3 app.py`
5. the flask app should run on `http://127.0.0.1:5000` click on the URL and validate the browser prints "172.17.0.2"

## Local usage with Nginx LB
1. Clone this repo to your local machine
2. From within the root directory of the project, run `docker compose up --build --scale app=3`
3. Once the environment is up and running, browse to `http://localhost:9090` and you should see the IP address of one of the containers running an instance of flask.
4. Press F5 to see how the round-robin LB directs the request to a different IP/container.

## Cleaning the environment
1. Press CTRL+C to stop the containers
2. run `docker compose down` to remove the containers



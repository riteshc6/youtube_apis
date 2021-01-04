# youtube_apis

App to periodically fetch youtube videos and serve through api

## Quickstart
1. Install docker-compose https://docs.docker.com/compose/install/
2. Add .env file in root directory with variables APIKEY, BASEURL, ES_HOSTS
3. Run docker-compose
    ```bash
        sudo docker-compose up -d
    ```
4. Stop docker-compose
    ```bash
        sudo docker-compose down
    ```

## Setting up

1. Create a virtual environment
    ```bash
    python3 -m venv myenv
    ```
    or
    ```bash
    # If you have virtualenv installed

    virtualenv -p python3 myenv
    ```

2. Activate the virtual environment
    ```bash
    source ./myenv/bin/activate
    ```

3. Install all dependency
    ```bash
    pip intall -r requirements.txt
    ```

4. Install  and run elasticsearch locally https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

5. Setup Enivronment Variables APIKEY, BASEURL, ES_HOSTS

6. Run the development web server
    ```bash
        uvicorn app.main:app --reload
    ```
## Deploy Using Docker

1. Install  and run elasticsearch locally https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html

2. Run Deployment script
    ``` bash
        sudo bash deploy.sh
    ```

# And then open it at browser
   http://127.0.0.1:8000/

# Check swagger Api's
   http://127.0.0.1:8000/api/v1/docs

# Check ReDoc Documentation
   http://127.0.0.1:8000/api/v1/redoc

# weather csv reader into api python webserver

reads csv file into python fastAPI webserver with docker integration and test suite

## Getting Started

### Prerequisites

- Docker: Follow the [official install guide](https://docs.docker.com/get-docker/) for Docker.
- Python: Follow the [official install guide](https://www.python.org/downloads/) for Python.

### Setup

Clone this repository to your local machine.

   ```sh
   git clone <repository-url>
   cd <repository-directory> 
   ```


### Running app

#### running with docker
   
1. Build app Docker image
    ```sh
   docker build -t csvreaderapp .
   ```
   
2. Run Docker image
    ```sh
   docker run -p 4000:80 csvreaderapp
    ```
   
3. Build the Docker image for the test suite.
    ```sh
   in separate terminal
   cd <repository-directory>/test
   docker build -t csvreaderapp-test .
    ```
   
4. Run test suite
    ```sh
   docker run csvreaderapp-test
    ```
   expected output:
   ```sh
   ........
   ----------------------------------------------------------------------
   Ran 8 tests in 0.057s

   OK
    ```
   
#### running locally

1. Run app
    ```sh
   uvicorn app:app --host 0.0.0.0 --port 80 --reload
    ```
   
2. Run test
    ```sh
   in separate terminal
   cd <repository-directory>/test
   python -m unittest test_app.py  
    ```
   expected output:
   ```sh
   ........
   ----------------------------------------------------------------------
   Ran 8 tests in 0.057s

   OK
    ```

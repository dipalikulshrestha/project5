# project5
# Capstone Udacity - Full Stack API Final Project

This project is to deploy a Flask application using Heroku and PostgreSQL and enable Role Based Authentication and roles-based access control git (RBAC) with Auth0 (third-party authentication systems).


# Application: Full Stack Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 


# Roles and Permissions:

There are 3 different types of roles associated with this application. The details and permissions associated are given below:

1. Casting Assistant
    * get:actors
    * get:movies

2. Casting Director
    * delete:actors
    * get:actors
    * get:movies
    * patch:actors
    * patch:movies
    * post:actors

3. Executive Producer
    * delete:actors
    * delete:movies
    * get:actors
    * get:movies
    * patch:actors
    * patch:movies
    * post:actors
    * post:movies
    

## Pre-Requisites

Create a postgre database for testing the app locally  before deploying to Heroku.
JWT tokens for each of the roles (Casting Assistant, Casting Director and Executive Producer) with appropriate permissions mapped to them (provided below with an expiry time of 24 hours)

## PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the project directory and running:

pip install -r requirements.txt


# The project is hosted live via Heroku.
Role based authentication has been setup for 3 roles (Casting Assistant, Casting Director and Executive Producer) using AUTH0.

### API Endpoint for testing 

https://cap-dipali.herokuapp.com/

## Unit Testing

1. To run the tests locally, make sure you have PostgreSQL installed.
2. Create a postgre database named captest.
3. Setup environment variables as mentioned in config_settings.env file locally by running below commands. 

    * DATABASE_URL - Update the datatabase name, user name, password, port #

        ```bash
        export DATABASE_URL=<Refer to the config_settings.env file and update your database parameters>
        ```

    * TOKEN_TEST - Copy the value from config_settings.env file. This is the Bearer token generated from AUTH0 for the role - Executive Producer which is allowed to run all endpoints.

        ```bash
        export TOKEN_TEST=<Copy/Paste from config_settings.env file as it is>
        ```

4. After setting up environment variables, run the below command. Make sure you are in the folder where test_app.py file is present.

    ```bash
        python test_app.py
    ```


## Test via Postman

1. Authorization token for all roles has been updated in postman collection file - Capstone.postman_collection
2. Import this postman collection file in POSTMAN app and run all cases


## API Reference

### Getting Started

1. Base URL : Backend app is hosted on https://cap-dipali.herokuapp.com/
2. Authentication : Role based authentication using AUTH0

####Below JWTs are available with an expiration time of 24 hours for each of the roles:
Casting Assistant
-----------------
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9IdDMzYVgzQkRxWUphR1Z4czREaiJ9.eyJpc3MiOiJodHRwczovL2RpcGFsaWsuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlY2ZjZjNmNGZjNmI0MGQwMzlkZDJhYiIsImF1ZCI6IkNhcEFQSSIsImlhdCI6MTU5MDkxNTI2NiwiZXhwIjoxNTkwOTIyNDY2LCJhenAiOiJjczdaYkVRNkJvRlRENDNwTUpSTlFKUUViWXpxVFpQZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.U3Fxtw4fYSK72J-5VA1bOG8eDGKTGCVbESIstnmqcXWe4rrm2C6rxGIYvLswGSr9ClAagv718tKYi3jWHS_TJgqUb8jMtkB6MbqHQROznKgchFVLH1WMpNXH4NHWB7ywCfTciVyhDDll1YOk_iQYEABvHhQzyCwts0S5m8ccR1u_ICkZrBCKfiXtZ-z6x6j-eH_Nz4bzbMuIdshE4QyFMoCflVIQIeNMtAMZadFv8y3Jk7xT4PzPvazQRiKBzPuHh7iCbwAXHDliytzcalqFUoxGXWI9U05H8r9qNiprFs823XJuwaaen5rMLC06wycIk17XTfw8nbSyOdWuYr-fGA

Casting Director
----------------
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9IdDMzYVgzQkRxWUphR1Z4czREaiJ9.eyJpc3MiOiJodHRwczovL2RpcGFsaWsuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOWIzOTM3NDlmYjI0MGM4YTIyYTk1MiIsImF1ZCI6IkNhcEFQSSIsImlhdCI6MTU5MDkxNjE3NiwiZXhwIjoxNTkwOTIzMzc2LCJhenAiOiJjczdaYkVRNkJvRlRENDNwTUpSTlFKUUViWXpxVFpQZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.MOAlsPBKS-0BITsgryM8qGYphuNIyKJuZKIqV6k7fUcS3ZAvqxA4hIStUsyfnbVuMFPnCML7u_MJIRvrLRVnjtkrpyawAzBmOMEWiDPfj-f9DyNNGYNG-CUKgDtD9NLzpK94L-Fqs1iIY4uVeOxVJRR-SG-9NJlcTuiveGYw7Rrasnx_70cPXQPirNM2A3yCyl69DzMnGs90j6AXMbP_al1mpbukwhqcO5jKHQobtoJ1goXEuZlTjEd3Mz8pL0ltOXuOyTAooGpaEeKr964HAr6oC5EyRT9GJk6B3iNqxJoq1_xlON8wC8k4h7lDTN6fxcet5r2QKrvSl_oy94_lbQ

Executive Producer
------------------
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9IdDMzYVgzQkRxWUphR1Z4czREaiJ9.eyJpc3MiOiJodHRwczovL2RpcGFsaWsuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOWI0YTJkNjNmODAwMGM4YzIwYTE4OCIsImF1ZCI6IkNhcEFQSSIsImlhdCI6MTU5MDkxNTY4NCwiZXhwIjoxNTkwOTIyODg0LCJhenAiOiJjczdaYkVRNkJvRlRENDNwTUpSTlFKUUViWXpxVFpQZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.N_YyLfddKsC_27pAH1SqbdVV28XjQlpqY0BBTgYpUTGiy_eBvnfkE_zWx_WzVQ1kbftGCUjsrn_krhzET5axCxRKN61kqZj2WonWiJLRq9fSrRsINQ_o8GR_yZ9d0-MpLlY9SMml4LUP2UqXm-xCfMcGEPJe_0Fnii4G7vpld_vpZQ9tMbWmh6zSr_JK8guHT8YriHZZm0R6FsSH0ke4GBl5twd3uncv-mQVsRCxLVnJaqIFH2s1aXoehibSMed0hv7xGbd2owm0rGduCl05LkSJcpOKLmfQW_02BhR0_PeBKLAu9u0vk7zLFfhEVgfcHxaS9x3Scz9FkmsUNnwCYw

### Error Handling

Errors are returned as JSON objects in the following format:

```json
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}
```

The API will return these error types when requests fail:
* 400: bad request
* 404: Resource not found
* 422: unprocessable
* 500: Internal Server Error

If the route requires authentification and the request fails, it will return:
* 401: "authorization_header_missing"
* 400: "invalid_claims"
* 403: "unauthorized"

### Roles and Permissions

#### Casting Assistant 
    • Can view actors and movies

#### Casting Director 
    • All permissions a Casting Assistant has 
    • Add or delete an actor from the database 
    • Modify actors or movies

#### Executive Producer
    • All permissions a Casting Director has 
    • Add or delete a movie from the database

### Endpoints

#### GET /

No authentication required. This is to check if the APP is up and running. 

```json
{
    "Message": "Welcome to the Casting Agency Application",
    "success": true
}
```

#### GET /actors (Auth required)

Returns details of all actors.

Sample output:

```json
{
    "actors": [
        {
            "age": 21,
            "gender": "Female",
            "id": 1,
            "name": "Pooja"
        },
        {
            "age": 35,
            "gender": "Male",
            "id": 2,
            "name": "Deepak"
        }
    ],
    "success": true
}
```

#### GET /actors/<actor_id> (Auth required)

Returns actor details for the given id.

Sample output:

```json
{
    "actors": {
            "age": 21,
            "gender": "Female",
            "id": 1,
            "name": "Pooja"
    },
    "success": true
}
```

#### GET /movies (Auth required)

Returns details of all movies.

Sample output: 

```json
{
    "movies": [
        {
            "id": 1,
            "releasedate": "28-09-2019",
            "title": "In Fabric"
        },
        {
            "id": 2,
            "releasedate": "25-02-2010",
            "title": "3 Idiots"
        }
    ],
    "success": true
}
```

#### GET /movies/<movie_id> (Auth required)

Returns movies details for the given id. 

Sample output: 

```json
{
    "movies": {
            "id": 1,
            "releasedate": "28-09-2019",
            "title": "In Fabric"
    },
    "success": true
}
```

#### POST /actors (Auth required)

Add a new actor.

Sample input:

```json
{
	"name": "Rishabh",
	"age": "20",
	"gender": "Male"
}
```

#### POST /movies (Auth required)

Add a new movie.

Sample input:

```json
{
	"title": "Snookers",
	"releasedate": "16-01-2020"
}
```

#### PATCH /actors/<actor_id> (Auth required)

Update an existing actor. 

Sample input:

```json
{
	"name": "Rohit",
	"age": "25"
}
```

#### PATCH /movies/<movie_id> (Auth required)

Update an existing movie. 

Sample Input:

```json
{
	"title": "Incubator"
}
```

#### DELETE /actors/<actor_id> (Auth required)

Delete an existing actor.

Sample Output:

```json
{
    "deleted_actor_id": 2,
    "message": "Actor details successfully deleted",
    "success": true
}
```

#### DELETE /movies/<movie_id> (Auth required)

Delete an existing movie.

Sample Output:

```json
{
    "deleted_movie_id": 3,
    "message": "Movie details successfully deleted",
    "success": true
}
```

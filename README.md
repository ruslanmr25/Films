Prerequisite


Install Postgres
The prerequisite to running the app locally is to have a PostgreSQL database available in your local, and the Postgres server must be up and running. Verify the Portgres installation, and start the Postgres server using:

# Mac/Linux
# Install Postgres using Brew. Reference: https://wiki.postgresql.org/wiki/Homebrew 
brew install postgresql
# Verify the installation
postgres --version
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop
Verify the database
Open the psql prompt to view the roles, and databases:

# Open psql prompt
psql [username]
# View the available roles
\du
# View databases
\list
Create a virtual environment
Once you have the starter file in your project directory, create a virtual environment that will help you keep the Python packages isolated from the ones already installed in your local machine.
cd capstone

# Create a Virtual environment
python3 -m venv myvenv
source myvenv/bin/activate

Set up the environment variables
After you have looked at the starter files, set up the environment variables as:
# You should have setup.sh and requirements.txt available
chmod +x setup.sh
source setup.sh


pip install -r requirement.txt
# Run the app
python3 app.py


## API Documentation

### Models
There are two models:
* Movie
	* title
	* release_date
* Actor
	* name
	* age
	* gender


Running the API [TODO] 
API endpoints can be accessed via https://fcnd.herokuapp.com/ 

### Endpoints


#### GET /movies 
* Get all movies

* Require `get:movie` permission

* **Example Request:** `curl 'http://localhost:8080/movie' \
		--header 'Authorization: Bearer <Your token>'`

* **Expected Result:**
    ```json
	{
		"movies": [{
			"id":1,
			"release_date": "2022-03-19-20:42",
			"title": "my future"
			},
			{
			"id":2,
			"release_date": "2022-03-19-20:43",
			"title": "life songer"
			},

			
		],
		"success": true
    }
    ```
	
#### GET /actor
* Get all actors

* Requires `get:actors` permission

* **Example Request:** `curl 'http://localhost:8080/actor'`

* **Expected Result:**
    ```json
	{
		"actors": [
			{
			"age": 45,
			"gender": "male",
			"id": 1,
			
			"name": "Javlon Turdialiyev"
			},
			{
			"age": 54,
			"gender": "female",
			"id": 2,
			
			"name": "Muxlisa Ne'matova"
			}
			
		],
		"success": true
	}
	```
	
#### POST /movie
* Creates a new movie.

* Requires `post:movie` permission

* Requires the title and release date.

* **Example Request:** (Create)
    ```bash
	curl --location --request POST 'http://localhost:5000/movie' \
		--header 'Content-Type: application/json'  \
		--header 'Authorization: Bearer <Your token>'\
		--data-raw '{
			"title": "Uzbekistan",
			"release_date": "2022-03-19-20:54"
		}'
    ```
    
* **Example Response:**
    ```bash
	{
		"success": true,
		'movie':[{
		'title':'Uzbekistan',
		'release_date':'2022-03-19-20:54'}
		]
	}
    ```

#### POST /actor
* Creates a new actor.

* Requires `post:actor` permission

* Requires the name, age and gender of the actor.

* **Example Request:** (Create)
    ```json
	curl --location --request POST 'http://localhost:5000/actor' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer <Your token>'\
		--data-raw '{
			"name": "Javlon Turdialiyev",
			"age": "18",
			"gender": "male"
        }'
    ```
    
* **Example Response:**
    ```json
	{
		"success": true,
		"actor":[{
			"name" : "Javlon Turdialiyev",
			"age":"18",
			"gender":"male"

		}

		]

    }
    ```

#### DELETE /movie/<int:movie_id>
* Deletes the movie with given id 

* Require `delete:movie` permission

* **Example Request:** `curl --request DELETE 'http://localhost:8080/movie/1' \	
		--header 'Authorization: Bearer <Your token>'\
`

* **Example Response:**
    ```json
	{
		"id": 1,
		"success": true
    }
    ```
    
#### DELETE /actor/<int:actor_id>
* Deletes the actor with given id 

* Require `delete:actor` permission

* **Example Request:** `curl --request DELETE 'http://localhost:5000/actors/1' \
--header 'Authorization: Bearer <Your token>'\`

* **Example Response:**
    ```json
	{
		"id": 1,
		"success": true
    }
    ```

#### PATCH /movies/<movie_id>
* Updates the movie where <movie_id> is the existing movie id

* Require `patch:movie` permission


* **Example Request:** 
	```json
    curl --location --request PATCH 'http://localhost:8080/movie/1' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer <Your token>'\
		--data-raw '{
			"title": "Hello"
        }'
  ```
  
* **Example Response:**
    ```json
	{
		"success": true, 
		"title":"Hello",
		"release_date":"2020-19-03-21:05"
    }
    ```
	
#### PATCH /actor/<actor_id>
* Updates the actor where <actor_id> is the existing actor id

* Require `patch:actor`

* **Example Request:** 
	```json
    curl --location --request PATCH 'http://localhost:5000/actors/1' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer <Your token>'\
		--data-raw '{
			"name": "Qamariddin Aqmirzayev"
        }'
  ```
  
* **Example Response:**
    ```json
	{
		"success": true, 
		"name":"Qamariddin Aqmirzayev",
		"age":18,
		"gender":"male"
		
	}
	```

	### Error Handling

Errors are returned as JSON objects in the following format:
```json
{
    "success": false, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal Server Error
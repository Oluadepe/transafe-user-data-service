# Transafe User Data Management service
This User Management Service is a RESTful API that handles user information and data.
It allows users to Create, Read, Update, and Delete their profiles, as well as manage their account settings and preferences.

## Functionality

The microservice provides the following functionality:
- [x] **User registration:** allows new users to create a profile with their basic information, such as name, email, and password.

- [x] **User profile management:** allows users to update their profile information, such as their name, address, phone number.

## Testing

To ensure the functionality and reliability of the microservice, it is recommended to perform the following types of testing.

- [x] **Unit tests:** we ensure that each component and function of the microservice works correctly in isolation, by mocking dependencies and input/output parameters.
- [x] **Integration tests:** we ensure that the microservice can interact with other services or systems, such as databases, messaging systems, or APIs, and produce the expected results.
- [x] **End-to-end tests:** we ensure that the microservice can handle user requests and responses correctly, by simulating user interactions and testing different scenarios and edge cases.

## How to Use

To use this User Management service,  please follow these steps:

- **1.** Clone the repository and install the dependencies:

```
terminal@terminal$ git clone https://github.com/rohteemie/transafe_user_data_service.git
terminal@terminal$ cd transafe_user_data_service
terminal@terminal$ pip3 install -r requirement.txt
```

- **2.** Configure the service settings:

In the .env file, you can set the environment variables for the service, such as the port number, the database connection string, and other options.

```bash
TRNSF_DB="database_name"
TRNSF_HOST="database_host"
TRNSF_HOST="database_user"
TRNSF_PWD="database_password"
USER_ROLE="user_role_string"
ADMIN_ROLE="admin_role_string"
JWT_SECRET_KEY="complex_jwt_secret_key"
JWT_ALLOWED_ISSUER="token_issuer"
COOKIE_NAME="cookie_name"
```

- **3.** Start the service:

```
terminal@terminal$ flask-app run
```

This will start the service on the specified port, and it will listen for incoming requests.

- **4.** Use the microservice API:
You can use a tool like Postman or cURL to send requests to the API endpoints and receive responses. The API endpoints follow the RESTful principles and use the HTTP methods and status codes to indicate the actions and results.
Authorization is done by cookie or including user token in the Authorization header. Here are some examples using cURL:

- `GET /api/users/:id`: retrieves the user profile with the specified ID.
```
terminal@terminal:~/transafe-user-data-service$ curl http://localhost:5000/api/v1/users/63a7abe1-910b-474a-9f21-6e51869ec6ce -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2M2E3YWJlMS05MTBiLTQ3NGEtOWYyMS02ZTUxODY5ZWM2Y2UiLCJpc3MiOiJUUkFOU0FGRSBUT0tFTiBJU1NVRVIiLCJyb2xlIjoidXNlciJ9.BDyOOnoyYpYhw4GirtN6gtJTNSYIsx3mOrL5XJv9Eho"

{
  "address": "Ajeku iya looje street",
  "created_at": "2023-04-04T15:05:20",
  "dob": {
    "day": 4,
    "month": 6,
    "year": 2023
  },
  "email": "ajiboyeadeleye080@gmail.com",
  "first_name": "Ajiboye",
  "gender": "Male",
  "id": "63a7abe1-910b-474a-9f21-6e51869ec6ce",
  "last_name": "Adeleye",
  "phone": "12345678910",
  "updated_at": "2023-04-07T00:19:20"
}

terminal@terminal:~/transafe-user-data-service$
````



- `GET /api/v1/users/me`: retrieves the user based on the current session.
    assuming `COOKIE_NAME="session"`
```
terminal@terminal:~/transafe-user-data-service$ curl http://localhost:5000/api/v1/users/me -b "session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2M2E3YWJlMS05MTBiLTQ3NGEtOWYyMS02ZTUxODY5ZWM2Y2UiLCJpc3MiOiJUUkFOU0FGRSBUT0tFTiBJU1NVRVIiLCJyb2xlIjoidXNlciJ9.BDyOOnoyYpYhw4GirtN6gtJTNSYIsx3mOrL5XJv9Eho"

{
  "address": "Ajeku iya looje street",
  "created_at": "2023-04-04T15:05:20",
  "dob": {
    "day": 4,
    "month": 6,
    "year": 2023
  },
  "email": "ajiboyeadeleye080@gmail.com",
  "first_name": "Ajiboye",
  "gender": "Male",
  "id": "63a7abe1-910b-474a-9f21-6e51869ec6ce",
  "last_name": "Adeleye",
  "phone": "12345678910",
  "updated_at": "2023-04-07T00:19:20"
}

terminal@terminal:~/transafe-user-data-service$
```

- `POST /api/users`: creates a new user profile with the specified information.

```
terminal@terminal:~/transafe-user-data-service$ curl -H "Content-Type: application/json" -X POST -d '{"first_name": "Pentagon", "last_name": "Daves", "address": "Block 234, Orland avenue, transafe estate.", "gender": "Male", "phone": "555234897", "email": "transafe@transafe.com", "dob_day": 4, "dob_month": 6, "dob_year": 2023}' http://localhost:5000/api/v1/users

{
  "message": "user created",
  "status": "success"
}

terminal@terminal:~/transafe-user-data-service$
```


- `PUT /api/users/:id`: updates the user profile with the specified ID and information.
```
terminal@terminal:~/transafe-user-data-service$ curl http://localhost:5000/api/v1/users/63a7abe1-910b-474a-9f21-6e51869ec6ce -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2M2E3YWJlMS05MTBiLTQ3NGEtOWYyMS02ZTUxODY5ZWM2Y2UiLCJpc3MiOiJUUkFOU0FGRSBUT0tFTiBJU1NVRVIiLCJyb2xlIjoidXNlciJ9.BDyOOnoyYpYhw4GirtN6gtJTNSYIsx3mOrL5XJv9Eho" -H "Content-Type: application/json" -X PUT -d '{"address": "my house address"}'

{
  "message": "user updated seccessfully",
  "status": "success"
}

terminal@terminal:~/transafe-user-data-service$
```
If attempts is made to change email, the request will be terminated and 409 error will be returned

```
terminal@terminal:~/transafe-user-data-service$ curl http://localhost:5000/api/v1/users/63a7abe1-910b-474a-9f21-6e51869ec6ce -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2M2E3YWJlMS05MTBiLTQ3NGEtOWYyMS02ZTUxODY5ZWM2Y2UiLCJpc3MiOiJUUkFOU0FGRSBUT0tFTiBJU1NVRVIiLCJyb2xlIjoidXNlciJ9.BDyOOnoyYpYhw4GirtN6gtJTNSYIsx3mOrL5XJv9Eho" -H "Content-Type: application/json" -X PUT -d '{"email": "ajiboyeadeleye080@gmail.com"}'

{
  "error": "email provided already in use"
}

terminal@terminal:~/transafe-user-data-service$
```

- `DELETE /api/users/:id`: deletes the user profile with the specified ID.
```
terminal@terminal:~/transafe-user-data-service$ curl http://localhost:5000/api/v1/users/63a7abe1-910b-474a-9f21-6e51869ec6ce -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2M2E3YWJlMS05MTBiLTQ3NGEtOWYyMS02ZTUxODY5ZWM2Y2UiLCJpc3MiOiJUUkFOU0FGRSBUT0tFTiBJU1NVRVIiLCJyb2xlIjoidXNlciJ9.BDyOOnoyYpYhw4GirtN6gtJTNSYIsx3mOrL5XJv9Eho" -X DELETE

{
  "message": "user deleted successfully",
  "status": "success"
}

terminal@terminal:~/transafe-user-data-service$
```

All the above request methods except for `POST` works same way with `api/v1/users/me` endpoint using user session for authorization.

## Future features:

- User data management: allows users to manage their data, such as documents, images, or other files, that are associated with their profile or account.
- User preferences: allows users to manage their account settings and preferences, such as language, timezone, or notification settings

## License

- **MIT LICENSE**
This service is licensed under the MIT License. See the LICENSE file for more information.

## Authors

<details>
	<summary>Owolabi Rotimi</summary>
	<ul>
	<li><a href="https://www.github.com/rohteemie">GitHub</a></li>
	<li><a href="https://www.linkedin.com/in/rohteemie">LinkedIn</a></li>
	<li><a href="https://www.twitter.com/rohteemie">Twitter</a></li>
	<li><a href="mailto:iamrotimiowolabi@gmail.com">Email</a></l>
	</ul>
</details>
<details>
        <summary>Ajiboye Adeleye</summary>
        <ul>
        <li><a href="https://www.github.com/Adeleye080">GitHub</a></li>
        <li><a href="https://www.linkedin.com/in/ajiboye-adeleye-b561a7211">LinkedIn</a></li>
        <li><a href="https://www.twitter.com/AdeleyeAjiboye">Twitter</a></li>
        <li><a href="mailto:ajiboyeadeleye080@gmail.com">Email</a></l>
        </ul>
</details>
<details>
        <summary>Olusegun Mayungbe</summary>
        <ul>
        <li><a href="https://www.github.com/Oluadepe">GitHub</a></li>
        <li><a href="https://www.linkedin.com/in/">LinkedIn</a></li>
        <li><a href="https://www.twitter.com/">Twitter</a></li>
        <li><a href="mailto:">Email</a></l>
        </ul>
</details>

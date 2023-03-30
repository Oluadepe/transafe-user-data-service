# Transafe User Data Management service
This User Management Service is a RESTful API that handles user information and data.
It allows users to Create, Read, Update, and Delete their profiles, as well as manage their account settings and preferences.

## Functionality
The microservice provides the following functionality:
- **User registration:** allows new users to create a profile with their basic information, such as name, email, and password.
- **User authentication:** provides authentication mechanisms, such as email/password, JWT tokens, or OAuth, to ensure that only authorized users can access their account information.
- **User profile management:** allows users to update their profile information, such as their name, email, address, phone number, and profile picture.
- **User data management:** allows users to manage their data, such as documents, images, or other files, that are associated with their profile or account.
- **User preferences:** allows users to manage their account settings and preferences, such as language, timezone, or notification settings.

## Testing
To ensure the functionality and reliability of the microservice, it is recommended to perform the following types of testing:
- **Unit tests:** we ensure that each component and function of the microservice works correctly in isolation, by mocking dependencies and input/output parameters.
- **Integration tests:** we ensure that the microservice can interact with other services or systems, such as databases, messaging systems, or APIs, and produce the expected results.
- **End-to-end tests:** we ensure that the microservice can handle user requests and responses correctly, by simulating user interactions and testing different scenarios and edge cases.

## How to Use
To use this User Management service,  please follow these steps:

- **1.** Clone the repository and install the dependencies:

`git clone https://github.com/rohteemie/transafe_user_data_service.git`

cd user-management-service

`pip3 install`


- **2.** Configure the service settings:

`source ENV/bin/activate`

`pip3 install -r requirements.txt`

In the .env file, you can set the environment variables for the service, such as the port number, the database connection string, the authentication provider, and other options.


- **3.** Start the service:

`flask-app run`

This will start the service on the specified port, and it will listen for incoming requests.

- **4.** Use the microservice API:

You can use the API endpoints provided by the service to manage user information and data. Here are some examples:

- POST /api/users: creates a new user profile with the specified information.

- POST /api/auth/login: authenticates the user with the specified credentials and returns an access token.

- GET /api/users/:id: retrieves the user profile with the specified ID.

- PUT /api/users/:id: updates the user profile with the specified ID and information.

- DELETE /api/users/:id: deletes the user profile with the specified ID.

You can use a tool like Postman or cURL to send requests to the API endpoints and receive responses. The API endpoints follow the RESTful principles and use the HTTP methods and status codes to indicate the actions and results

- **MIT LICENSE**
This service is licensed under the MIT License. See the LICENSE file for more information.

### AUTHORS
---
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

# Airbcar Backend API

## Endpoints
- **POST /users/api/login/**: Authenticate and get a JWT token.
  - Request: `{"username": "your_username", "password": "your_password"}`
  - Response: `{"refresh": "...", "access": "..."}`
- **GET /users/api/users/**: List all users.
  - Requires: `Authorization: Bearer <access_token>`
- **POST /users/api/users/**: Create a user.
  - Requires: `Authorization: Bearer <access_token>`
  - Request: `{"name": "Test", "email": "test@example.com"}`
- **GET /users/api/bookings/**: List all bookings.
  - Requires: `Authorization: Bearer <access_token>`
- **POST /users/api/bookings/**: Create a booking.
  - Requires: `Authorization: Bearer <access_token>`
  - Request: `{"user_id": 1, "car_id": 101}`

## Authentication
- Use the access token from `/login/` in the `Authorization` header: `Bearer <access_token>`.
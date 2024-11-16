# Pet Adoption API

## Overview

This project is a **Pet Adoption Web API** that allows users to manage pet information. It supports CRUD operations (Create, Read, Update, Delete) for pet records, enabling users to:

- Add new pets to the system
- View a list of available pets
- Update pet details
- Delete a pet from the system

The application uses **FastAPI** for the API, **SQLAlchemy** for database interaction, and **PostgreSQL** as the database. This project helps in managing pet adoption records efficiently.

## Features

- **Add a Pet**: Allows users to add new pets into the system.
- **List Pets**: Allows users to retrieve a list of all pets available for adoption.
- **Get Pet Details**: Allows users to retrieve details of a specific pet.
- **Update Pet**: Allows users to update the details of an existing pet.
- **Delete Pet**: Allows users to delete a pet record from the system.

## Technologies Used

- **FastAPI**: A fast and modern web framework for building APIs with Python.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database used to store pet adoption records.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server to run FastAPI.

## Installation

To set up the project on your local machine, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pet-adoption-api.git
cd pet-adoption-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root of the project and set the database URL:

```
DATABASE_URL=postgresql://username:password@localhost/dbname
```

Replace `username`, `password`, and `dbname` with your actual PostgreSQL credentials.

### 5. Run the application

To run the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will run on `http://localhost:8000`.

### 6. Create Database Tables

The tables will be automatically created when the application starts, as `Base.metadata.create_all(bind=engine)` is called in the `main.py` file.

## API Endpoints

### 1. **List All Pets**

**GET** `/pets`

Returns a list of all pets in the system.

**Response:**

```json
[
  {
    "id": 1,
    "name": "Max",
    "species": "Dog",
    "breed": "Indie",
    "age": "5years",
    "health_status": "Healthy",
    "location": "Hyderabad",
    "status": "available",
    "added_date": "2024-01-01"
  },
  ...
]
```

### 2. **Get Pet by ID**

**GET** `/pets/{pet_id}`

Retrieve details of a specific pet by its ID.

**Response:**

```json
{
  "id": 1,
  "name": "Max",
  "species": "Dog",
  "breed": "Indie",
  "age": "5years",
  "health_status": "Healthy",
  "location": "Hyderabad",
  "status": "available",
  "added_date": "2024-01-01"
}
```

### 3. **Add New Pet**

**POST** `/pets`

Add a new pet to the system.

**Request Body:**

```json
{
  "name": "Racxax",
  "species": "Cat",
  "breed": "Indie",
  "age": "5years",
  "health_status": "Healthy",
  "location": "Hyderabad",
  "status": "available",
  "added_date": "2024-01-01"
}
```

**Response:**

```json
{
  "id": 2,
  "name": "Racxax",
  "species": "Cat",
  "breed": "Indie",
  "age": "5years",
  "health_status": "Healthy",
  "location": "Hyderabad",
  "status": "available",
  "added_date": "2024-01-01"
}
```

### 4. **Update Pet Details**

**PUT** `/pets/{pet_id}`

Update an existing pet's details.

**Request Body:**

```json
{
  "name": "Racxax Updated",
  "age": "6years"
}
```

**Response:**

```json
{
  "id": 2,
  "name": "Racxax Updated",
  "species": "Cat",
  "breed": "Indie",
  "age": "6years",
  "health_status": "Healthy",
  "location": "Hyderabad",
  "status": "available",
  "added_date": "2024-01-01"
}
```

### 5. **Delete Pet**

**DELETE** `/pets/{pet_id}`

Delete a pet from the system.

**Response:**

```json
{
  "message": "Pet 2 Deleted Successfully"
}
```

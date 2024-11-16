'''This module is model of petshop'''

from pydantic import BaseModel, Field
from datetime import date

class Pet_request(BaseModel):
    "this describes the pet"
    name: str = Field(
        ...,
        description = "Name of the pet",
        example = "Max"
    )
    species: str = Field(
        ...,
        description = "Species of Pet eg. Dog, Cat, Birds etc",
        example = "Dog"
    )
    breed: str = Field(
        ...,
        description = "Breed of the Pet",
        example = "Indie"
    )
    age: str = Field(
        ...,
        description = "Age in years",
        example = "5years"
    )
    health_status: str = Field(
        ...,
        description = "Health condition of the pet",
        example = "Healthy"
    )
    location: str = Field(
        ...,
        description = "Location of the pet",
        example = "Hyderabad"
    )
    status: str = Field(
        ...,
        description = "Available or Unavailable",
        example = "available"
    )
    added_date: date = Field(
        ...,
        description="Date when the pet was listed",
        example="2024-01-01"
    )



class Pet_response(BaseModel):
    "this shows pet response"
    id: int = Field(
        ...,
        description = "id of pet",
        example = "1"
    )
    name: str = Field(
        ...,
        description = "Name of the pet",
        example = "Max"
    )
    species: str = Field(
        ...,
        description = "Species of Pet eg. Dog, Cat, Birds etc",
        example = "Dog"
    )
    breed: str = Field(
        ...,
        description = "Breed of the Pet",
        example = "Indie"
    )
    age: str = Field(
        ...,
        description = "Age in years",
        example = "5years"
    )
    health_status: str = Field(
        ...,
        description = "Health condition of the pet",
        example = "Healthy"
    )
    location: str = Field(
        ...,
        description = "Location of the pet",
        example = "Hyderabad"
    )
    status: str = Field(
        ...,
        description = "Available or Unavailable",
        example = "available"
    )
    added_date: date = Field(
        ...,
        description="Date when the pet was listed",
        example="2024-01-01"
    )
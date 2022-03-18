# Catastic Companions - Final API Project

Arica Conrad

BIT 465 - REST API Development

March 16, 2022

Final API Project

## Introduction

This is my final project for my BIT 465 - REST API Development class. Catastic Companions is an API for a fictitious local cat shelter and is only used internally. The API keeps track of all the cats the shelter has hosted, including the cats who were adopted. The shelter staff members can register a new account and log in to the system, where they are then able to view all the cats, edit the cats, and delete the cats.

## Project Requirements

### Overview

This project involves the creation of a mobile application with two major components: a backend service and a mobile/web application. Formal designs for each must be submitted, in writing, prior to beginning development. The backend service and mobile/web application must include, at a minimum, the features listed below.

The purpose of the application is to maintain a list of items along with some detail information. Possible sample implementations include a shopping list, to do list, bucket list, etc. If you are working on an application or you have an already made one that can satisfy the following requirements, you can use it for the project.

### Backend Services

- Shall use a proper JSON format for all data exchange with the mobile/web application.
- Shall use a DynamoDB/PostgreSQL/SQLite database to store any service data.
- Shall include each of the following data types at least once:
  - String (VARCHAR)
  - Date (DATETIME)
  - Decimal (FLOAT)
  - Integer (INTEGER)
  - Boolean (Bool)
- Shall provide, at a minimum, one GET, POST, UPDATE, and DELETE feature.

### Mobile/Web Application

- Shall provide a user registration page to create a new account.
- Shall provide a user login page for existing accounts.
- Shall provide at least one list view with the following features:
  - Add
  - Delete
  - Edit
- Shall provide at least one item detail view with the following features:
  - Edit/Save/Cancel
  - Delete

### Submission

The proper documentation must be submitted and approved before beginning development. The documentation for the backend services must include the API (see <https://openweathermap.org/current> for an example), sample JSON messages, common response/error codes, and a database schema. The documentations for the mobile/web application must include a web design workflow, wireframe page mockups, and a web design palette (colors, fonts, element styles).

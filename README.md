# **Backend Coding Assigment** by Felipe Moreira

### Project Overview

This project involves developing a backend application that manages GeoJSON data and provides an API for creating, retrieving, and filtering GeoFeatures. The backend uses Django and Django Rest Framework (DRF) to handle API requests and GeoDjango for geospatial data management. The goal of this project is to showcase the ability to handle geospatial data efficiently, create RESTful APIs, and integrate third-party services for GeoJSON data handling.

### Project Structure

- /api: Contains the main API logic for managing GeoFeatures.
  - views.py: Handles the API views.
  - serializers.py: Defines serializers for the GeoFeature model.
  - models.py: Contains the GeoFeature model with geospatial fields.
  - urls.py: Defines URL patterns for the API endpoints.
- load_geojson.py: A script to load GeoJSON data into the database.
- settings.py: Contains Django project settings, including database and installed apps configuration.

### Prerequisites

Before you start, make sure you have the following installed:

- Python 3.8+ (Recommended: Python 3.8 or later)
- Django 3.2+ (For compatibility with GeoDjango)
- PostGIS (To handle geospatial data in PostgreSQL)
- pip (Python package manager)

### Installation

1. Clone the repository

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/backend-coding-assignment.git
   cd backend-coding-assignment
   ```

2. Install dependencies

   Install the required packages from requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database

   This project uses PostgreSQL with PostGIS extension for handling geospatial data. Ensure you have PostgreSQL and PostGIS installed, then configure the database.

   - Create the database:

   ```bash
   createdb geo_backend
   ```

   - Enable PostGIS:

   ```bash
   psql -d geo_backend -c "CREATE EXTENSION postgis;"
   ```

   - Configure your DATABASES setting in settings.py to use the geo_backend database with PostGIS enabled.

4. Apply database migrations

   Run the migrations to create the necessary database tables:

   ```bash
    python manage.py migrate
   ```

5. Load provided GeoJSON data

   Run the script load_geojson.py:

   ```bash
    python load_geojson.py
   ```

### Running the Project

Once you’ve set up the project and database, you can run the Django development server:

1. Start the server

   ```bash
    python manage.py runserver
   ```

2. Access the API

- The API will be available at http://127.0.0.1:8000/.
- The API includes endpoints for creating, retrieving, and filtering GeoFeature objects:
  GET /api/features/: List all GeoFeatures.
  POST /api/features/: Create a new GeoFeature by providing a GeoJSON payload.
  GET /api/features/{id}/: Retrieve a specific GeoFeature by ID.
  GET /api/features/bbox/: Filter features within a bounding box.

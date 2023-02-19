# Toohla REST API

### What is this?

This is a RESTful service when a user inputs their origin and destination into the client which returns the carbon emissions, distance, and the time of travel for each mode of transportation:

- Driving
- Walking
- Taking the train

### Design

- Origin and destination incomes as latlng
- Pass the data to Google directions API, to get `distance` and `time` for each transport mode
- Calculate carbon emissions based on the `distance` and the existing emissions data(assume it's fetched by a scheduled worker, for example, running nightly)
- Compose a response and send to the client
- Another endpoint in the same procedure but with origin and destination as address, instead of latlng

### Run

- Create dot env by `cp .env.example .env` and configure with proper values for production
- Run by `docker compose up -d`

### Test

### Development

- Create a virtualenv in your favorite way
- Install dependencies by `pip install -r requirements.txt`
- Install git pre-commit hooks by `pre-commit install`
- Run the dev server by `python manage.py runserver`

### API documentation

Automatic swagger API documentation is configured, and you can find it by browsing `BASE_URL/swagger` in `development`.

In production, run `python manage.py collectstatic` for generating API docs static files, and configure the production web server(nginx or caddy etc) to serve the static files in a desired path.

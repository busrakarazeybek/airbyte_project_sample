# Airbyte Data Integration Project

## Overview
This project demonstrates how to use Airbyte to integrate data from a MySQL source into a PostgreSQL destination. The connectors are custom built using Airbyte's CDK.

## Setup
1. Clone the repository and navigate to the project directory.
2. Set up the environment variables by renaming `.env.example` to `.env` and filling in the appropriate values.
3. Run the Docker containers:

## Connectors
### MySQL Source
The source connector reads data from a MySQL database. Configuration is defined in `connectors/source_mysql/config.json`.

### PostgreSQL Destination
The destination connector writes data to a PostgreSQL database. Configuration is defined in `connectors/destination_postgres/config.json`.

## Running the Project
1. Start the Airbyte server and webapp using Docker.
2. Access the Airbyte web interface at `http://localhost:8000`.
3. Configure the source and destination connectors and set up a sync schedule.
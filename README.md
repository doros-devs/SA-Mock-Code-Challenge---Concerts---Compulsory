Concert Management System

Overview

This project simulates a concert management system using raw SQL queries for database interactions. It includes three primary entities: Band, Venue, and Concert. A band can perform at multiple venues, and a venue can host multiple concerts. This system provides functionalities to manage bands, venues, and concerts, along with methods to retrieve and analyze concert data, such as determining the band with the most performances, and checking if a concert is in a band’s hometown.

Features

	•	Band Management: Create and manage band data.
	•	Venue Management: Create and manage venue data.
	•	Concert Management: Record concerts with details including date, band, and venue.
	•	Data Retrieval: Retrieve data on bands, venues, and concerts, including which bands played where, how many concerts each band has performed, and more.
	•	Aggregate Data: Find the band that has performed the most concerts and venues that have hosted the most performances.

Project Structure

|-- concerts.db        # SQLite database file
|-- schema.sql         # SQL file containing table creation scripts
|-- concert.py         # Python file containing Concert class and methods
|-- band.py            # Python file containing Band class and methods
|-- venue.py           # Python file containing Venue class and methods
|-- main.py            # Python file to interactively test the system with user inputs
|-- README.md          # Project documentation

Database Schema

	•	bands Table
	•	id: Integer (Primary Key)
	•	name: String
	•	hometown: String
	•	venues Table
	•	id: Integer (Primary Key)
	•	title: String
	•	city: String
	•	concerts Table
	•	id: Integer (Primary Key)
	•	band_id: Integer (Foreign Key referencing bands(id))
	•	venue_id: Integer (Foreign Key referencing venues(id))
	•	date: String

Requirements

	•	Python 3.x
	•	SQLite3 or PostgreSQL (depending on your environment)
	•	Required Python modules:
	•	sqlite3
	•	psycopg2 (for PostgreSQL if used)

Setup Instructions

1. Clone the Repository
    git clone https://github.com/your-username/concert-management.git
    cd concert-management

2. Set Up Virtual Environment (Optional but recommended)

   Create a virtual environment:
        python -m venv venv

   Activate the virtual environment:

	•	On macOS/Linux:
        source venv/bin/activate

    .  On Windows:
        .\venv\Scripts\activate

3. Install Dependencies

For SQLite3, no additional installation is required, as it’s bundled with Python.

For PostgreSQL, install psycopg2:
    pip install psycopg2

4. Set Up Database

Run the SQL schema to create the database tables: sqlite3 concerts.db < schema.sql

5. Add Sample Data (Optional)

You can insert some sample data into the tables for testing purposes by executing INSERT SQL queries in your database.

6. Running the Application

Run the interactive main.py to test and manage the concert system:
    python main.py

7. Testing Methods

Use the interactive command-line interface to:

	•	Add a new band
	•	Add a new venue
	•	Create a new concert with a band and a venue
	•	Retrieve concerts and performance data for bands and venues
	•	Analyze the data by calculating the most frequent performers

Example Usage

Welcome to the Concert Management System

1. Add a new band
2. Add a new venue
3. Record a concert
4. List all concerts for a band
5. List all concerts for a venue
6. Get all bands that have played at a venue
7. Check if a concert is a hometown show
8. Exit

Example workflow:

	1.	Add bands like “Coldplay” from “London” or “The Beatles” from “Liverpool.”
	2.	Add venues like “O2 Arena” in “London” or “Madison Square Garden” in “New York.”
	3.	Record concerts like “Coldplay” performing at “O2 Arena” on “2024-10-20.”
	4.	Retrieve data like all concerts by “Coldplay” or all bands that performed at “Madison Square Garden.”

Code Explanation

Band Class

The Band class represents a music band, and includes methods to retrieve concerts the band has performed, venues where the band has played, and methods for creating new concerts.

Venue Class

The Venue class represents a concert venue and includes methods to retrieve concerts held at the venue and bands that have played there.

Concert Class

The Concert class represents a specific concert that took place at a venue, performed by a band on a specific date. The class includes methods to retrieve associated bands and venues.

SQL Queries

All methods in the classes use raw SQL queries to interact with the database, such as creating new records, retrieving records, performing joins, and calculating aggregates like the band with the most performances.

Contributing

If you’d like to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to include tests for any new features.

License

This project is licensed under the MIT License.

This README provides a general overview of your project, its features, and how to set it up and run it. Modify it as necessary to fit your specific requirements.


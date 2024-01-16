# Book Catalog
<img src="https://github.com/denisepostl/BookGUI/blob/main/static/screen.png">

# Instructions

## Transform into JSON

In the `transform.py` file, you'll find the code to import data from a CSV file and export its contents into a JSON file.

````
python transform.py
````

## Start the Container
Before running the application, it is essential to start the container for persistently saving data in a PostgreSQL database. Execute the following command to launch the PostgreSQL container:

```bash
docker-compose up -d
```
This command initiates a PostgreSQL database container in detached mode.

## Start the Application
To launch the application, run the following command. The main application is contained within this script.

``bash
python app.py
```

## Verify Database Creation

To check if the database has been successfully created, follow these steps:

List all containers:

```bash
docker ps
```

Identify the correct container and access its bash shell:

```bash
docker exec -it [CONTAINER_ID] bash
```
Replace [CONTAINER_ID] with the actual container ID.

Connect to PostgreSQL:
```bash
psql -U postgres -d postgres
```

Use <bold>\dt</bold> to display all tables.

Check for entries in the books table, for example:

```bash
SELECT * FROM books;
```
<img src="https://github.com/denisepostl/BookGUI/blob/main/static/check.png">





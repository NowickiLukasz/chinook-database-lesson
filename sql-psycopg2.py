import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build cursor object of the database
cursor = connection.cursor()

# Quesry 1 - select all records  from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Selects name from the Artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" form the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the album withi "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen", from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - Select all tracks where composer is "Metallica" from "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Metallica"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (one)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)

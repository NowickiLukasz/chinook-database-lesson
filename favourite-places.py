from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create a class based model for "Places" table
class Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    capital = Column(String)

# insted of connecting to the database directly, we will as for a session
# create a new instance of sessionmakeer, then point to our engine (the db)


Session = sessionmaker(db)


# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declaritive_base subclass
base.metadata.create_all(db)


# Creating records on our "Places" table
belgium = Places(
    country="Belgium",
    capital="Brussels"
)


czechia = Places(
    country="Czech-Republic",
    capital="Prague"
)

ireland = Places(
    country="Ireland",
    capital="Bray"
)

# Add each instance to the DB
# session.add(belgium)
# session.add(czechia)
# session.add(ireland)


# Commit our session to the DB
# session.commit()


# Query database to find country 
countries = session.query(Places)
for place in countries:
    print(
        place.country,
        place.capital,
        sep=" | "
    )
    

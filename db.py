from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib

password = "Postgresql@678"
encoded_password = urllib.parse.quote_plus(password)

# Replace the placeholder in the db_url with the actual password using string formatting
db_url = f"postgresql://postgres:{encoded_password}@localhost/DATA1"

# Create an SQLAlchemy engine
engine = create_engine(db_url)

Base = declarative_base()

class SampleModel(Base):
    __tablename__ = "sample_table"

    id = Column(Integer, Sequence("sample_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_data = SampleModel(name="John Doe", age=30)
session.add(new_data)
session.commit()

result = session.query(SampleModel).filter_by(name="John Doe").first()
if result:
    print(f"ID: {result.id}, Name: {result.name}, Age: {result.age}")
else:
    print("No data found for 'John Doe'")

# Close the session
session.close()

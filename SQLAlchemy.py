from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine('sqlite:///Assignement.db', echo = True)
Base = declarative_base()
 
class Books(Base):
   __tablename__ = 'Books'
   
   id = Column(Integer, primary_key = True)
   title = Column(String)
   year = Column(Integer)
 
Base.metadata.create_all(engine)
 
from sqlalchemy.orm import sessionmaker
 
Session = sessionmaker(bind = engine)
session = Session()
 
session.add_all([
   Books(title='StrÄƒinul', year='1942'), 
   Books(title='Procesul',year='1927'), 
   Books(title='Micul Print',year='1925'),
   Books(title='Razboiul Lumilor',year='1898')]
)
 
session.commit()
 
result = session.query(Books).all()
 
for row in result:
   print ("Title: ",row.title, "Year:",row.year)
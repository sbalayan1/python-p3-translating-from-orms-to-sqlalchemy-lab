from sqlalchemy import create_engine
from models import Dog

engine = create_engine('sqlite:///:memory:')
def create_table(base):
    pass
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    pass
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, row):
    pass
    # print(session.query(Dog).filter(Dog.id == row.id).first())
    # print(Dog(name=row.name, breed=row.breed))

    #the Dog() instance creation works and passes the test but instead of pulling an instance from the session, it creates a new instance. 
    return session.query(Dog).filter(Dog.id == row.id).first()
    
def get_all(session):
    pass
    # query = session.query(Dog)
    return [dog for dog in session.query(Dog)]
    

def find_by_name(session, name):
    pass
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    pass
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    pass
    return session.query(Dog).filter(
        Dog.name == name,
        Dog.breed == breed
    )

def update_breed(session, dog, breed):
    pass
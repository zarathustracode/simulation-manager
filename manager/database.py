from click import echo
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sqlite.db', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    usersimulation = relationship("Simulation", backref='users')
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

class Model(Base):
    __tablename__= "models"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    memorycost = Column(Integer)
    performancecost = Column(Float)
    modelsimulation = relationship("Simulation", backref='models')

class Simulation(Base):
    __tablename__= "simulations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    userid = Column(Integer, ForeignKey("users.id"), nullable=False)
    modelid = Column(Integer, ForeignKey("models.id"), nullable=False)
    starttime = DateTime()
    endtime = DateTime()


Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
linear_model = Model(name='linear model', memorycost=1000, performancecost=12.123)

Session = sessionmaker(bind=engine)

session = Session()

session.add(ed_user)
session.add(linear_model)

first_simulation = Simulation(userid=ed_user.id, modelid=linear_model.id)
session.flush()

session.add(first_simulation)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])




session.commit()




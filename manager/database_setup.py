from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = 'sqlite:///sqlite.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
SessionLocal = sessionmaker(bind=engine, future=True)

engine = create_engine('sqlite:///sqlite.db', echo=True)

Base = declarative_base()

def get_db_session():
  db_session = SessionLocal()
  try:
    yield db_session
  finally:
    db_session.close()


# ed_user = User(name='ed', fullname='Ed Jones', email='ed@gmail', nickname='edsnickname')
# linear_model = Model(name='linear model', memorycost=1000, performancecost=12.123)

# session = get_db_session()

# session.add(ed_user)
# session.add(linear_model)
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', email='wendy@gmail', nickname='windy'),
#     User(name='mary', fullname='Mary Contrary', email='mary@gmail', nickname='mary'),
#     User(name='fred', fullname='Fred Flintstone', email='fred@gmail', nickname='freddy'),
#     Model(name='convolutional model', memorycost=2000, performancecost=9.0),
#     Model(name='recurrent', memorycost=10000, performancecost=20.1),
#     Model(name='feed-forward model', memorycost=1500, performancecost=15.3)])

# session.flush()

# first_simulation = Simulation(userid=ed_user.id, modelid=linear_model.id)

# session.add(first_simulation)
# session.add_all(
#     [Simulation(userid=1, modelid=2),
#     Simulation(userid=2, modelid=3),
#     Simulation(userid=1, modelid=1)]
# )



# session.flush()
# session.commit()


# def test_basic_innerjoin():

#     usr = aliased(User)
#     sim = aliased(Simulation)
#     mod = aliased(Model)

#     joinquery = select(usr.fullname).join(sim, sim.userid==usr.id).distinct()

#     result = session.execute(joinquery).fetchone()

#     assert result[0] == 'Ed Jones'

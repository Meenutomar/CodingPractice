from sqlmodel import create_engine, Session

password = 'Mahadev%4006'
DATABASE_URL = f"mysql+pymysql://root:{password}@localhost/scenic"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session


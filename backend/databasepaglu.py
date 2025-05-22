from sqlmodel import create_engine, Session

password = '123456'
#DATABASE_URL = f"mysql+pymysql://root:{password}@localhost/postgres"
DATABASE_URL = f"postgresql+psycopg2://postgres:{password}@localhost/postgres"


engine = create_engine(DATABASE_URL, echo=True)

def get_session_pagli():
    with Session(engine) as session:
        yield session


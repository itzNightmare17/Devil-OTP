from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URI = "postgresql://samqtzsm:A6bGtfO0q12nORvPhlNqCob0BPKu7Ftd@balarama.db.elephantsql.com/samqtzsm"

def start() -> scoped_session:
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    print(str(e))

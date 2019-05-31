from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cricket_db.models import Base
from cricket_db.cricsheet_xml_reader import CricsheetXMLReader

if __name__ == '__main__':
    engine = create_engine('sqlite:///cricsheet.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    reader = CricsheetXMLReader()
    objects = reader.get_objects_from_directory('data')
    session.bulk_save_objects(objects)
    session.commit()
    session.close()

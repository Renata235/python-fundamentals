from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        usuario = Usuario(id=1, nome='Alan Kay')
        session.add(usuario)
        session.commit()
        print "Registro inserido"
    except Exception as e:
        session.rollback()
        print "Falhou ao inserir"
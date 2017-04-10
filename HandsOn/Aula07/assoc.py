from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///dep.db')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Analistas(Base):
    __tablename__ = 'analistas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    tokens = relationship("Tokens")


class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer, primary_key=True)
    endereco = Column(String)


class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    analista_id = Column(Integer, ForeignKey('analistas.id'))
    servidor_id = Column(Integer, ForeignKey('servidores.id'))
    token = Column(String)
    servidor = relationship('Servidores')
    analista = relationship('Analistas')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        analista = Analistas(id=1, nome='Andre Tanenbaum')
        servidor = Servidores(id=1, endereco='192.168.0.2')
        token = Tokens(id=1, token='xpto123')

        token.servidor = servidor
        analista.tokens.append(token)

        session.add(analista)
        session.add(token)
        session.add(servidor)

        session.commit()
    except Exception as e:
        print e
        session.rollback()

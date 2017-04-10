from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///assoc2.db')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

association_table = Table(
    'analistas_servidores',
    Base.metadata,
    Column('analistas_id', Integer, ForeignKey('analistas.id')),
    Column('servidores_id', Integer, ForeignKey('servidores.id')),
)


class Analistas(Base):
    __tablename__ = 'analistas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    servidores = relationship('Servidores', secondary=association_table)


class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer, primary_key=True)
    endereco = Column(String)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        analista = Analistas(id=1, nome='Andre Tanenbaum')
        session.add(analista)

        servidor1 = Servidores(id=1, endereco='192.168.0.2')
        servidor2 = Servidores(id=2, endereco='192.168.0.3')
        analista.servidores.append(servidor1)
        analista.servidores.append(servidor2)

        session.add(servidor1)
        session.add(servidor2)
        session.commit()
    except Exception as e:
        session.rollback()
        print e

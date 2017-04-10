from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///dep.db')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    # 1 to N
    dependentes = relationship('Dependentes')


class Dependentes(Base):
    __tablename__ = 'dependentes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    # N to 1
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'))

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    try:
        funcionario = Funcionario(id=1, nome='Joaquim da Silva')
        session.add(funcionario)
        dependente1 = Dependentes(id=1, nome="Joaozinho")
        dependente2 = Dependentes(id=2, nome="Mariazinha")

        funcionario.dependentes.append(dependente1)
        funcionario.dependentes.append(dependente2)

        session.add(dependente1)
        session.add(dependente2)
        session.commit()
    except Exception as e:
        print e
        session.rollback()

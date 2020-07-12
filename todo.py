from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date


#Conectar a la base de datos
engine = create_engine( 'mysql+pymysql://root:oscar@localhost/estudiantes' )
#engine = create_engine('sqlite:///cursos.db', echo=True)
Base = declarative_base()

class Asistencia(Base):
    __tablename__='Asistencia'
    id_profesor = Column(Integer, primary_key=True)
    id_curso = Column(Integer)
    id_materia = Column(Integer)
    id_alumno = Column(Integer)

class curso(Base):
    __tablename__='Curso'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(140))

class Profesor(Base):
    __tablename__='Profesor'
    id_profesor = Column(Integer, primary_key=True)
    Nombre_comp = Column(String(140))
    Cedula = Column(String(8))
    Celular = Column(Integer)

class Alumno(Base):
    __tablename__='Alumno'
    id_alumno = Column(Integer, primary_key=True)
    Nombre_comp = Column(String(140))
    Cedula = Column(String(8))

class Materia(Base):
    __tablename__='Materia'
    id_materia = Column(Integer, primary_key=True)
    id_profesor = Column(Integer)    


    
Sesion = sessionmaker(bind=engine)

sesion = Sesion()



if __name__ == '__main__':
    Base.metadata.create_all(engine)
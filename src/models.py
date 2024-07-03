from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///blog_starwars.db')

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    fecha_creacion = Column(String(20), nullable=False)
    favoritos = relationship('Favoritos', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500))
    clima = Column(String(100))
    terreno = Column(String(100))
    favoritos = relationship('Favoritos', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(100))
    genero = Column(String(50))
    descripcion = Column(String(500))
    favoritos = relationship('Favoritos', back_populates='personaje')

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    id_planeta = Column(Integer, ForeignKey('planetas.id'))
    id_personaje = Column(Integer, ForeignKey('personajes.id'))
    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')

if __name__ == '__main__':
    Base.metadata.create_all(engine)

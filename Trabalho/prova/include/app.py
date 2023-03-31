from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///jogos.db')
Base = declarative_base()

class Jogo(Base):
    __tablename__ = 'jogos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    plataforma = Column(String)
    preco = Column(String)
    quantidade = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

jogos = [
    {"nome": "DEAD SPACE REMAKE", "plataforma": "PS5", "preco": 350, "quantidade": 10},
    {"nome": "FORSPOKEN", "plataforma": "PC", "preco": 299, "quantidade": 8},
    {"nome": "DEAD ISLAND 2", "plataforma": "PS5", "preco": 350, "quantidade": 10},
    {"nome": "HOGWARTS LEGACY", "plataforma": "PC", "preco": 219, "quantidade": 7},
    {"nome": "WILD HEARTS", "plataforma": "XBox Series", "preco": 350, "quantidade": 7},
    {"nome": "RESIDENT EVIL 4", "plataforma": "PS5", "preco": 289, "quantidade": 10},
    {"nome": "THE LEGEND OF ZELDA: TEARS OF THE KINGDOM", "plataforma": "Switch", "preco": 350, "quantidade":10}
]

for jogo in jogos:
    cd_gta = Jogo(**jogo)
    session.add(cd_gta)

session.commit()

jogos = session.query(Jogo).all()
print(jogos) #assim ele me retorna o espaço de armazenamento.

for jogo in jogos:
    print(f'Nome: {jogo.nome}')
    print(f'Plataforma: {jogo.plataforma}')
    print(f'Preço: R${jogo.preco}')
    print(f'Quantidade: {jogo.quantidade}')
    print('')
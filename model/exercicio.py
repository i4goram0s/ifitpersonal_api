from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from typing import Union

from  model import Base


class Exercicio(Base):
    __tablename__ = 'exercicio'

    id = Column("pk_exercicio", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    link = Column(String(300))
    descricao = Column(String(300))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, link:str, descricao:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um exercicio

        Arguments:
            nome: nome do exercicio.
            link: link que se espera comprar daquele exercicio
            descricao: descricao esperado para o exercicio
            data_insercao: data de quando o exercicio foi inserido à base
        """
        self.nome = nome
        self.link = link
        self.descricao = descricao

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao



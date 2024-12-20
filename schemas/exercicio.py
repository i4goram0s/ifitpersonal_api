from pydantic import BaseModel
from typing import Optional, List
from model.exercicio import Exercicio


class ExercicioSchema(BaseModel):
    """ Define como um novo exercicio a ser inserido deve ser representado
    """
    nome: str = "back squat"
    link: str = "https://www.youtube.com/watch?v=ultWZbUMPL8"
    descricao: str = "lorem ipsum"


class ExercicioBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do exercicio.
    """
    nome: str = "back squat"


class ListagemExerciciosSchema(BaseModel):
    """ Definição da listagem de exercícios.
    """
    exercicios:List[ExercicioSchema]


def apresenta_exercicios(exercicios: List[Exercicio]):
    """ Retorna uma representação do exercicio seguindo o schema definido em
        exercicioViewSchema.
    """
    result = []
    for exercicio in exercicios:
        result.append({
            "nome": exercicio.nome,
            "link": exercicio.link,
            "descricao": exercicio.descricao
        })

    return {"exercicios": result}


class ExercicioViewSchema(BaseModel):
    """ Definição de retorno de um único exercício
    """
    id: int = 1
    nome: str = "Back Squat"
    link: str = "https://www.youtube.com/watch?v=ultWZbUMPL8"
    descricao: str = "lorem ipsum"


class ExercicioDelSchema(BaseModel):
    """ Definição do retorno após a exclusão de um exercicio
    """
    mesage: str
    nome: str

def apresenta_exercicio(exercicio: Exercicio):
    """ Retorno dos dados do exercicio
    """
    return {
        "id": exercicio.id,
        "nome": exercicio.nome,
        "link": exercicio.link,
        "descricao": exercicio.descricao
    }

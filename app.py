from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Exercicio
from schemas import *
from flask_cors import CORS

info = Info(title="IFitPersonal API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Lista das rotas básicas para inserção. listagem e exclusão de Exercicios do projeto IFitPersonal")
exercicio_tag = Tag(name="Exercicio", description="Adição, visualização e remoção de exercicios da base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/exercicio', tags=[exercicio_tag],
          responses={"200": ExercicioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_exercicio(form: ExercicioSchema):
    """Adiciona um novo exercicio à base de dados

    Retorna as informações do exercício adicionado! 
    """
    exercicio = Exercicio(
        nome=form.nome,
        link=form.link,
        descricao=form.descricao)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando exercicio
        session.add(exercicio)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_exercicio(exercicio), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Exercicio de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/\n" + str(e)
        return {"mesage": error_msg}, 400


@app.get('/exercicios', tags=[exercicio_tag],
         responses={"200": ListagemExerciciosSchema, "404": ErrorSchema})
def get_exercicios():
    """Faz a busca por todos os Exercicios cadastrados

    Retorna uma  listagem de exercicios já cadsatrados na base.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    exercicios = session.query(Exercicio).all()

    if not exercicios:
        # se não há exercicios cadastrados
        return {"exercicios": []}, 200
    else:
        # retorna a representação de exercicio
        print(exercicios)
        return apresenta_exercicios(exercicios), 200


@app.get('/exercicio', tags=[exercicio_tag],
         responses={"200": ExercicioViewSchema, "404": ErrorSchema})
def get_exercicio(query: ExercicioBuscaSchema):
    """Faz a busca por um exercicio a partir do id(nome) do exercicio

    Retorna um exercicíco com base a partir do nome buscado.
    """
    exercicio_id = query.nome
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    exercicio = session.query(Exercicio).filter(Exercicio.id == exercicio_id).first()

    if not exercicio:
        # se o exercicio não foi encontrado
        error_msg = "Exercicio não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação de exercicio
        return apresenta_exercicio(exercicio), 200


@app.delete('/exercicio', tags=[exercicio_tag],
            responses={"200": ExercicioDelSchema, "404": ErrorSchema})
def del_exercicio(query: ExercicioBuscaSchema):
    """Deleta um Exercicio a partir do nome de exercicio informado

    Retorna uma mensagem de confirmação da remoção.
    """
    exercicio_nome = unquote(unquote(query.nome))
    print(exercicio_nome)
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Exercicio).filter(Exercicio.nome == exercicio_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Exercicio removido", "id": exercicio_nome}
    else:
        # se o exercicio não foi encontrado
        error_msg = "Exercicio não encontrado na base :/"
        return {"mesage": error_msg}, 404


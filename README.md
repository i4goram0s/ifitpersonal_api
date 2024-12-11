# API IFit Personal

Este projeto disponibiliza rotas básicas de um app para gestão de treinos personalizados,
a fim de facilitar a montagem de treinos por profissionais da Ed. Física e compartilhr com seus respectivos alunos.

Inicialmente o projeto disponibiliza apenas rotas de cadastro, listagem e exclusão de Exercícios, armazenando na base de dados 
o nome do exercício, a descrição do mesmo, limitada a 300 caracteres e o link do vídeo de demonstração no youtube.

À medida que o projeto evoluir, a docuementação será atualizada em paralelo.



---
## Como executar 


Favor ao clonar repositório, acessar o diretório raiz do projeto pelo terminal e executar os seguintes comandos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

O comando acima instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

Acesse [http://localhost:5000/openapi/swagger](http://localhost:5000/openapi/swagger) para execução das rotas.

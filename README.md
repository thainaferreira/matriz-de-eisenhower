# Matriz de Eisenhower

Aplicação feita para ajudar a definir as prioridades se baseando na [Matriz de Eisenhower](https://www.dropbox.com/pt_BR/business/resources/eisenhower-matrix).

<br>

## Como instalar e rodar? 🚀

Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

    #Este passo é para baixar o projeto
    git clone https://github.com/thainaferreira/matriz-de-eisenhower.git

Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

    #Entrar na pasta
    cd matriz-de-eisenhower

    #Criar um ambiente virtual
    python -m venv venv

    #Entrar no ambiente virtual
    source venv/bin/activate

Então, para instalar as dependências, basta:

    pip install -r requirements.txt

Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:

    flask db upgrade

Para rodar, basta digitar o seguinte, no terminal:

    flask run

E o sistema estará rodando em `http://127.0.0.1:5000/`

## Utilização 🖥️

Para utilizar este sistema, é necessário utilizar um API Client, como o [Insomnia](https://insomnia.rest/download)

### Rotas

### ![POST](https://i.imgur.com/Qhk9miC.png) CREATE CATEGORY

```
/category
```

Rota responsavel de fazer a inserção dos dados na tabela categories.

`RESPONSE STATUS -> HTTP 201 (created)`

<img width="100%" src='https://files-kenzie-academy-brasil.s3.amazonaws.com/q3/sprint5/entrega-matriz-eisenhower/image-3.png' alt='exemplo requisição post para criação de categoria'/>

#### ![PATCH](https://i.imgur.com/An2Czkl.png) UPDATE CATEGORY BY ID

```
/category/<id>
```

Rota responsável de fazer a atualização dos dados na tabela categories.

`RESPONSE STATUS -> HTTP 200 (ok)`

<img width="100%" src='https://files-kenzie-academy-brasil.s3.amazonaws.com/q3/sprint5/entrega-matriz-eisenhower/image-5.png' alt='exemplo requisição patch para atualizar categoria'/>

#### ![DELETE](https://i.imgur.com/ZMSQTeK.png) DELETE CATEGORY BY ID

```
/category/<id>
```

Rota responsável de fazer a deleção dos dados na tabela categories.

`RESPONSE STATUS -> HTTP 204 (No content)`

<img width="100%" src='https://files-kenzie-academy-brasil.s3.amazonaws.com/q3/sprint5/entrega-matriz-eisenhower/image-7.png' alt='exemplo requisição delete'/>

#### ![POST](https://i.imgur.com/Qhk9miC.png) CREATE TASK

```
/task
```

Esta rota é responsável por fazer a inserção dos dados na tabela tasks:

`RESPONSE STATUS -> HTTP 201 (created)`

<img width="100%" src='https://files-kenzie-academy-brasil.s3.amazonaws.com/q3/sprint5/entrega-matriz-eisenhower/image-9.png' alt='exemplo requisição post para criar uma task'/>

#### ![PATCH](https://i.imgur.com/An2Czkl.png) UPDATE TASK BY ID

```
/task/<id>
```

Rota responsável de fazer a atualização dos dados na tabela tasks.

`RESPONSE STATUS -> HTTP 200 (ok)`

<img width="100%" src='https://files-kenzie-academy-brasil.s3.amazonaws.com/q3/sprint5/entrega-matriz-eisenhower/image-12.png' alt='exemplo requisição patch para atualizar task'/>

#### ![DELETE](https://i.imgur.com/ZMSQTeK.png) DELETE TASK BY ID

```
/task/<id>
```

Rota responsável de fazer a deleção dos dados na tabela tasks.

`RESPONSE STATUS -> HTTP 204 (No content)`

<img width="100%" src='https://files-kenzie-academy-brasil.s3.amazonaws.com/q3/sprint5/entrega-matriz-eisenhower/image-14.png' alt='exemplo requisição delete'/>

#### ![GET](https://i.imgur.com/zH6h6cZ.png) GET ALL CATEGORIES

```
/
```

Rota responsável de obter todos as categorias com suas respectivas tasks.

`RESPONSE STATUS -> HTTP 200 (ok)`

<img width="100%" src='https://files-kenzie-academy-brasil.s3.amazonaws.com/q3/sprint5/entrega-matriz-eisenhower/image-16.png' alt='exemplo requisição get'/>

## Tecnologias utilizadas 📱

- Flask
- SQLAlchemy
- Migrate
- Blueprints
- Flask Factory

## Licence

MIT

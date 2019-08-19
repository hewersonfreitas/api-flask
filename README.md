# API Flask, React, Mongo DB

CRUD utilizando Flask para API Backend, e algumas de suas ferramentas

- Flask
- flask_cors
- pymongo
- bson

## Como executar o projeto

Vamos executar os comandos abaixo partindo que esteja no diretório raiz onde fez o clone do projeto.

```sh
cd backend
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

Acesse o projeto através do endereço:
```sh
http://localhost:5000
```

## CRUD

### Create

Para criar uma entrada no banco iremos utilizar o path abaixo em algum aplicativo como Postman ou Insomnia

```sh
http://localhost:5000/api/add/store
```

Via metódo POST, passaremos o corpo do objeto json a ser inserido
```json
{
	"code":"1",
	"name":"Loja 1",
	"city": "Fortaleza",
	"state": "CE"
}
```

Exemplo:

![](./images/add-store.png)

### Listar Items

1. Listar todos
   Para listar todos os itens acessamos via metodo GET o endereço abaixo:

```sh
http://localhost:5000/api/list/all
```

Será retornado os valores existentes
```json
[
  {
    "name": "Loja 1",
    "_id": {
      "$oid": "5d595929a5b5a9067e8e5a50"
    },
    "state": "CE",
    "city": "Fortaleza",
    "code": 1
  }
]
```

Exemplo:
![]('./images/list-all.png)

2. Listar por filtro de localidade

3. Listar por _id




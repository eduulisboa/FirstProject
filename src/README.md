# S3 - FastAPI Boilerplate
Template de backend utilizando FastAPI

## Como usar
Faça um clone desse repositório dentro do repositório em que você irá usá-lo:
```bash
git clone https://github.com/S3-Software-Solutions-Services/fastapi-boilerplate.git
```

Mova os arquivos do boilerplate para a raíz do seu repositório:
```bash
mv fastapi-boilerplate/* .
mv fastapi-boilerplate/.env.dev .
mv fastapi-boilerplate/.vscode .
```

Remova a pasta do boilerplate que ficará vazia:
```bash
rm -rf fastapi-boilerplate
```

#

# Setup Project

## Requisitos
- Python 3.8+
- Docker & Docker Compose
- Pipenv

## Instalando Pipenv (caso não tenha instalado)
Em um terminal de sua escolha, execute:
```bash
pip3 install pipenv
```

## Instalando dependencias e ativando ambiente virtual
Em um terminal de sua escolha, execute:
```bash
pipenv install
pipenv shell
```

## Rodando a aplicação
Em um terminal de sua escolha, execute:
```bash
docker-compose up # Caso queira parar pressione CTRL + C
```

Acesse a aplicação na rota padrão:
- http://127.0.0.1:8000/docs

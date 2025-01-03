# Usar a imagem base do Python 3.10 (compatível com Pipenv)
FROM python:3.10-bookworm

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY Pipfile ./

# Instalar Pipenv
RUN pip install --no-cache-dir pipenv

# Instalar as dependências usando o Pipenv
RUN pipenv lock && pipenv install --system

# Copiar os arquivos do projeto para o container
COPY . /app

# Expor a porta 1337 para o Coolify
EXPOSE 1337

# Configurar o comando de inicialização com o Pipenv
CMD ["python", "main.py"]

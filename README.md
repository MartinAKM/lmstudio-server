# Passo a passo

## 1. Comece criando um ambiente virtual

### Criando ambiente virtual
    py -3.13 -m venv venv

### Ativando ambiente virtual
    ./venv/Scripts/Activate.ps1

### Instalando bibliotecas no ambiente virtual
    pip install --no-cache-dir -r requirements.txt

## 2. Crie o arquivo .env com base no example.env

## 3. Crie uma imagem e container

### Criando imagem com base no arquivo Dockerfile
    docker build -t lmstudio-server .

### Criando container com base na imagem
    docker run -d -p 8020:8020 --name lmstudio-server  lmstudio-server
# Cat Breeds API Validation

Este projeto foi criado para validar a API  Cat Breeds.
O foco principal foi validar a API pública Cat Facts API (https://catfact.ninja/),é verificar a resposta da API para diferentes cenários de paginação e limites de resposta do endpoint GET “/breeds”.

## Requisitos

- Python 3.11.8
- Requests 2.32.3
- Behave 1.2.6
- Allure 2.27.0

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/welitaluisa/CatFactsQe
   cd seu-repositorio

2. Instale as dependências:
   ```bash
    pip install -r requirements.txt


## Estrutura do Projeto

test/features/ - Contém os arquivos de cenário Behave (features).
test/steps/ - Contém os arquivos de passos que implementam os cenários de teste.
test/allure/ - Relatórios gerados pelo Allure.
reports/ - Contém arquivo html
Postman/ - Contem a collection.json e o arquivo environments
Mapa mental/ - Contém o mapa mental usado no desafio criado no XMind


## Como Rodar os Testes

1. Execute os testes com o Behave:

    ```bash
    behave ou 
    behave --format allure_behave.formatter:AllureFormatter --outfile=allure-results

    - Dentro da pasta '\tests'

2. Para gerar o relatório do Allure após os testes:

    ```bash
    allure generate allure-results -o reports/html --clean


## Exemplos de Cenários de Teste

### Os seguintes cenários são validados para a API de raças de gatos:

1. Validação da resposta da API sem paginação

* A API deve retornar o status 200.
* A resposta deve conter as propriedades current_page = 1 e per_page = 25.
* A última breed na lista deve ser "Chausie".    

2. Validação da resposta da API para a página 2

* A API deve retornar o status 200
* A resposta deve conter as propriedades current_page igual e per_page = 25.
* A última breed na lista deve ser "Kurilian Bobtail, or Kuril Islands Bobtail"

3. Validação da resposta da API para a página 4

* A API deve retornar exatamente 23 raças na pagina 4,
* A lista deve começar do item 76.
* A última breed encontrada deve ser "York Chocolate"

4. Validação da resposta com limite 45 na página 1:

* A resposta deve validar que retorna 45 itens na pagina 1
* A última breed encontrada deve "serKarelian Bobtail"
* A última pagina é 3

5. Validação da resposta com limit = 1

* Valida que deve ser retornado apenas 1 breed na pagina 1

6. Validação da resposta buscando um pagina inexistente

* Valida que é retornado lista vazia

7. Validação de limit negativo 

* Valida que é retornado 'Bad Resquest' 
***Cenário falhado porque esta retornando "Não encontrado". 

## Contribuições

Contribuições são bem-vindas! Para enviar uma contribuição:

1. Crie um fork do repositório.
2. Crie uma nova branch (git checkout -b feature-nova).
3. Faça suas alterações e commit (git commit -am 'Adicionar nova feature').
4. Envie para o seu fork (git push origin feature-nova).
5. Crie uma Pull Request.


# DESAFIO MATERA

## Estratégia de Testes - Web

### Teste exploratório

-   Baseado em experiência - ad hoc

	- Como não possuo uma expecificação técnica , irei realizar alguns testes exploratório na funcionalidade 

-  Baseado em Hipótese

	- Lee Copeland

		- Hipótese 1 - Buscar por nome usando 3 caracteres  

			- Deve retornar todos usuários que contém no nome os 3 caracteres digitados

		- Hipótese 2 - Buscar por email passando email completo

			- Deve retornar o usuário cadastrado que contém o e-mail digitado

		- Hipótese 3 - Filtrar sem preencher nenhum campo

			- Deve retornar mensagem de erro com exigencia de escolher um filtro obrigatóriamente

		- Hipótese 4 -  Pode selecionar mais de um tipo de pessoa 

			- deve retornar a lista de tipos de pessoa selecionado

- Baseado em Heurísticas

	- Baseado em principios
Julio de Lima

		- Campos Obrigatórios

			- Quais campos são obrigatório?

		- Mascara

			- O campo "e-mail" valida se o e-mail é valido?

		- Estouro de campo

			- Qual tamanho maximo de caracteres do campo "Nome"?

		- Listagem de 0,1 e muitos registros

			- Como é exibido a tela quando não encontra nenhum registro?
			- Qual limite maximo de registro exibido por tela?
			- Existe paginação ? Se sim, qual é o limite por tela?

		- Responsividade

			- Verificar como é exibido os botões e os campos do filtros em diferentes responsividade da tela

- Baseado em Sessão

	- Jon e James Bach

		- Sessãp: 45 a 90 min
		- Charter

			- Explore 
			- Com uso de: 
			- Para saber

		- Relatório de Sessão

## Estratégia de Testes - API

### teste exploratório

- Para testar a API Utilizarei o check List  sugerido por Julio de Lima 

	-  Regra de negócio
	-  Continuidade dos fluxos
	-  Tipagem de dados
	-  Parâmetro ( corpo, filtro, path, etc)
	-  Uso de token de usuário diferente
	-  Validação de métodos
	-  Listagem de 0, 1, e muitos recursos
	-  Estrutura da resposta
	-  Códigos dos estados HTPP
	-  Documentos dos contratos da API

- Heuristica VADER

	- Verbos - Métodos da API
	- Autentificação e Autorização
	- Dados e sua Estrutura
	- Codigo de HTTP para Erros
	- Responsibilidade - Tempo de respost

### Regra de negocio

- Partição de Equivalência 
- Tabela de decisão
- Analise valor Limite
- Analise de Risco

## Exercício 1 - Testes funcionais de frontend 

# Resolução:

### Consulta de usuários - Filtros

- Campos

	- Tipo de pessoa

		- dropdown

	- Nome

		- label

	- E-mail

		- label

- Botão

	- LIMPAR FILTROS
	- FILTRAR

### CASOS DE TESTES WEB

- caminhos felizes

	- [CT - 01] Filtrar usuário pelo tipo de pessoa específica 

		- Scenario: Search users by person type
		-   Given that I am on the "User Query" screen
		-   When I select "ADM" from the "Person Type" drop-down menu
		-   And click on the "Filter" button
		-   Then I should see a list of users that are of type "ADM"

	- [CT - 02] Filtrar usuário pelo nome 

		- Scenario: Search users by name
		-   Given that I am on the "User Query" screen
		-   When  I type "Welita Luisa" in the "Name" field
		-   And  click on the "Filter" button
		-   Then I should see a list of users containing "Welita Luisa"

	- [CT - 03] - Filtrar usuário por e-mail

		- Scenario: Search users by email
		-   Given that I am on the "User Query" screen
		-   When I type "welita.luisa@teste.com.br" in the "Email" field
		-   And click on the "Filter" button
		-   Then I should see a list of users with the email "welita.luisa@teste.com.com.br"

	- [CT - 04] Filtrar por tipo e nome de pessoa simultaneamente

		- Scenario: Search users by person type and name
		-   Given that I am on the "User Query" screen
		-   When I select "ADM" from the "Person Type" drop-down menu
		-   And type "Joaquim Lima" in the "Name" field
		-   And click on the "Filter" button
		-   Then I should see a list of ADM users containing the name "Joaquim Lima"

	- [CT - 05] Filtrar por nome e e-mail simultaneamente

		- Scenario: Search users by name and email
		-   Given that I am on the "User Query" screen
		-   When I type "Ana Smith" in the "Name" field
		-   And type "ana.smith@example.com" in the "Email" field
		-   And click on the "Filter" button
		-   Then I should see a list of users named "Ana Smith" with the email "ana.smith@example.com"

	- [CT - 06] Limpar filtros e verificar se os campos ficam vazios e se a tela retorna o estado padrão 

		- Scenario: Clear filters and clear fields
		-   Given that I am on the "User Query" screen
		-   And I filled in the fields "Type of person", "Name" and "Email"
		-   When I click the "Clear filters" button
		-   Then all filter fields must be displayed empty
		-   And the user list should return to its default state


	- [CT - 07] Filtrar usuário inserindo apenas 3 caracteres no campo "Nome"

		- Scenario: Filter user by entering only 3 characters in the "Name" field
			- Given that I'm on the "User Search" screen
			- When I type "ana" in the "Name" field
			- And I click the "Filter" button
			- Then you must list all users who currently contain the characters "ana"

	- [CT - 08] Preencher os filtros , limpar e inserir novos valores

		- Scenario: Populate filters, clear them, and enter new values
			- Given that I am on the "User Query" screen
			- And I entered values ​​in the “Type of person”, “Name” and “Email” fields
			- When I click the "Clear filters" button
			- Then, all filter fields must be empty
			- When I select “Person Type” again
			- And I type "José X" in "Name"
			- And type "jose.x@teste.com.br" in "Email"
			- And click on the "Filter" button
			- Then the results corresponding to the new filter values ​​should then be displayed

- caminhos infelizes

	- [CT - 01] Buscar usuário com e-mail inválido

		- Scenario: Search users with an invalid email format
		-   Given that I am on the "User Query" screen
		-   When I type "invalid-email" in the "Email" field
		-   And click on the "Filter" button
		-   Then I should see an error message "Invalid email format"

	- [CT- 02] Filtrar sem preencher nenhum campo

		- Scenario: Search for users without filling in any filters
		-   Given that I am on the "User Query" screen
		-   When I click the "Filter" button without filling in any fields
		-   Then I should see a message "you need to choose a filter"

	- [CT - 03 ]Validar limite de caracteres suportado no campo "Nome"

		- Scenario: Enter more characters than allowed in the "Name" field
		-   Given that I am on the "User Query" screen
		-   When I type a name longer than 1000 characters in the "Name" field
		-   And click on the "Filter" button
		-   Then I should see an error message "The "name" field supports up to X characters"

	- [CT - 04] Digitar e-mail sem dominio "@"

		- Scenario: Enter an email without "@" or domain
		-   Given that I am on the "User Query" screen
		-   When I type "invalidemail.com" in the "Email" field
		-   And click on the "Filter" button
		-   Then I should see an "Invalid email format" error message

	- [CT - 05] Inserir caracteres especiais no campo "Nome"

		- Scenario: Search users with invalid characters in the name
			- Given I am on the "User Search" screen
			- When I enter "@#$%&*!" in the "Name" field
			- And I click on the "Filter" button
			- Then I should see an error message "Invalid characters in the name field"

****************************************************************************************************************************

## Exercício 2 - Testes funcionais de backend 

### API 

- https://catfact.ninja

# Resolução: 

### CASOS DE TESTE API

- caminhos felizes

	- GET /Breeds

		- [CT - 01] Busca todas as raças de gato cadastrados 

			- Retorna uma lista de 25 raças de gato na pagina 1

				- Scenario: Successfully retrieve the front page of cat breeds
				- Given that the API is available
				- When I send a GET request to "/breeds", 
				- Than response status should be 200
				- And the response must contain an array of “data”
				- And the “data” array must have up to 25 items
				- And each item must have the fields “breed”, “country”, “origin”, “coat” and “pattern”
				- And the last breed is Chausie

	- GET/breeds?page=2

		- [CT - 02] Busca apenas a lista de raça de gatos da pagina 2

			- Scenario: search for the list of breeds on page 2
			-     Given that the API is available
			-     When send a GET request to "breeds?page=2
			-     Than the response status should be 200
			-     And the response must contain a "current_page" field with value 2
			-     And the number of races returned must be equal to 25
			-     And list on page 2 starts at item 26
			-     And the last breed returned should be "Kurilian Bobtail, or Kuril Islands Bobtail"
			-     And the active pagination link is 2

	- GET/breeds?page=3

		- [CT - 03] Busca apenas a lista de raça de gatos da pagina 3

			- Scenario: search for the list of breeds on page 3
			-     Given that the API is available
			-     Than I send a GET request to "breeds?page=3
			-     Than the response status should be 200
			-     And the response must contain a "current_page" field with value 3
			-     And the number of races returned must be equal to 25
			-     And list on page 2 starts at item 51
			-     And the last breed returned should be "Russian Blue"
			-     And the active pagination link is 3

	- GET/breeds?page=4

		- [CT - 04] Busca apenas a lista de raça de gatos da pagina 4

			- Scenario: search for the list of breeds on page 4
			-     Given that the API is available
			-     When I send a GET request to "breeds?page=4
			-     Than the response status should be 200
			-     And the response must contain a "current_page" field with value 4
			-     And the number of races returned must be equal to 23
			-     And list on page 4 starts at item 76
			-     And the last breed returned should be "York Chocolate"
			-     And the active pagination link is 4

	- Get/breeds?page=1&limit=45

		- [CT - 05] Busca apenas a lista de raça de gatos da pagina 1 e limite = 45

			- Scenario: Search only the cat breed list on page 1 and limit = 45
			-     Given that the API is available
			-     When I send a GET request to "breeds?page=1&limit=45
			-     Than the response status should be 200
			-     And the response must contain a "current_page" field with value 1
			-     And the number of races returned must be equal to 45
			-     And the last breed returned should be "Karelian Bobtail"
			-     And the active pagination link is 1
			-     And the last pagination is = 3

	- GET/breeds?limit=30

		- [CT - 06] Busca com limite de 30 raças de gato por pagina

			- Scenario: Search with a limit of 30 cat breeds per page
			-     Given that the API is available
			-     When I send a GET request to "breeds?limit=30
			-     Than response status should be 200
			-     And the response must contain a "current_page" field with value 1
			-     And the number of races returned must be equal to 30
			-     And the last breed returned should be "Cyprus"
			-     And the active pagination link is 1
			-     And the last pagination is = 4

	- GET/breeds?limit=1

		- [CT - 07] Busca com limite de 1 raças de gato por pagina

			- Scenario: Search with a limit of 1 cat breeds per page
			-     Given that the API is available
			-     When I send a GET request to "breeds?limit=1
			-     Than response status should be 200
			-     And the response must contain a "current_page" field with value 1
			-     And the number of races returned must be equal to 1
			-     And the last breed returned should be "Abyssinian"
			-     And the active pagination link is 1
			-     And the last pagination is = 98

	- GET/breeds?limit=98

		- [CT - 08] Busca com limite de 98 raças de gatos por pagina

			- Scenario: Search with a limit of 98 cat breeds per page
			-     Given that the API is available
			-     When I send a GET request to "breeds?limit=98
			-     Than response status should be 200
			-     And the response must contain a "current_page" field with value 1
			-     And the number of races returned must be equal to 1
			-     And the last breed returned should be "York Chocolate"
			-     And the active pagination link is 1
			-     And the last pagination is = 1

- caminhos infelizes

	- GET/breeds?limit=0

		- [CT -01] Busca limite = 0

		  Quando envia limite = zero a api retorna 15 raças de cachorro por pagina. nesse caso não deveria retornar uma lista vazia?
		  

			- Scenario: Search limit = 0
				-  Given that the API is available
				-  When I send a GET request to "breeds?limit=0
				-  Than Should return empty list

	- GET/breeds?limit=-10

		- [CT - 02] Busca com limite negativo

			-   Scenario: Request with an invalid limit parameter
			-     Given the API is available
			-     When I send a GET request to "/breeds" with "limit=-10"
			-     Then the response status should be 400
			-     And the response should contain an error message

	- GET/breeds?page=-4

		- [CT - 03] Busca com pagina negativa

			- Scenario: Negative page search
			- Given that the API is available
			- When I do a search, passing a negative page on the garment
			- Then the API should return an error 
			- And the message "cannot return negative page search"

	- GET/breeds?page=0

		- [CT - 04]Busca com pagina =0

			- Scenario: Zero pagination
				- Given that the API is available
				- When I do a search, passing a zeroed page on the clothing
				- Then the API should return an error 
				- And the message "cannot return search for page zero"

	- GET/breeds?page=999

		- [CT - 05]Busca com pagina invalida

			- Scenario: Invalid pagination
				- Given that the API is available
				- When I do a search, passing an invalid page in the parameter
				- So the API should return an empty list

**************************************************************************************************************************

## Exercício 3 - Resolução de problemas

### Você encontrou um bug em um API em ambiente de produção que ocasionou diversas dificuldades para o cliente

- De que forma você reportaria esse bug?

# Resposta

	- Antes de reportar um bug sigo o seguinte framework:

		- 1 - Confirmo se o bug realmente esta acontecendo ou se não foi problemas de ambiente ou massa de testes inconsistentes
		- 2 - reproduzo o bug, coleto todas as informações possiveis: 
			- Logs, ambiente afetado, qual foi a versão da feature que iniciou a falha, qual o risco 
		- 3 - Crio um Card de bug no Azure ou outro sistema de gestão de bugs, contendo todas as informações detalhadamente encontrada no passo 2, o passo a passo para reproduzir as evidências  e a feature relacionada

			- Exemplo - 1: [Errro]Busca com limite negativo -1 esta retornando codigo 404 ao invez de 400

				- Ao realizar a busca passando o parametro limit=-1 a api retorna o erro 404 " e a mensagem "Not Fout"
				- Ambiente: Produção 
				- API: GET/https://catfact.ninja/breeds?limit=-1
				- Retorno esperado: // Deveria retornar mensagem de erro  400 (Bad Request)
				- Detalhes: no Script do Postman no [CT- 12]Busca com limite negativo -1

			- Exemplo 2 - [Erro] - Busca com limite = 0, esta retornando lista com 15 raças deveria retornar lista vazia

				- Ao realizar a busca passando o parametro limit=0 a api retorna  15 raças de gatos na pagina 1 
				- Ambiente: Produção
				- API: https://catfact.ninja/breeds?limit=0
				- Retorno esperado:   // Deveria retornar lista vazia 
				- Detalhes: no postman, no [CT- 11]Busca com limite = 0 

		- 4 - Comunico com o time sobre o bug criado  e qual é o impacto sobre o negocio e a criticidade do bug
		- 5 - Monitoro a correção e testo após a correção para garantir que foi corrigido
		- 6 - Automatizo os cenários referente ao bug garantindo a amplitude da cobertura e os testes de regressão

## Você identificou que este problema poderia ter sido pego durante os testes da feature. 

	- O que você poderia fazer para mitigar este bug e possíveis futuros nessa feature?
	
	# Resposta

		- Adicionar um teste especifico para esse bug 
		- Rodar todos os testes automatizados já existente - testes de regreção
		- Analisar a cobertura de teste de unidade e integração 
		- Implementar alertas automáticos para detectar erro inesperados
		- Realizar teste exploratório com proposito de encontrar defeito não cobertos nos testes automatizados

****************************************************************************************************************************

## Exercício 4 - Testes automatizados

- Foi criado a automação no endereço: https://github.com/welitaluisa/CatFactsQe 


*XMind - Trial Version*
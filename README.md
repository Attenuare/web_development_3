# web_development_3
Projetos básicos desenvolvido em Django com o intuito de obter as primeiras impressões do framework

## First Project
Projeto simples de iniciação por meio do framework Django, utilizando templates diferentes para averiguar feriados.

## Check Hollyday SQLite
Projeto elaborado por meio do Framework Django, que através do consumo da API `holidayapi.com` realiza o upload de feriados para o banco de dados, e por meio de um input do usuário verifica se o dia em específico é feriado ou não em algum pais.

#### Inicialização
* Necessário a instalação do Framework Django e suas respectivas dependências
* Na raiz do projeto execute o comando `pip install -r requirements.txt <br\>
* Após finalizada a instalação inicie o servidor com o comando `python manage.py runserver <br/>
*Output:*

  ![image](https://user-images.githubusercontent.com/102560265/230701184-e2e1f42c-8842-4117-ba57-c01bb6abd1c0.png)


#### Atualização da base de Feriados
* Na raiz do projeto onde contem o arquivo `manage.py` entre no modo imperativo com as *variáveis de ambiente* carregadas, por meio do comando `python manage.py shell`
* Realize o import da Classe de conexão com a API por meio do commando `from polls.hollidays_api.libs.hollidays_class import Hollydays`
* Instancie um objeto do tipo Hollydays `object_ = Hollydays()` e execute o método `object_.get_all_hollidays()` <br/> Dessa forma o objeto iniciará o download de todos os feriados dos respectivos países.
* Após a finalização do download realize a inserção no banco de dados por meio do comando `object_.database_insert_holliday()` <br/>
O Output em seguida exemplifica a resposta do envio, caso haja realmente algo a ser atualizado no banco de dados.

  ![image](https://user-images.githubusercontent.com/102560265/230701049-23bae847-c793-45a6-be1f-eb0d8dcb589d.png)

Comandos utilizados:
1. Após criar a pasta do projeto, entre na mesma e dê o comando django-admin startproject nome_projeto .
(Com o ponto no final não cria uma subpasta com o projeto após finalizar o comando)
2. Um projeto django é composto por várias apps
3. Criando uma nova app (python manage.py startapp nome_da_app)
4. Criando o banco de dados(python manage.py migrate)
5. Criando superusuário para a aplicação: (python manage.py createsuperuser)
6. Realizando as migrações após criar ou atualizar o modelo: (python manage.py makemigrations) e após isso (python manage.py migrate) para aplicar as migrações

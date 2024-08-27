# Gerador de Dietas - README
## Descrição
O Gerador de Dietas é uma aplicação web que permite aos usuários inserirem informações pessoais como peso, altura e o objetivo que desejam alcançar, sejam eles perda de peso, ganho de massa e manutenção.

## Funcionalidades
- Inserção de informações.
- Gerar cronograma de alimentação: Ao submeteras informações, um cronograma é exibido na tela, formatada em HTML.
## Estrutura do Projeto
- HTML (index.html): Estrutura a interface do usuário, permitindo a inserção de ingredientes e a visualização da receita gerada.
- CSS (style.css): Estiliza a interface, proporcionando uma experiência de usuário agradável.
- JavaScript (script.js): Manipula as interações do usuário, como adicionar ou remover ingredientes, e faz a requisição ao backend para gerar a receita.
- Backend (app.py): Utiliza o Flask para criar uma API que recebe os ingredientes, comunica-se com o modelo generativo para criar a receita, e retorna o resultado em formato HTML.
## Como Executar
### Requisitos
- Python 3.x
- Flask
- Flask-CORS
- Google Generative AI (Biblioteca gemini)
## Passos para Configuração
- Clone o repositório:
git clone https://github.com/GustaDev07/NutriFit.git
cd projeto-gerador-receitas

- Instale as dependências do Python:
pip install flask flask-cors google-generativeai

- Gere sua chave de API em: https://aistudio.google.com/app/u/1/apikey
- Adicione sua chave API do Google Generative AI no arquivo app.py na linha:
gemini.configure(api_key="suachaveapi")

- Execute a aplicação Flask:
python api.py

- Abra o arquivo index.html no navegador:
Utilize um servidor local, como Live Server no VS Code, ou abra o arquivo diretamente em seu navegador.

## Licença
Este projeto é licenciado sob a Licença MIT.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Contato
Para mais informações, entre em contato pelo email: gustarealyze@gmail.com

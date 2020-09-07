# Zup Test

### Tecnologias Utilizadas
- Python 3.8
- Bibliotecas: behave, selenium, xlrd
   - Instalação pelo gerenciador de pacotes do Python: "pip install selenium behave xlrd" ou "pip3 install selenium behave xlrd". (Executar comando sem aspas)

### Instruções para execução dos testes via interpretador do Python
  - Criar uma virtual environment com o Python ou utilizar o interpretador padrão do Python.
  - Abrir o Projeto com a IDE Pycharm e criar uma execução para o arquivo main.py ou executar a linha de comando "python main.py" ou "python3.8 main.py" no diretório raiz do projeto. (Executar comando sem aspas)
  
### Instruções para execução dos testes via docker
  - Ter o docker instalado na máquina.
  - Acessar o diretório raiz do projeto e executar o comando "docker build --tag zuptest ." para criação da imagem. (Executar comando sem aspas)
  - Executar o script run_with_docker.sh disponível no diretório raiz do projeto para execução dos testes no docker.

### Informações úteis
  - As plataformas suportadas para execução são: Firefox e Chrome | Linux e Windows.
  - Antes de executar os testes, verificar o S.O e versão do navegador na sua máquina e realizar o download do chromedriver e geckodriver correspondente a versão do navegador em: https://chromedriver.chromium.org/downloads , https://github.com/mozilla/geckodriver/releases . Após isso substituir os arquivos no diretório "drivers/files" a partir do diretório raiz do projeto. (Permissionar o arquivo baixado para execução caso utilize S.O Linux)
  - O navegador pode ser alterado no arquivo main.py substituindo na linha 20 o comando "before_suite('F', False)" para Firefox e "before_suite('C', False)" para Chrome. (Inserir comando sem aspas duplas)
  - A estrutura utiliza BDD para execução dos testes com a biblioteca behave do Python. Os arquivos de histórias com a extensão ".feature" podem ser encontrados no diretório "features" a partir do diretório raiz do projeto.
  - O projeto captura os dados de entrada para pesquisa do produto e dados para validação do mesmo a partir de um arquivo excel utilizando a biblioteca xlrd do Python. O arquivo excel se encontra no diretório "data" a partir do diretório raiz do projeto.
  - O projeto pode ser executado em headless alterando na linha 20 o comando "before_suite(Navegador, False)" para não execução em headless e "before_suite(Navegador, True)" para execução em headless, do arquivo main.py a partir do diretório raiz do projeto. Por padrão o valor da variável é True para execução em healdless no docker.
  - No diretório raiz do projeto encontra-se o arquivo de dependências "requirements.txt".
  - Foram adicionados 3 cenários de testes, no primeiro apenas a inserção do produto é realizada. No segundo é inserido o produto e incrementada a quantidade do mesmo no carrinho. E no último é adicionado um produto no carrinho e realizada a remoção.
  - Os logs de execução são gerados no diretório "logs/navegador_em_execução/data_atual" a partir do diretório raiz do projeto. Lá também são geradas na pasta screenshots as capturas de tela quando o teste retorna erro. Todos os logs e capturas de telas são gerados utilizando o padrão de data e hora atual.
  - Este projeto utiliza o padrão Page Objects e os testes são separados nos dretórios: "page" (Páginas), "steps" (Passo a passo dos testes) e features (Arquivo BDD).
  - Todas as interações do selenium com o navegador foram abstraídas no arquivo "drivers/interact.py" a partir do diretório raiz o projeto. Os erros gerados ao não encontrar os objetos foram tratados nas funções.
  - Os diretórios utilizados no código foram capturados a partir de funções para serem utilizadas em todo o projeto de testes visando a reutilização de código.
  - A grande maioria das classes estão comentadas com a descrição da usabilidade da mesma.

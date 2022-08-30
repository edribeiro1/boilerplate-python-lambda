# Boilerplate Lambda


1. Iniciar o git.
    - ```git init```
2. Configurar .gitignore.
    - Utilizar o [gitignore.io](https://www.toptal.com/developers/gitignore/)
3. Definir arquitetura de arquivos.
    - Padrão Python
        - .git/
        - docs/
        - src/ ou "nome_do_projeto/"
        - tests/
        - .gitignore
        - requirements.txt
        - README.md
        - 
4. Ambiente Virtual
    - Configurar e habilitar ambiente virtual
        - ```python -m venv venv```
        - Windows CMD/Powershell
            - ```venv\Scripts\activate```
        - Windows Gitbash/Linux terminal
            - ```source venv/Scripts/activate```
        - Linux Terminal
            - ```source venv/bin/activate```

5. Instalar Dependências
    - Ambiente dev
        - ```pip install prospector[with_everything] blue isort -r requirements.txt```
    - Ambiente testes/integração
        - ```pip install -r requirements.txt```
    - Ambiente homologação/produção
        - ```pip install -r requirements.txt```
    
5. Ferramentas de formatação de código.
    - Padronização de escrita de código
        - blue (formata o código)
        - isort (faz o sort das importações)

6. Ferramentas de análise.
    - Checagem de qualidade e complexidade de código
        - bandit (Problemas de segurança)
        - mypy (Tipagem)
        - prospector (Agregador de ferrametas)
            - Flake8
            - Mccabe
            - pylint
            - pep8
            - pep257
        
```prospector --no-autodetect --strictness veryhigh src/```

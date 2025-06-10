# agente-csv-grupo302

Agente autônomo com LangChain para análise de CSVs via linguagem natural.

✅ 1. Criar o projeto no Deepnote

* Acessar a url  https://deepnote.com 

* Fazer o login.

* Clicar em  “New project”.

* Nomear o projeto: Agente_CSV_Grupo302.

* Selecionar o kernel Python 3.

* Aguardar o ambiente ser carregado.

✅ 2. Upload da estrutura de arquivos

* Clicar na aba “Files” na lateral esquerda.

* Fazer o upload dos seguintes arquivos:

	-  main.ipynb

	- Pasta /scripts/ agente.py

	- Pasta /data/ 202401_NFs.zip

	- requirements.txt

✅ 3. Instalar as dependências

- Executar na primeira célula do main.ipynb o comando: !pip install -r requirements.txt

✅ 4. Executar o notebook main_nfs.ipynb


* Extrair o conteúdo de 202401_NFs.zip para a pasta /data.

* Ler os arquivos CSV com pandas.

* Criar os agentes com LangChain.

* Fazer perguntas em linguagem natural.

💡 Certifique-se de substituir "sua-chave-aqui" pela sua chave de API da OpenAI (ou usar variável de ambiente no Deepnote).

✅ 5. Usar variáveis de ambiente (para segurança)

* Ocultar a chave da OpenAI:

	- Clicar em Environment (ícone de engrenagem no menu lateral).

	- Clicar em Environment variables.

	Adicionar: OPENAI_API_KEY: sua-chave-aqui

* Escrever no notebook:

```Python
import os
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
```

✅ 6. Colaboração no Deepnote

* Em Settings > Share, convidar os membros do grupo (limite de 5 membros).

Lembre-se: apenas 3 membros podem editar simultaneamente na versão gratuita.

* Usar comentários nas células para revisões assíncronas.

✅ 7. Estrutura da Solução do Projeto no Deepnote

📁 Agente_CSV_Grupo302
├── main.ipynb          ← Notebook principal para análise de NFs
├── requirements.txt
├── .env (não obrigatório)
├── /scripts/
│   └── agente.py
├── /data/
│   ├── 202401_NFs.zip
│   └── ...

✅ 8. Estrutura da Solução do Projeto no GitHub

📁 Organização da pasta do projeto

Agente_CSV_Grupo302/
│
├── README.md                     ← Apresentação do projeto
├── requirements.txt             ← Bibliotecas necessárias
├── .env                         ← (opcional) Chave da OpenAI
├── main.ipynb                   ← Notebook com agente genérico
├── /data/                       ← Arquivos CSV extraídos do .zip
│   ├── 202401_NFs.zip│
├── /scripts/                    ← Scripts auxiliares
│   └── agente.py                ← Função de criação do agente LangChain

🔧 Lógica da solução (funcionamento do sistema)

Etapa	Descrição

1. Upload	O usuário envia o arquivo .zip com os CSVs.

2. Extração	O notebook extrai os arquivos na pasta /data.

3. Leitura	Os CSVs são lidos com pandas como DataFrames.

4. Criação de agente	O LangChain usa o create_pandas_dataframe_agent com o LLM configurado.

5. Perguntas em linguagem natural	O usuário faz perguntas, e o agente responde com base nos dados.

6. Visualização e validação	As respostas são exibidas e comparadas com o esperado.

🔍 Dependências

| Pacote          | Função principal                                       |
|-----------------|--------------------------------------------------------|
| `langchain`     | Framework para construção de agentes LLM.              |
| `openai`        | Interface com modelos da OpenAI (ChatGPT, GPT-4).      |
| `llama-index`   | Framework para indexação e consulta de dados com LLMs. |
| `pandas`        | Leitura e manipulação de arquivos CSV.                 |
| `python-dotenv` | Carregar variáveis de ambiente de um arquivo `.env`.   |

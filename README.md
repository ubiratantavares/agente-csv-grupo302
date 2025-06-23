# 🧠 Agente Autônomo para Análise de Notas Fiscais em CSV — Grupo 302

Este projeto tem como objetivo o desenvolvimento de um agente autônomo capaz de ler arquivos CSV contendo dados de notas fiscais, interpretar perguntas em linguagem natural e fornecer respostas automáticas e precisas, combinando inteligência artificial, busca vetorial e automação de processos.

## ⚙️  Tecnologias e Ferramentas Utilizadas

* [LangChain](https://python.langchain.com/) — Framework para construção de agentes inteligentes com LLMs.

* [HuggingFace Embeddings](https://huggingface.co/sentence-transformers) — Geração de embeddings para representação vetorial dos documentos.

* [FAISS](https://github.com/facebookresearch/faiss) — Biblioteca para busca vetorial eficiente.

* [OpenRouter (GPT-3.5 Turbo)](https://openrouter.ai/) — LLM utilizado para compreensão e geração de respostas.

* [pandas](https://pandas.pydata.org/) — Manipulação e tratamento dos dados estruturados.

* [Deepnote](https://deepnote.com/) — Ambiente colaborativo de notebooks interativos (opcional para testes e prototipação).

## 📁 Estrutura do Projeto

```plaintext
├── app.py                            # Script principal de execução do agente
├── install.sh                        # Script de instalação das dependências
├── requirements.txt                  # Dependências do projeto
├── data/
│   └── 202401_NFs.zip                # Arquivo compactado contendo os CSVs
│   └── 202401_NFs/                   # Dados extraídos (cabeçalho, itens, dados consolidados)
├── nf/
│   ├── agent.py                      # Implementação do agente RAG
│   ├── csv_loader.py                 # Carregamento dos arquivos CSV
│   ├── formatter/
│   │   ├── nota_fiscal_document_builder.py  # Formatação dos documentos para o RAG
│   │   └── nota_fiscal_preprocessor.py      # Pré-processamento e consolidação dos dados
│   ├── vectorstore.py                # Criação do índice vetorial com FAISS
│   └── zip_extractor.py              # Extração do arquivo ZIP
```

## 🚀 Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/ubiratantavares/agente-csv-grupo302.git
cd agente-csv-grupo302
```

2. **Instale as dependências:**

```bash
bash install.sh
```

3. **Execute o agente:**

Edite o arquivo `app.py` se necessário (por exemplo, forneça sua API Key do OpenRouter), depois:

```bash
python app.py
```

O sistema irá:

* Descompactar os dados (se ativado)

* Carregar e consolidar os CSVs

* Criar documentos formatados a partir dos dados

* Gerar o índice vetorial com embeddings

* Inicializar o agente autônomo

* Executar perguntas de teste e apresentar as respostas

## 💡 Exemplo de Perguntas

✔️  Quais empresas emitiram notas fiscais acima de R\$ 1.000.000,00?

✔️  Qual a nota fiscal com maior valor emitido para o estado de SP?

✔️  Quais foram as três notas fiscais de maior valor emitidas em janeiro de 2024?

✔️  Quantas notas fiscais tiveram como destinatário o Fundo Nacional de Desenvolvimento da Educação?

✔️  Qual o valor total das notas fiscais destinadas ao estado de São Paulo (SP)?

## 🛠️  Requisitos

* Python 3.10 ou superior

* API Key válida do [OpenRouter](https://openrouter.ai/)

* Sistema operacional compatível com os pacotes Python do projeto

## 👨‍💻 Equipe

**Grupo 302 — Análise de CSV**

| Nome     | E-mail                                                                    |
| -------- | ------------------------------------------------------------------------- |
| Ubiratan | [ust1973@gmail.com](mailto:ust1973@gmail.com)                             |
| Sérgio   | [sergio@peq.coppe.ufrj.br](mailto:sergio@peq.coppe.ufrj.br)               |
| João     | [copello13@gmail.com](mailto:copello13@gmail.com)                         |
| Ricardo  | [ricardogoncalveslima3@gmail.com](mailto:ricardogoncalveslima3@gmail.com) |
| Nathan   | [nathan.araujosantos@gmail.com](mailto:nathan.araujosantos@gmail.com)     |

## 📄 Licença

Este projeto é apenas para fins educacionais no contexto do curso de Agentes Autônomos do I2A2.

import os
from dotenv import load_dotenv

from nf.zip_extractor import ZipExtractor
from nf.csv_loader import CSVLoader
from nf.formatter.nota_fiscal_preprocessor import NotaFiscalPreprocessor
from nf.formatter.nota_fiscal_document_builder import NotaFiscalDocumentBuilder
from nf.vectorstore import VectorStoreBuilder
from nf.agent import RAGNotaFiscalAgent

# Carregar variáveis do .env
load_dotenv()

# Recuperar a API Key da variável de ambiente
api_key = os.getenv("OPENAI_API_KEY")

# local onde encontra-se o arquivo zipado
#zip_file_path = "./data/202401_NFs.zip"

# local onde o arquivo vai ser descompactado
extract_path = "./data/202401_NFs"

# extraindo o arquivo zipado
#extractor = ZipExtractor(zip_file_path, extract_path)
#extractor.extract()

# carregando os arquivos csv
loader = CSVLoader(extract_path)
dados = loader.load_csv_files()

for chave, valor in dados.items():
    print(f"{chave}: {valor.shape}")

# pré-processamento dos dados tabulares
# agrupando os itens por nota fiscal e mesclando os dados com o cabeçalho
preprocessor = NotaFiscalPreprocessor(dados)
df_merged = preprocessor.preparar_dados_estruturados()
extract_file_path = extract_path + "/" + "df_merged.csv"
df_merged.to_csv(extract_file_path, index=False)

# formatando os dados tabulares para o RAG
# formatando o texto da nota fiscal e criando o objeto Document
builder = NotaFiscalDocumentBuilder(df_merged)
docs = builder.formatar_documentos()

# inicializando o modelo de embeddings
vs_builder = VectorStoreBuilder()

# gerando vetores a partir de Document
vector_store = vs_builder.build_vectorstore(docs)

# construindo e expondo o retriever baseado em FAISS
retriever = vs_builder.get_retriever(vector_store)

agent = RAGNotaFiscalAgent(retriever, api_key)

queries = ["Quais empresas emitiram notas fiscais acima de R$ 20.000,00?",
           "Qual a nota fiscal com maior valor emitido para o estado de SP?",
           "Quantas notas fiscais tiveram como destinatário o Fundo Nacional de Desenvolvimento da Educação?",
           "Qual é o fornecedor que teve o maior valor recebido?",
           "Qual a descrição do item com o maior valor na quantidade entre todos as notas fiscais apresentadas?"]
             
for query in queries:
    print(f"\nPergunta: {query}")
    response = agent.consultar(query)
    print(f"Resposta: {response}\n")

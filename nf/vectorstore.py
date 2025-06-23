from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS

class VectorStoreBuilder:
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2", device: str = "cpu"):
        self.model_name = model_name
        self.device = device
        self.embedding_model = self._load_embedding_model()

    def _load_embedding_model(self):
        return HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={"device": self.device},
            encode_kwargs={"normalize_embeddings": True},
            multi_process=False
        )

    def build_vectorstore(self, documents: list[Document]) -> FAISS:
        return FAISS.from_documents(documents, self.embedding_model)

    def get_retriever(self, vectorstore: FAISS, k: int = 2):
        return vectorstore.as_retriever(search_kwargs={"k": k})


from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.agents import Tool,initialize_agent
from langchain.agents.agent_types import AgentType

class RAGNotaFiscalAgent:
    
    def __init__(self, retriever, 
                       openai_api_key: str, 
                       openai_api_base: str = "https://openrouter.ai/api/v1",
                       model: str = "openai/gpt-3.5-turbo",
                       temperature: float = 0):

        self.llm = ChatOpenAI(api_key=openai_api_key,
                              openai_api_base=openai_api_base,
                              temperature=temperature,
                              model=model,
                              max_tokens=256)
        
        self.retriever = retriever
        self.qa_chain = self._build_qa_chain()
        self.agent = self._build_agent()

    def _build_qa_chain(self):
        return RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=self.retriever)

    def _build_agent(self):
        tools = [Tool(name = "ConsultaNotasFiscais",
                      func = self.qa_chain.run, 
                      description="Use esta ferramenta para responder sobre notas fiscais emitidas em janeiro de 2024.")]

        return initialize_agent(tools=tools,
                                llm=self.llm,
                                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                verbose=True)    

    def consultar(self, query: str):
        return self.agent.invoke(query)
                   
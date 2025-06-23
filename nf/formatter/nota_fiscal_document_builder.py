import pandas as pd
from langchain.docstore.document import Document

class NotaFiscalDocumentBuilder:
    def __init__(self, merged_df: pd.DataFrame):
        self.merged_df = merged_df

    def formatar_documentos(self):
        documentos = []

        for _, row in self.merged_df.iterrows():
            conteudo = f"""
                        Nota Fiscal: {row['CHAVE DE ACESSO']}
                        Emitente: {row['RAZÃO SOCIAL EMITENTE']} ({row['UF EMITENTE']})
                        Destinatário: {row['NOME DESTINATÁRIO']} ({row['UF DESTINATÁRIO']})
                        Data de Emissão: {row['DATA EMISSÃO']}
                        Valor Total: R${row['VALOR NOTA FISCAL']:.2f}
                        Natureza: {row['NATUREZA DA OPERAÇÃO']}

                        Itens:
                        {row['DESCRIÇÃO ITENS']}
                        """
            documentos.append(Document(page_content=conteudo.strip()))

        return documentos

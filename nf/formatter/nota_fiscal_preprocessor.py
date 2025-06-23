import pandas as pd

class NotaFiscalPreprocessor:
    def __init__(self, dados):
        for filename, df in dados.items():
            if filename == "202401_NFs_Cabecalho.csv":
                cabecalho_df = df
            elif filename == "202401_NFs_Itens.csv":
                itens_df = df
        self.cabecalho_df = cabecalho_df
        self.itens_df = itens_df

    def agrupar_itens(self):
        grouped = self.itens_df.groupby("CHAVE DE ACESSO").apply(
            lambda x: "\n".join(
                f"- {row['DESCRIÇÃO DO PRODUTO/SERVIÇO']} (Qtd: {row['QUANTIDADE']}, Valor Total: R${row['VALOR TOTAL']:.2f})"
                for _, row in x.iterrows())
        ).reset_index(name="DESCRIÇÃO ITENS")
        return grouped

    def preparar_dados_estruturados(self):
        grouped_itens = self.agrupar_itens()
        return pd.merge(self.cabecalho_df, grouped_itens, on="CHAVE DE ACESSO", how="left")


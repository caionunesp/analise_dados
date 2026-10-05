import streamlit as st
import pandas as pd

st.title("Meu primeiro dash")

st.subheader("Caio Nunes Pereira")

st.divider()

st.write("Olá, mundo")

nome_usuario = "Caio Nunes Pereira"
idade_usuario = 18 
st.write(f"Usuário conectado: {nome_usuario} | Idade: {idade_usuario} anos")

st.divider()

df = pd.DataFrame({
    'Matérias': ['Português', 'Matemática', 'Python', 'Frame'],
    'Notas': [5, 9, 7, 10]
})

st.write("Visualização dos dados obtidos:")
st.dataframe(df) 

st.divider()

st.subheader("Caixa de Supermercado")

produtos_disponiveis = {
    "Arroz 5kg": 26.90,
    "Feijão 1kg": 7.50,
    "Café 500g": 18.20,
    "Leite 1L": 5.49
}

item_escolhido = st.selectbox(
    "Escolha um item para comprar:",
    options=list(produtos_disponiveis.keys())
)

quantidade = st.number_input("Digite a quantidade desejada:", min_value=1, value=1, step=1)

def calcular_preco_total(item, qtd):
    preco_unitario = produtos_disponiveis[item]
    return preco_unitario * qtd

valor_total = calcular_preco_total(item_escolhido, quantidade)

st.metric(label="Total da Compra", value=f"R$ {valor_total:.2f}")

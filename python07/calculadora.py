import streamlit as st 

st.title('** Math APP **')
st.header('Aplicação para calculos matematicos')

numero1 = st.number_input('1º numero: ')
numero2 = st.number_input('2º numero: ')
mathfunction = st.selectbox('Selecione a função', ['Soma', 'Subtração', 'Multiplicação', 'Divisão'])

if st.button('Start', type='primary'):
    if mathfunction == 'Soma':
        soma = numero1 + numero2
        st.success(f'Resultado: {soma}')
    elif mathfunction == 'Subtração':
      subtracao = numero1 - numero2
      st.success(f'Resultado: {subtracao}')
    elif mathfunction == 'Multiplicação':
      multiplicacao = numero1*numero2
      st.success(f'Resultado: {multiplicacao}')
    elif mathfunction == 'Divisão':
      divisao = numero1/numero2
      st.success(f'Resultado: {divisao}')
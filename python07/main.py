import streamlit as st

st.write('Hello World!')
st.write('Primeira aplicação com streamlit')

st.title('Bem vindo ao painel')
st.header('Isso é um cabeçalho')

st.success('Mensagem de sucesso!')
st.info('Mensagem de info')
st.warning('Mensagem de aviso')
st.error('Mensagem de erro')

nome = st.text_input('Digite o seu nome: ')
idade = st.number_input('Digite a sua idade: ', step=1, min_value=1, max_value=120)
curso_selecionado = st.selectbox('Selecione o seu curso', ['Python', 'Django', 'FastApi'])
descricao = st.text_area('Informe uma descrição: ')
termos = st.checkbox('Aceito os termos')
genero = st.radio('Selecione o genero', ['Masculino', 'Feminino'], horizontal=True)

if st.button('Enviar', type='primary'):
    st.success('Dados cadastrados com sucesso!')
    st.write(f'Nome: {nome}')
    st.write(f'Idade: {idade}')
    st.write(f'Curso: {curso_selecionado}')
    st.write(f'Descrição: {descricao}')
    st.write(f'Genero: {genero}')
    if termos:
      st.info('Os termos foram aceitos!')
    else:
      st.error('Os termos não foram aceitos!')
      
alunos = [
    {'Nome': 'Jubileu da Silva', 'Idade': 20, 'Curso': 'FastApi', 'Descrição': 'Primeiro ano'},
    {'Nome': 'PH', 'Idade': 25, 'Curso': 'FastApi', 'Descrição': 'Segundo ano'},
    {'Nome': 'Romeu', 'Idade': 18, 'Curso': 'Django', 'Descrição': 'Primeiro ano'},
]

st.table(alunos)

aba_cadastro, aba_matricula, aba_cursos, aba_professores = st.tabs(['Cadastro', 'Matriculas', 'Cursos', 'Professores'])
with aba_cadastro:
    st.title('Página de cadastro')
    
with aba_matricula:
    st.title('Página de matricula')
    
cursos = []
with aba_cursos:
    st.title('Página de cursos')
    nome_curso = st.text_input('Digite o nome do curso: ')
    tempo_estimado = st.number_input('Digite o tempo estimado: ', step=1)
    if st.button('Cadastrar', type='primary'):
        novo_curso = {'Nome': nome_curso, 'Tempo estimado': tempo_estimado}
        cursos.append(novo_curso)
        st.success('Curso cadastrado com sucesso!')
        
    st.table(cursos)

professores = []
with aba_professores:
    st.title('Página de Professores')
    nome_professor = st.text_input('Digite o nome do professor: ')
    modalidade_professor = st.text_input('Digite a modalidade: ')
    
    if st.button('Cadastrar professor', type='primary'):
      novo_professor = {'Nome': nome_professor, 'Modalidade': modalidade_professor}
      professores.append(novo_professor)
    
    st.table(professores)
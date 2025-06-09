import streamlit as st
import os

st.set_page_config(
        page_title="Bob Educa",
        page_icon="👨‍🎓",
        layout="centered",
        initial_sidebar_state="expanded",
    )

st.title("Bob-Educa 👨‍🎓")

st.markdown("""
### O que é o Bob-Educa?

Esse é o Bob, o professor mais duvidoso da internet.  
Você manda um **PDF ou PowerPoint**, ele estuda tudo rapidinho,  
e responde **com muita simpatia e amor**, com vídeos animados e fundo de **parkour do Minecraft** já que você não consegue prestar atenção hoje em dia!  

Mas relaxa, o Bob vai te explicar!  
""")

st.markdown("---")

uploaded_file = st.file_uploader("📂 Envie seu PDF ou PowerPoint aqui", type=["pdf", "ppt", "pptx"])

if uploaded_file:
    # Criar uma pasta temporária se ainda não existir
    os.makedirs("uploaded_docs", exist_ok=True)

    # Salvar o arquivo enviado
    file_path = os.path.join("uploaded_docs", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Documento '{uploaded_file.name}' enviado com sucesso!")
    st.info("Bob vai estudar esse conteúdo e preparar o show... 🎬💥")
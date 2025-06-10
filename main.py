import streamlit as st
import os
from document_processing.extractor import extract_text_from_pdf, extract_text_from_ppt
import openai  
from bob import bob_responde

st.set_page_config(
        page_title="Bob Educa",
        page_icon="👨‍🎓",
        layout="centered",
        initial_sidebar_state="expanded",
    )

#openai.api_key = st.secrets.get("OPENAI_API_KEY")
openai.api_key = st.secrets["OPENROUTER_API_KEY"]

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
    
    if uploaded_file.name.endswith(".pdf"):
        content = extract_text_from_pdf(file_path)
    else:
        content = extract_text_from_ppt(file_path)

    if content:
        st.markdown("### 👀 O Bob leu o seguinte conteúdo:")
        st.text_area("Texto extraído:", content, height=300)

        st.subheader("💬 Pergunte algo para o Bob:")
        user_question = st.text_input("Digite sua pergunta aqui 👇")

        if st.button("🎤 Perguntar para o Bob"):
            if user_question.strip():
                with st.spinner("Bob tá pensando... e xingando também 🧠💢"):
                    response = bob_responde(user_question, content)
                    st.markdown("### 🤬 Resposta do Bob:")
                    st.success(response)
            else:
                st.warning("Digite uma pergunta antes de clicar!")
    else:
        st.error("❌ Não foi possível extrair texto do documento.")
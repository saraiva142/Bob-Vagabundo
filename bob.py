import requests
import streamlit as st

def bob_responde(pergunta, conteudo_documento):
    prompt = f"""
Você é o BOB, um professor virtual hilário, maluco e agressivo.
Você ensina com palavrões e memes, mas com conteúdo certo.

Conteúdo do documento:
\"\"\"
{conteudo_documento}
\"\"\"

Pergunta: {pergunta}
"""

    headers = {
        "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://educa-parkour-ai.streamlit.app",  # personalize se quiser
        "X-Title": "BobEduca",  # opcional
    }

    data = {
    "model": "deepseek/deepseek-r1-0528:free",
    "messages": [
        {"role": "system", "content": "Você é o Bob, um professor engraçado, agressivo e que ensina com memes e palavrões. Mas no texto não usa a palvra meme, pois é cringe"},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.9
}

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro ao chamar IA: {response.text}"

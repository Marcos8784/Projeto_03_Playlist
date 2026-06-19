import streamlit as st

musicas = {
    "MC VINE7": {
        "na reliquia do 2T": "https://www.youtube.com/watch?v=rIuKKV06CZA&list=RDrIuKKV06CZA&start_radio=1",
        "Artigo de Grife":"https://www.youtube.com/watch?v=5yWeij5KAmI"
   
    },
    "MC Ryan SP": {
        "Sereno da Madrugada ": "https://www.youtube.com/watch?v=KV48hAUGLKY",
        "Tubarão Gigante":"https://www.youtube.com/watch?v=rBgEpYrkiI0"
    },
    "MC FR da Norte": {
        "Ligação Perdida": "https://www.youtube.com/watch?v=d0LXPKUiwx0",
         "Memphis Depay":"https://www.youtube.com/watch?v=8go8KPe9hXg&list=RDEM9SWbkzVN90V1ca1wY-xiBQ&start_radio=1"
    },
}
st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("selecione o artista" , musicas.keys())
musica_artista = musicas[artista]
st.title(artista)
video, sobre = st.tabs(['video','sobre'])
with video :
 for musica in musica_artista.items():
    titulo,link = musica
    st.subheader(titulo)
    st.video(link)
with sobre :
 if artista == "MC VINE7":
   st.markdown("""
## 🎤 MC VINE7

MC VINE7 é um artista que transforma experiências, sentimentos e vivências em música. 
Com uma identidade marcante e uma sonoridade própria, busca unir batidas envolventes, 
letras autênticas e muita energia para criar uma conexão verdadeira com seu público.

Misturando influências do **funk, trap e rap**, MC VINE7 representa uma nova geração 
da música urbana, trazendo atitude, criatividade e dedicação em cada lançamento.

Sua missão é levar sua arte cada vez mais longe, criando músicas que transmitam emoção, 
inspirem pessoas e deixem sua marca na cena musical.

🎶 **Gêneros:** Funk • Trap • Rap • Hip Hop

🔥 **MC VINE7 — uma voz, uma história, um legado.**
""")
 elif  artista == "MC Ryan SP":
  st.markdown("""
## 🎤 MC Ryan SP

MC Ryan SP é um dos grandes nomes da nova geração do funk brasileiro. 
Conhecido por sua presença marcante, letras envolventes e estilo autêntico, 
o artista conquistou seu espaço na cena musical com músicas que refletem 
a realidade, as conquistas e as histórias das ruas.

Com uma mistura de **funk paulista, trap e influências do rap**, MC Ryan SP 
cria sons com muita personalidade, conectando suas experiências com milhões 
de ouvintes. Sua trajetória é marcada por grandes lançamentos, parcerias de 
sucesso e uma forte conexão com seu público.

O artista representa a força do funk de São Paulo, levando sua música para 
diferentes lugares e mostrando sua evolução constante dentro da indústria musical.

🎶 **Gêneros:** Funk • Trap • Rap Nacional

🔥 **MC Ryan SP — talento, vivência e atitude que fazem parte da nova história do funk brasileiro.**
""") 
 else: 
  st.markdown("""
## 🎤 MC FR da Norte

MC FR da Norte é um artista que representa a força e a identidade da música 
das quebradas. Com uma trajetória marcada pela dedicação e pela busca constante 
por evolução, o artista leva para suas músicas histórias, sentimentos e a 
realidade vivida nas ruas.

Com uma sonoridade que mistura **funk, trap e rap**, MC FR da Norte apresenta 
um estilo próprio, trazendo batidas marcantes, letras de impacto e muita 
personalidade em cada lançamento.

Sua música busca conectar pessoas, transmitir experiências e mostrar a cultura 
da periferia através da arte, mantendo suas raízes e construindo seu espaço 
na cena musical.

🎶 **Gêneros:** Funk • Trap • Rap Nacional

🔥 **MC FR da Norte — representando sua essência, sua história e a força da música urbana.**
""")

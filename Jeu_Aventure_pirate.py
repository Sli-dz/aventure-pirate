import streamlit as st
# Configuration de la page
st.set_page_config(page_title="Aventure Pirate", page_icon="🏴‍☠️", layout="centered")
# Initialisation des variables
if "étape" not in st.session_state:
   st.session_state.étape = 0
if "score" not in st.session_state:
   st.session_state.score = 0
# Fonction pour recommencer
def recommencer():
   st.session_state.étape = 0
   st.session_state.score = 0
# Affiche le score en haut
st.markdown(f"<div style='text-align:center; color:#FFD700; font-size:18px;'>Score : {st.session_state.score}/10</div>", unsafe_allow_html=True)
# Styles CSS
st.markdown(
   """
<style>
       body {
           background-color: #001f3f;
       }
       .stButton>button {
           background-color: #8B0000;
           color: white;
           border-radius: 10px;
           height: 3em;
           width: 100%;
           font-size: 16px;
       }
       .stRadio label {
           font-size: 18px;
           color: #FFE4B5;
       }
       .stMarkdown h1, h2, h3 {
           color: #FFD700;
       }
</style>
   """,
   unsafe_allow_html=True
)
# MENU PRINCIPAL
if st.session_state.étape == 0:
   st.title("🏴‍☠️ Aventure Pirate")
   st.image("https://cdn.pixabay.com/photo/2013/07/12/14/36/pirate-148280_960_720.png", width=200)
   st.markdown("**Bienvenue moussaillon !** Une légende raconte qu’un trésor maudit est caché sur l’île de la Mort. "
               "Tu dois faire les bons choix pour espérer le trouver…")
   if st.button("Commencer l'aventure"):
       st.session_state.étape = 1
# Étapes 1 à 10
elif st.session_state.étape == 1:
   st.markdown("Tu débarques sur l'île. Devant toi : une jungle sombre ou une plage déserte.")
   choix = st.radio("Quel chemin prends-tu ?", ["", "La jungle", "La plage"])
   if st.button("Valider"):
       if choix == "La jungle":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Un piège t’attendait sur la plage…")
           recommencer()
elif st.session_state.étape == 2:
   st.markdown("Tu entends un bruit. Un singe tient une carte. Tu…")
   choix = st.radio("Que fais-tu ?", ["", "Lui parler doucement", "Essayer de lui prendre la carte", "Ignorer le singe"])
   if st.button("Valider"):
       if choix == "Lui parler doucement":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le singe s'enfuit avec la carte !")
           recommencer()
elif st.session_state.étape == 3:
   st.markdown("Tu trouves une grotte, mais l’entrée est piégée.")
   choix = st.radio("Comment entrer ?", ["", "Analyser les symboles", "Forcer l’entrée", "Lancer une pierre"])
   if st.button("Valider"):
       if choix == "Analyser les symboles":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Le piège s’active !")
           recommencer()
elif st.session_state.étape == 4:
   st.markdown("À l’intérieur, un squelette tient une clé.")
   choix = st.radio("Tu :", ["", "Prends doucement la clé", "Pousses le squelette", "Cries pour voir s’il réagit"])
   if st.button("Valider"):
       if choix == "Prends doucement la clé":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Un mécanisme se déclenche.")
           recommencer()
elif st.session_state.étape == 5:
   st.markdown("Tu tombes dans une salle avec 3 coffres.")
   choix = st.radio("Lequel ouvres-tu ?", ["", "Le coffre en or", "Le coffre en bois", "Le coffre poussiéreux"])
   if st.button("Valider"):
       if choix == "Le coffre poussiéreux":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("C'était un piège !")
           recommencer()
elif st.session_state.étape == 6:
   st.markdown("Une énigme est gravée au mur : 'Je grandis sans vie, j’ai des racines invisibles. Qui suis-je ?'")
   choix = st.radio("Réponse :", ["", "Une montagne", "Une idée", "Un fantôme"])
   if st.button("Valider"):
       if choix == "Une montagne":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("La salle s’effondre...")
           recommencer()
elif st.session_state.étape == 7:
   st.markdown("Un pirate fantôme t’interroge : 'Quel est le nom de mon navire ?'")
   choix = st.radio("Réponse :", ["", "Le Kraken", "L’Ombre Noire", "La Perle Oubliée"])
   if st.button("Valider"):
       if choix == "L’Ombre Noire":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Mauvaise réponse ! Il te maudit.")
           recommencer()
elif st.session_state.étape == 8:
   st.markdown("Tu trouves un passage secret, mais il faut entrer un code.")
   choix = st.radio("Quel code semblera le bon ?", ["", "1715", "1492", "1666"])
   if st.button("Valider"):
       if choix == "1715":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Code erroné !")
           recommencer()
elif st.session_state.étape == 9:
   st.markdown("Tu arrives à un lac souterrain. Une barque t’attend.")
   choix = st.radio("Tu :", ["", "Montes doucement", "Cries pour voir si c’est sûr", "Lances une torche dans l’eau"])
   if st.button("Valider"):
       if choix == "Montes doucement":
           st.session_state.étape += 1
           st.session_state.score += 1
       else:
           st.error("Tu déclenches une réaction étrange dans l’eau.")
           recommencer()
elif st.session_state.étape == 10:
   st.balloons()
   st.success("TU AS RÉUSSI ! Le trésor est à toi, capitaine !")
   st.markdown(f"**Score final : {st.session_state.score}/10**")
   st.image("https://cdn.pixabay.com/photo/2014/04/03/11/50/treasure-312943_960_720.png", width=300)
   if st.button("Recommencer"):
       recommencer()
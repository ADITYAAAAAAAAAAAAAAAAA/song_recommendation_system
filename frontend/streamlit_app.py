import streamlit as st
st.set_page_config(page_title="Mood-Based Song Recommender 🎵", page_icon="🎶")

import requests

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



st.title("🎧 Mood-Based Song Recommender")

st.write("Enter how you're feeling, and get song recommendations based on your mood!")

user_input = st.text_input("How are you feeling today?", "")

if st.button("Get Recommendations"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Predicting mood and fetching recommendations..."):
            try:
                response = requests.post("http://127.0.0.1:5000/predict", json={"text": user_input})
                data = response.json()

                if "error" in data:
                    st.error(f"Error: {data['error']}")
                else:
                    st.success(f"Predicted Mood: {data['predicted_mood'].capitalize()}")

                    if data["recommended_songs"]:
                        st.subheader("🎵 Recommended Songs")
                        for song in data["recommended_songs"]:
                            st.write(f"**{song['track_name']}** by *{song['artists']}* ({song['mood']})")
                    else:
                        st.info("No songs found for this mood. Try a different expression!")

            except requests.exceptions.RequestException as e:
                st.error("Failed to connect to the backend API.")



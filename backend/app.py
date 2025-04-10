from flask import Flask, request, jsonify
import pandas as pd
import joblib
import traceback

app = Flask(__name__)

# Load trained components
model = joblib.load("model/mood_classifier.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

# Load labeled song data
songs_df = pd.read_csv("data/labeled_songs.csv")  # ✅ Update the path
songs_df['mood'] = songs_df['mood'].str.strip().str.lower()  # ✅ Clean moods


@app.route('/')
def index():
    return "🎵 Mood-based Song Recommendation API is running!"

@app.route('/predict', methods=['POST'])
def predict_mood():
    try:
        data = request.json
        user_input = data.get("text", "")

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Vectorize input
        input_vector = vectorizer.transform([user_input])

        # Predict mood
        prediction = model.predict(input_vector)
        predicted_label = label_encoder.inverse_transform(prediction)[0]

        # Map predicted label to mood in song dataset
        mood_mapping = {
            "joy": "happy",
            "anger": "energetic",
            "sadness": "sad",
            "neutral": "calm",
            "fear": "calm",
            "surprise": "energetic"
        }
        mapped_mood = mood_mapping.get(predicted_label, predicted_label)

        # Filter songs
        filtered_songs = songs_df[songs_df['mood'].str.lower() == mapped_mood.lower()]

        if filtered_songs.empty:
            return jsonify({
                "predicted_mood": mapped_mood,
                "recommended_songs": [],
                "message": "No songs found for this mood"
            })

        top_songs = filtered_songs.sample(n=min(5, len(filtered_songs)))
        song_list = top_songs[["track_name", "artists", "mood"]].to_dict(orient="records")

        return jsonify({
            "predicted_mood": mapped_mood,
            "recommended_songs": song_list
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


    
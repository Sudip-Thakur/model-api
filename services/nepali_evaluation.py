import os
from transformers import pipeline
from utils.computation import compute_letter_correctness, compute_similarity
import librosa

# Load Nepali speech recognition model
nepali_recognizer = pipeline("automatic-speech-recognition", model="spktsagar/wav2vec2-large-xls-r-300m-nepali-openslr")

async def evaluate_nepali_pronunciation(audio, text):
    try:
        audio_path = f"/tmp/{audio.filename}"

        # Save uploaded file
        with open(audio_path, "wb") as f:
            content = await audio.read()
            f.write(content)

        # Process speech
        audio_data, sample_rate = librosa.load(audio_path, sr=16000)
        prediction = nepali_recognizer(audio_data)
        predicted_text = prediction['text']
        
        correctness = compute_letter_correctness(text, predicted_text)
        score = compute_similarity(text, predicted_text)

        result = {
            "transcribed_text": text,
            "student_transcription": predicted_text,
            "letters_correctness": correctness,
            "current_score": score
        }

        # Clean up temporary file
        os.remove(audio_path)

        return result

    except Exception as e:
        return {"error": str(e)}

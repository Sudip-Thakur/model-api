import os
from gradio_client import Client, handle_file

# Initialize Gradio API client
GRADIO_API_URL = "aletrn/ai-pronunciation-trainer"
gr_client = Client(GRADIO_API_URL)

async def evaluate_english_pronunciation(audio, text):
    try:
        audio_path = f"/tmp/{audio.filename}"

        # Save uploaded file
        with open(audio_path, "wb") as f:
            content = await audio.read()
            f.write(content)

        # Send request to AI Pronunciation Trainer API
        result = gr_client.predict(
            text=text,
            audio_rec=handle_file(audio_path),
            lang="en",
            score_de=0,
            score_en=0,
            api_name="/get_updated_score_by_language"
        )

        response_data = {
            "transcribed_text": result[0],
            "letters_correctness": result[1],
            "current_score": result[2],
            "student_phonetic_transcription": result[3],
            "ideal_phonetic_transcription": result[4],
        }

        # Clean up temporary file
        os.remove(audio_path)

        return response_data

    except Exception as e:
        return {"error": str(e)}

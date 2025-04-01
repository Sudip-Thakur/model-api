import Levenshtein

def compute_letter_correctness(expected_text, predicted_text):
    correctness = []
    expected_words = expected_text.split()
    predicted_words = predicted_text.split()

    for word_index, expected_word in enumerate(expected_words):
        predicted_word = predicted_words[word_index] if word_index < len(predicted_words) else ""
        word_correctness = ["1" if i < len(expected_word) and i < len(predicted_word) and expected_word[i] == predicted_word[i] else "0" for i in range(max(len(expected_word), len(predicted_word)))]
        correctness.append("".join(word_correctness))

    return " ".join(correctness)

def compute_similarity(expected_text, predicted_text):
    distance = Levenshtein.distance(expected_text, predicted_text)
    max_len = max(len(expected_text), len(predicted_text))
    similarity_score = (1 - distance / max_len) * 100  # Convert to percentage
    return round(similarity_score, 2)

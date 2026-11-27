def classify_words_by_vowels(words: list[str]) -> dict:
    result = {"kam": [], "o‘rta": [], "ko‘p": []}
    for word in words:
        count = sum(letter in "aeiou" for letter in word.lower())
        if count <= 1:
            result["kam"].append(word)
        elif count <= 3:
            result["o‘rta"].append(word)
        else:
            result["ko‘p"].append(word)
    return result

if __name__ == "__main__":
	words = ["python", "an", "education", "sky", "developer"]
	print(classify_words_by_vowels(words))

import random
from typing import List, Dict, Tuple


class VocabularyTrainer:
    def __init__(self, word_list: List[Dict[str, str]]):
        self.word_list = word_list
        self.score = 0
        self.total_words = len(word_list)

    def get_random_word(self) -> Dict[str, str]:
        return random.choice(self.word_list)

    def check_answer(self, word: Dict[str, str], user_answer: str) -> bool:
        return user_answer.lower() == word["translation"].lower()

    def run_quiz(self, num_questions: int) -> None:
        for _ in range(num_questions):
            word = self.get_random_word()
            print(f"\nTranslate this word: {word['english']}")
            user_answer = input("Your answer: ")

            if self.check_answer(word, user_answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. The correct answer is: {word['translation']}")

        print(f"\nQuiz finished! Your score: {self.score}/{num_questions}")


def main():
    word_list = [
        {"english": "Hello", "translation": "Hola"},
        {"english": "Goodbye", "translation": "Adiós"},
        {"english": "Thank you", "translation": "Gracias"},
        {"english": "Please", "translation": "Por favor"},
        {"english": "How are you?", "translation": "¿Cómo estás?"},
    ]

    trainer = VocabularyTrainer(word_list)
    trainer.run_quiz(5)


if __name__ == "__main__":
    main()

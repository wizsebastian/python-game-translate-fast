import random
from typing import List, Dict, Tuple


class VocabularyTrainer:
    def __init__(self, word_list: List[Dict[str, str]]):
        self.word_list = word_list
        self.score = 0
        self.total_words = len(word_list)

    def get_words_list(self) -> None:
        words_list = []
        file = open("words_baul.txt", "r")
        file_lines = file.readlines()

        for lines in file_lines:
            lines = lines.strip().split(",")
            item = {"en": lines[0], "es": lines[1], "level": lines[2]}
            words_list.append(item)

        file.close()
        return words_list

    def get_random_word(self) -> Dict[str, str]:
        return random.choice(self.word_list)

    def check_answer(self, word: Dict[str, str], user_answer: str) -> bool:
        return user_answer.lower() == word["es"].lower()

    def run_quiz(self, num_questions: int) -> None:
        for _ in range(num_questions):
            word = self.get_random_word()
            print(f"\nTranslate this word: {word['en']}")
            user_answer = input("Your answer: ")

            if self.check_answer(word, user_answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong. The correct answer is: {word['es']}")

        print(f"\nQuiz finished! Your score: {self.score}/{num_questions}")


def main():
    print("Hello! Welcome to the vocabulary trainer.")
    print(
        "You will be given a word in English and you have to translate it to Spanish."
    )
    print("Let's start!\n")
    input("Press Enter to continue...")
    print("\n")
    rounds = input("Select the level of difficulty: 0, 1, 2 or 3 to 5: ")
    questionsCount = input("Select the number of questions: ")
    # return
    # TODO: try to fix the flow to get the words and run the quizS
    trainer = VocabularyTrainer(word_list)
    word_list = trainer.get_words_list()
    # trainer.run_quiz(5)

    # print(lista)


if __name__ == "__main__":
    main()

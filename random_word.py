import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

# Функция для получения английского слова и его определения
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP (например, 404)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None  # Важно возвращать None при ошибке, чтобы избежать проблем в дальнейшем
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Функция для перевода текста на русский язык
def translate_to_russian(text):
    try:
        translation = translator.translate(text, dest="ru")
        return translation.text
    except Exception as e:
        print(f"Ошибка при переводе: {e}")
        return text  # Возвращаем оригинальный текст в случае ошибки

# Функция для игры в слова
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()

        if word_dict is None:  # Проверка на случай, если get_english_words вернула None из-за ошибки
            print("Не удалось получить слово. Попробуйте позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим определение слова на русский
        russian_definition = translate_to_russian(word_definition)

        print(f"Значение слова: {russian_definition}")  # Выводим определение на русском
        user = input("Что это за слово на английском? ")

        if user.lower() == word.lower(): # сравниваем введенное слово с загаданным в нижнем регистре
            print("Правильно!")
        else:
            print(f"Неверно, это слово - {word}")

        play_again = input('Хотите сыграть еще раз? y/n ')
        if play_again.lower() != "y": # сравниваем ввод пользователя с "y" в нижнем регистре
            print("Спасибо за игру!")
            break

word_game()
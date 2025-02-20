import wikipediaapi

def print_paragraphs(page):
        print(f"\nСтатья: {page.title}\n")
    for section in page.sections:
        print(section.title)
        print(section.text)
        print("-" * 40)

def main():
        user_agent = "MyWikiApp/1.0 (https://example.com; your_email@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(language='ru', user_agent=user_agent)

    try:
        while True:
            # Шаг 1: Запрашиваем у пользователя первоначальный запрос
            search_query = input("Введите свой запрос для поиска на Википедии (или 'выход' для завершения): ")
            if search_query.lower() == "выход":
                print("Выход из программы.")
                break

            # Шаг 2: Переход к первоначальному запросу в Википедии
            page = wiki_wiki.page(search_query)
            if not page.exists():
                print("Статья не найдена. Попробуйте другой запрос.")
                continue

            # Шаг 3: Предлагаем пользователю выбор действий
            while True:
                print("\nВыберите действие:")
                print("1. Листать параграфы статьи")
                print("2. Перейти на одну из связанных страниц")
                print("3. Выйти в главное меню")

                choice = input("Введите номер действия (1-3): ")

                if choice == "1":
                    print_paragraphs(page)
                elif choice == "2":
                    # Получаем связанные страницы
                    print("\nСвязанные страницы:")
                    links = page.links  # Получаем связанные страницы
                    link_list = list(links.keys())  # Получаем имена связанных страниц
                    for i, link_title in enumerate(link_list[:5], start=1):  # показываем только первые 5
                        print(f"{i}. {link_title}")

                    link_choice = input("\nВыберите номер связанной страницы (или 'выход' для возврата): ")
                    if link_choice.lower() == 'выход':
                        break

                    try:
                        link_index = int(link_choice) - 1
                        if 0 <= link_index < len(link_list):
                            page = wiki_wiki.page(link_list[link_index])  # Переход на выбранную связанную страницу
                        else:
                            print("Некорректный номер.")
                    except ValueError:
                        print("Введите корректное число.")
                elif choice == "3":
                    break
                else:
                    print("Некорректный ввод. Пожалуйста, введите 1, 2 или 3.")
    except KeyboardInterrupt:
        print("\nВыход из программы по запросу пользователя.")

if __name__ == "__main__":
    main()

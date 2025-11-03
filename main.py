class Section:
    def __init__(self, id, title, pages, doc_id):
        self.id = id
        self.title = title
        self.pages = pages  
        self.doc_id = doc_id

class Document:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SectionDocument:
    def __init__(self, doc_id, section_id):
        self.doc_id = doc_id
        self.section_id = section_id

documents = [
    Document(1, "Документ по безопасности"),
    Document(2, "Технический документ"),
    Document(3, "Руководство пользователя"),
    Document(4, "Архивный документ"),
]

sections = [
    Section(1, "Актуальные сведения", 5, 1),
    Section(2, "Общие сведения", 10, 1),
    Section(3, "Установка", 8, 2),
    Section(4, "Архив", 12, 2),
    Section(5, "Анализ данных", 6, 3),
    Section(6, "Приложение", 4, 4),
]

sections_documents = [
    SectionDocument(1, 1),
    SectionDocument(1, 2),
    SectionDocument(2, 3),
    SectionDocument(2, 4),
    SectionDocument(3, 5),
    SectionDocument(4, 6),
    SectionDocument(3, 1),
    SectionDocument(4, 2),
]


def main():
    one_to_many = []
    for d in documents:
        for s in sections:
            if s.doc_id == d.id:
                one_to_many.append((s.title, s.pages, d.name))

    many_to_many = []
    for sd in sections_documents:
        for d in documents:
            if d.id == sd.doc_id:
                for s in sections:
                    if s.id == sd.section_id:
                        many_to_many.append((s.title, s.pages, d.name))

    print("Задание В1:")
    for title, pages, doc_name in one_to_many:
        if title.startswith("А"):
            print(title, "-", doc_name)

    print("\nЗадание В2:")
    res = []
    for d in documents:
        doc_sections = [s for s in one_to_many if s[2] == d.name]
        if len(doc_sections) > 0:
            min_pages = min([p for _, p, _ in doc_sections])
            res.append((d.name, min_pages))
    res.sort(key=lambda x: x[1])
    for r in res:
        print(r[0], "-", r[1])

    print("\nЗадание В3:")
    many_to_many.sort(key=lambda x: x[0])
    for title, pages, doc_name in many_to_many:
        print(title, "-", doc_name)


if __name__ == "__main__":
    main()
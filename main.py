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

def get_sections_starting_with(letter, sections, documents):
    result = []
    for s in sections:
        if s.title.startswith(letter):
            for d in documents:
                if s.doc_id == d.id:
                    result.append((s.title, d.name))
    return result

def get_documents_with_min_pages(sections, documents):
    result = []
    for d in documents:
        pages_list = [s.pages for s in sections if s.doc_id == d.id]
        
        if pages_list:
            result.append((d.name, min(pages_list)))
            
    return sorted(result, key=lambda x: x[1])

def get_sections_and_documents_many_to_many(sections, documents, sections_documents):
    result = []
    for sd in sections_documents:
        for s in sections:
            for d in documents:
                if sd.section_id == s.id and sd.doc_id == d.id:
                    result.append((s.title, d.name))
    
    return sorted(result, key=lambda x: x[0])


if __name__ == "__main__":
    print("Задание В1:")
    res_b1 = get_sections_starting_with("А", sections, documents)
    for title, doc_name in res_b1:
        print(f"{title} - {doc_name}")

    print("\nЗадание В2:")
    res_b2 = get_documents_with_min_pages(sections, documents)
    for doc_name, min_p in res_b2:
        print(f"{doc_name} - {min_p}")

    print("\nЗадание В3:")
    res_b3 = get_sections_and_documents_many_to_many(sections, documents, sections_documents)
    for title, doc_name in res_b3:
        print(f"{title} - {doc_name}")

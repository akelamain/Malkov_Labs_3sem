import unittest
from main import (Section, Document, SectionDocument, 
                  get_sections_starting_with, 
                  get_documents_with_min_pages, 
                  get_sections_and_documents_many_to_many)


class TestSectionDocumentLogic(unittest.TestCase):
    def setUp(self):
        self.documents = [
            Document(1, "Документ А"),
            Document(2, "Документ Б"),
            Document(3, "Документ В")
        ]

        self.sections = [
            Section(1, "Анализ", 10, 1),       
            Section(2, "Введение", 5, 1),      
            Section(3, "Архитектура", 20, 2),  
            Section(4, "База данных", 15, 3),  
            Section(5, "Алгоритм", 8, 1)       
        ]

        self.sections_documents = [
            SectionDocument(1, 1),
            SectionDocument(1, 2),
            SectionDocument(2, 3),
            SectionDocument(3, 4),
            SectionDocument(1, 5) 
        ]

    def test_sections_starting_with_A(self):
        result = get_sections_starting_with("А", self.sections, self.documents)
        expected = [
            ("Анализ", "Документ А"),
            ("Архитектура", "Документ Б"),
            ("Алгоритм", "Документ А")
        ]
        self.assertEqual(result, expected)

    def test_min_pages_by_document(self):
        result = get_documents_with_min_pages(self.sections, self.documents)
        expected = [
            ("Документ А", 5),
            ("Документ В", 15),
            ("Документ Б", 20)
        ]
        self.assertEqual(result, expected)

    def test_many_to_many_relationship(self):
        result = get_sections_and_documents_many_to_many(
            self.sections, self.documents, self.sections_documents
        )
        
        expected = [
            ("Алгоритм", "Документ А"),
            ("Анализ", "Документ А"),
            ("Архитектура", "Документ Б"),
            ("База данных", "Документ В"),
            ("Введение", "Документ А")
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

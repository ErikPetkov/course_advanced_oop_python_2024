from typing import List
from project.document import Document
from project.category import Category
from  project.topic import Topic

class Storage:
    def __init__(self):
        self.categories :List[Category] = []
        self.topics :List[Topic] = []
        self.documents :List[Document] = []

    def add_category(self,category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self,topic: Topic):
        if topic not in self.topics :
            self.topics.append(topic)


    def add_document(self,document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self,category_id: int, new_name: str):
        cat = next((c for c in self.categories if c.id == category_id),None)
        if cat:
            cat.name = new_name

    def edit_topic(self,topic_id: int, new_topic: str, new_storage_folder: str):
        top = next((t for t in self.topics if t.id == topic_id),None)
        if top:
            top.storage_folder = new_storage_folder
            top.topic = new_topic

    def edit_document(self,document_id: int, new_file_name: str):
        doc = next((d for d in self.documents if d.id == document_id),None)
        if doc:
            doc.file_name = new_file_name

    def delete_category(self,category_id: int, new_name: str):
        cat = next((c for c in self.categories if c.id == category_id),None)
        if cat:
            self.categories.remove(cat)

    def delete_topic(self,topic_id: int, new_topic: str, new_storage_folder: str):
        top = next((t for t in self.topics if t.id == topic_id),None)
        if top:
            self.topics.remove(top)

    def delete_document(self,document_id: int, new_file_name: str):
        doc = next((d for d in self.documents if d.id == document_id),None)
        if doc:
            self.documents.remove(doc)

    def get_document(self,document_id):
        doc = next((d for d in self.documents if d.id == document_id), None)
        if doc:
            return doc,document_id

    def __repr__(self):
        return "\n".join(self.documents)



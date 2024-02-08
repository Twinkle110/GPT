import sys
#sys.path.append(r'C:\Users\parcheem\OneDrive - Publicis Groupe\Documents1\OpenAI\retriever')
import os
#from retriever.retrieval import Retriever
from retrieval import Retriever

# Create a Controller class to manage document embedding and retrieval
class Controller:
    def __init__(self):
        self.retriever = None
        self.query = ""

    def embed_document(self, file):
        # Embed a document if 'file' is provided
        if file is not None:
            self.retriever = Retriever()
             # Check the file extension to determine the file type
            #file_extension = os.path.splitext(file.name)[1].lower()

            #if file_extension == ".pdf":
            # Create and add embeddings for PDF documents
                #self.retriever.create_and_add_embeddings(file.name)
            #elif file_extension in [".xlsx", ".xls"]:
            # Create and add embeddings for Excel documents
                #self.retriever.create_and_add_embeddings_excel(file.name)
            #else:
                #raise ValueError("Unsupported file format")
            # Create and add embeddings for the provided document file
            self.retriever.create_and_add_embeddings(file.name)

    def retrieve(self, query):
        # Retrieve text based on the user's query
        texts = self.retriever.retrieve_text(query)
        return texts  
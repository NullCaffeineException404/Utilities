from langchain.schema import Document

def load_sample_docs():
    return [
        Document(page_content="This policy covers accidental death up to ₹10,00,000 for individuals under 65 years of age."),
        Document(page_content="Coverage excludes injuries from extreme sports, substance abuse, and self-inflicted harm."),
        Document(page_content="Claims must be filed within 90 days of the incident with supporting medical documentation."),
    ]

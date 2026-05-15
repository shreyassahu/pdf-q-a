from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.environ.get("GOOGLE_API_KEY"))



def chunk_text(text):
    words = text.split()
    total_words = len(words)

    chunks = []

    i = 0
    last_ind = 500

    start = 0
    while start < total_words:
        end = start + 500
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start += 400
    
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunks
    )

    print(result.embeddings)




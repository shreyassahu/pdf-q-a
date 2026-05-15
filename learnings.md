## Project 2: PDF Q&A — Day 1

- `pdfplumber` extracts much cleaner text than PyPDF2 — PyPDF2 splits words with spaces
- FastAPI handles file uploads via `UploadFile` — access the file object with `file.file`
- FastAPI doesn't auto-redirect POST requests with trailing slash mismatches (unlike GET)
- Always use `https://` when hitting deployed services — `http://` causes a redirect that can convert POST to GET
- In Python, everything is an object including methods. In Java, methods live on the class vtable — objects store fields + a class pointer
- Second project setup was noticeably faster than the first — deployment muscle memory is building

## Project 2: PDF Q&A — Day 2

- Chunking: split text into ~500 word pieces with ~100 word overlap. Overlap ensures answers spanning chunk boundaries aren't lost
- Use a `while` loop for chunking, not `for` — you're stepping by a fixed amount (400 words), not iterating one-by-one. Python `for` loops ignore manual changes to the loop variable
- Embeddings convert text into a list of numbers (vector) that captures meaning. Similar text → similar vectors → close in vector space
- Google Gemini `gemini-embedding-001` returns 3072-dimensional vectors, free tier, no credit card needed
- You can embed multiple chunks in one API call by passing a list to `contents`
- `.env` files must be in `.gitignore` BEFORE the first commit, not after. Google aggressively scans for leaked API keys and revokes them instantly
- Always verify your app is loading the right key — `load_dotenv()` must be called before reading env vars

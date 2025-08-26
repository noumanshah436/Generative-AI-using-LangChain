from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# SemanticChunker tries to split text based on meaning rather than just size.

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3,
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)


"""
Got it 👍 Let me break down how **`SemanticChunker`** works in your example.

---

### 🔎 What `SemanticChunker` Does

Unlike simple text splitters (e.g., character or sentence-based), **`SemanticChunker`** tries to split text **based on meaning** rather than just size.

It uses **embeddings** (vector representations of text) to find points in the text where there's a **semantic shift** — meaning when the topic or context changes.

---

### ⚙️ How It Works Step by Step

1. **Embeddings Creation**

   * Each sentence (or small text span) in your input text is converted into a numerical vector using `OpenAIEmbeddings()`.
   * These vectors capture semantic meaning (so sentences about cricket are close to each other, but sentences about terrorism are far away).

2. **Similarity & Breakpoints**

   * The splitter looks at the similarity between consecutive chunks of text.
   * If the semantic difference is **large enough** (a "breakpoint"), it decides: "This is a good place to split."

3. **Breakpoint Thresholds**

   * In your code:

     ```python
     breakpoint_threshold_type="standard_deviation",
     breakpoint_threshold_amount=3,
     ```

     * It uses **statistical thresholds** (standard deviation of similarity scores).
     * If a sentence is **3 standard deviations** less similar to the previous flow, it creates a new chunk.

4. **Document Creation**

   * Finally, it returns a list of `Document` objects, each containing text that is **semantically coherent** (same topic/idea).

---

### 📝 In Your Example

Your text has 3 topics:

* 🌾 Farmers working in fields
* 🏏 Cricket (IPL)
* ⚠️ Terrorism

`SemanticChunker` will likely split this into **3 chunks** because the meaning shifts strongly between these parts.

---

✅ **In short:**
`SemanticChunker` uses **embeddings + similarity + statistical thresholds** to split text at **meaningful boundaries** instead of arbitrary lengths.

---

Do you want me to also **show the similarity scores step by step** for your `sample` text (so you can see where the breaks happen)?

"""
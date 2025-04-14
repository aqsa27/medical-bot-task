# medical-bot-task

This is my solution to the take-home Medical Assistant Bot assignment. I built an intelligent question-answering system that responds to medical questions using a retrieval-based approach. 

##  My Approach

To build the assistant, I chose a retrieval-based method. The dataset included over 16,000 medical question-answer pairs, so instead of generating new answers, I focused on retrieving the most relevant existing one.

I started by cleaning the dataset — removing any missing values, trimming extra spaces, and dropping duplicate questions. Then I used the `all-MiniLM-L6-v2` model from the `sentence-transformers` library to convert each Q+A pair into an embedding vector.

I stored these embeddings in a FAISS index, which makes it easy to quickly search and find the closest match to a user’s question. When someone types a question, the bot encodes it, searches the index, and returns the most relevant answer.

This approach keeps the answers grounded in real medical content and avoids the risk of the model making things up.

## Project Structure

Medical-Assistant-Bot-Assignment/
├── data/                            # Raw dataset goes here
│   └── mle_screening_dataset.csv
├── embeddings/                      # Where FAISS index + metadata live
│   ├── faiss_index.bin
│   └── qa_metadata.pkl
├── src/                             # All source code scripts
│   ├── build_index.py               
│   └── rag_bot.py                   
├── requirements.txt                 # Dependencies for reproducibility
├── README.md                        # Project overview and documentation
└── .gitignore                       


## 💬 Example Interactions 

Below are five questions that are semantically similar to examples in the dataset. These help demonstrate that the system can handle real-world, natural phrasing — not just exact question matches.

---

**Q1:** What does someone with anemia usually feel like?

**A:**


---

**Q2:** Why do people develop asthma?

**A:**


---

**Q3:** How can depression show up in someone’s day-to-day life?

**A:**


**Q4:** What kinds of treatments help manage high blood pressure?

**A:**


---

**Q5:** Does lupus affect different parts of the body?

**A:**


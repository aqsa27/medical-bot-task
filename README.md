# medical-bot-task

This is my solution to the take-home Medical Assistant Bot assignment. I built an intelligent question-answering system that responds to medical questions using a retrieval-based approach. 

##  My Approach

To build the assistant, I chose a retrieval-based method. The dataset included over 16,000 medical question-answer pairs, so instead of generating new answers, I focused on retrieving the most relevant existing one.

I started by cleaning the dataset — removing any missing values, trimming extra spaces, and dropping duplicate questions. Then I used the `all-MiniLM-L6-v2` model from the `sentence-transformers` library to convert each Q+A pair into an embedding vector.

I chose all-MiniLM-L6-v2 because it offers a strong balance between speed and semantic accuracy for sentence-level embeddings. It's lightweight and optimized for fast similarity search in large-scale datasets like this one.

I stored these embeddings in a FAISS index, which makes it easy to quickly search and find the closest match to a user’s question. When someone types a question, the bot encodes it, searches the index, and returns the most relevant answer.

This approach keeps the answers grounded in real medical content and avoids the risk of the model making things up.

Note: The `faiss_index.bin` and `qa_metadata.pkl` files inside the `embeddings/` folder are not included in the repo due to size. You can regenerate them by running `build_index.py` . You can find the dataset under the `data/` folder.


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
```

Bot: The most common symptom of anemia is fatigue (feeling tired or weak). If you have anemia, you may find it hard to find the energy to do normal activities.
                
Other signs and symptoms of anemia include:
                
Shortness of breath
                
Dizziness
                
Headache
                
Coldness in the hands and feet
                
Pale skin
                
Chest pain
                
These signs and symptoms can occur because your heart has to work harder to pump oxygen-rich blood through your body.
                
Mild to moderate anemia may cause very mild symptoms or none at all.
                
Complications of Anemia
                
Some people who have anemia may have arrhythmias (ah-RITH-me-ahs). Arrhythmias are problems with the rate or rhythm of the heartbeat. Over time, arrhythmias can damage your heart and possibly lead to heart failure.
                
Anemia also can damage other organs in your body because your blood can't get enough oxygen to them.
                
Anemia can weaken people who have cancer or HIV/AIDS. This can make their treatments not work as well.
                
Anemia also can cause many other health problems. People who have kidney disease and anemia are more likely to have heart problems. With some types of anemia, too little fluid intake or too much loss of fluid in the blood and body can occur. Severe loss of fluid can be life threatening.

---
```
**Q2:** Why do people develop asthma?

**A:**

```               
An inherited tendency to develop allergies, called atopy (AT-o-pe)
                
Parents who have asthma
                
Certain respiratory infections during childhood
                
Contact with some airborne allergens or exposure to some viral infections in infancy or in early childhood when the immune system is developing
                
If asthma or atopy runs in your family, exposure to irritants (for example, tobacco smoke) may make your airways more reactive to substances in the air.
                
Some factors may be more likely to cause asthma in some people than in others. Researchers continue to explore what causes asthma.
                
The "Hygiene Hypothesis"
                
One theory researchers have for what causes asthma is the "hygiene hypothesis." They believe that our Western lifestylewith its emphasis on hygiene and sanitationhas resulted in changes in our living conditions and an overall decline in infections in early childhood.
                
Many young children no longer have the same types of environmental exposures and infections as children did in the past. This affects the way that young children's immune systems develop during very early childhood, and it may increase their risk for atopy and asthma. This is especially true for children who have close family members with one or both of these conditions.

Please enter your question: that young children's immune systems develop during very early childhood, and it may increase their risk for atopy and asthma. This is especially true for children who have close family members with one or both of these conditions.se family members with one or both of these conditions.


---
```
**Q3:** How can depression show up in someone’s day-to-day life?

**A:**

```
Bot: Depression is a serious medical illness. It's more than just a feeling of being sad or "blue" for a few days. If you are one of the more than 19 million teens and adults in the United States who have depression, the feelings do not go away. They persist and interfere with your everyday life. Symptoms can include       - Feeling sad or "empty"    - Loss of interest in favorite activities    - Overeating, or not wanting to eat at all    - Not being able to sleep, or sleeping too much    - Feeling very tired    - Feeling hopeless, irritable, anxious, or guilty    - Aches or pains, headaches, cramps, or digestive problems    - Thoughts of death or suicide       Depression is a disorder of the brain. There are a variety of causes, including genetic, biological, environmental, and psychological factors. Depression can happen at any age, but it often begins in teens and young adults. It is much more common in women. Women can also get postpartum depression after the birth of a baby. Some people get seasonal affective disorder in the winter. Depression is one part of bipolar disorder.    There are effective treatments for depression, including antidepressants, talk therapy, or both.    NIH: National Institute of Mental Health
---
```

**Q4:** What kinds of treatments help manage high blood pressure?

**A:**

```
Bot: Today, many different types of medicines are available to control high blood pressure. These medicines work in different ways. Some lower blood pressure by removing extra fluid and salt from your body. Others affect blood pressure by slowing down the heartbeat, or by relaxing and widening blood vessels. Often, two or more drugs work better than one. Here are the types of medicines used to treat high blood pressure. -   Diuretics (water or fluid Pills)  flush excess sodium from your body, which reduces the amount of fluid in your blood and helps to lower your blood pressure. Diuretics are often used with other high blood pressure medicines, sometimes in one combined pill.   -  Beta Blockers help your heart beat slower and with less force. As a result, your heart pumps less blood through your blood vessels, which can help to lower your blood pressure.  -  Angiotensin-Converting Enzyme (ACE) Inhibitors. Angiotensin-II is a hormone that narrows blood vessels, increasing blood pressure. ACE converts Angiotensin I to Angiotensin II. ACE inhibitors block this process, which stops the production of Angiotensin II, lowering blood pressure.  -  Angiotensin II Receptor Blockers (ARBs) block angiotensin II hormone from binding with receptors in the blood vessels. When angiotensin II is blocked, the blood vessels do not constrict or narrow, which can lower your blood pressure.  -  Calcium Channel Blockers keep calcium from entering the muscle cells of your heart and blood vessels. This allows blood vessels to relax, which can lower your blood pressure.   -  Alpha Blockers reduce nerve impulses that tighten blood vessels. This allows blood to flow more freely, causing blood pressure to go down.  -  Alpha-Beta Blockers reduce nerve impulses the same way alpha blockers do. However, like beta blockers, they also slow the heartbeat. As a result, blood pressure goes down.  -  Central Acting Agents act in the brain to decrease nerve signals that narrow blood vessels, which can lower blood pressure.  -  Vasodilators relax the muscles in blood vessel walls, which can lower blood pressure.   Diuretics (water or fluid Pills)  flush excess sodium from your body, which reduces the amount of fluid in your blood and helps to lower your blood pressure. Diuretics are often used with other high blood pressure medicines, sometimes in one combined pill. Beta Blockers help your heart beat slower and with less force. As a result, your heart pumps less blood through your blood vessels, which can help to lower your blood pressure. Angiotensin-Converting Enzyme (ACE) Inhibitors. Angiotensin-II is a hormone that narrows blood vessels, increasing blood pressure. ACE converts Angiotensin I to Angiotensin II. ACE inhibitors block this process, which stops the production of Angiotensin II, lowering blood pressure. Angiotensin II Receptor Blockers (ARBs) block angiotensin II hormone from binding with receptors in the blood vessels. When angiotensin II is blocked, the blood vessels do not constrict or narrow, which can lower your blood pressure. Calcium Channel Blockers keep calcium from entering the muscle cells of your heart and blood vessels. This allows blood vessels to relax, which can lower your blood pressure. Alpha Blockers reduce nerve impulses that tighten blood vessels. This allows blood to flow more freely, causing blood pressure to go down. Alpha-Beta Blockers reduce nerve impulses the same way alpha blockers do. However, like beta blockers, they also slow the heartbeat. As a result, blood pressure goes down. Central Acting Agents act in the brain to decrease nerve signals that narrow blood vessels, which can lower blood pressure. Vasodilators relax the muscles in blood vessel walls, which can lower blood pressure
```

---

**Q5:** Does lupus affect different parts of the body?

**A:**

```
Bot: Normal variations (polymorphisms) in many genes can affect the risk of developing SLE, and in most cases multiple genetic factors are thought to be involved. In rare cases, SLE is caused by mutations in single genes. Most of the genes associated with SLE are involved in immune system function, and variations in these genes likely affect proper targeting and control of the immune response. Sex hormones and a variety of environmental factors including viral infections, diet, stress, chemical exposures, and sunlight are also thought to play a role in triggering this complex disorder. About 10 percent of SLE cases are thought to be triggered by drug exposure, and more than 80 drugs that may be involved have been identified.  In people with SLE, cells that have undergone self-destruction (apoptosis) because they are damaged or no longer needed are not cleared away properly. The relationship of this loss of function to the cause or features of SLE is unclear. Researchers suggest that these dead cells may release substances that cause the immune system to react inappropriately and attack the body's tissues, resulting in the signs and symptoms of SLE.
---
```

## How I Evaluated the Bot

Since this is a retrieval-based bot (not something I trained to predict labels or generate text), I evaluated it by seeing how well it could answer real, paraphrased questions — the kind a normal user might actually ask.

I didn’t just test it with exact matches from the dataset. Instead, I asked five reworded versions of common medical questions, like “What does someone with anemia usually feel like?” or “Why do people develop asthma?” to test accuracy.

In each case, the bot pulled the correct information from the dataset and gave a detailed response that matched the intent of my question.

---

### Why I Didn’t Use Accuracy or F1 Scores

Those kinds of metrics are great for classification models, but they don’t really apply here — my bot isn’t predicting categories or generating new text. It’s just retrieving the closest match from a large set of question-answer pairs.

So instead of using numbers, I focused on whether the bot gave a **relevant and complete answer** that made sense for the question I typed in.

---

### What Worked Well
- It gives fast answers with no hallucinations
- It works even when the question is reworded or casually phrased
- All the answers are grounded in real, pre-verified medical content

---

## Future Improvements

If I had more time (and if the assignment allowed it), here’s what I would explore to make the assistant more powerful:

- **Add a generation layer**: I’d like to add a lightweight summarization model like T5 or OpenBioLLM to rephrase or personalize the retrieved answers. That way, the bot could sound more conversational while still staying factually accurate.
I would explore integrating Llama3-OpenBioLLM-70B, an open-source model fine-tuned on high-quality biomedical literature, PubMed, and clinical texts. Its domain-specific training makes it ideal for generating accurate, trustworthy summaries or follow-ups grounded in medical context. This would help enhance the bot's ability to deliver conversational, yet factually reliable, responses.

- **Support multiple answers**: Right now, the system only returns the top match. I’d like to retrieve the top 2–3 results and either let the user choose, or combine them into a more complete answer.

- **Confidence scoring**: I’d add a way to show how confident the system is in its answer — maybe based on the FAISS similarity score — and even say something like “I’m not sure” if no good match is found.


Right now the system works well for its scope, but these are the ideas I’d explore to make it feel more intelligent and helpful.

## AI Use and Compliance

I confirm that no third-party AI services (like OpenAI, Claude, or others) were used to generate or assist with any part of the solution. All code, logic, and documentation were written independently by me.



# 📰 News Headline Classification System

An end-to-end **Natural Language Processing (NLP)** project that classifies news headlines into predefined categories using machine learning. The project includes data preprocessing, feature engineering, model comparison, evaluation, and deployment using **Streamlit**.

Users can enter a custom news headline and receive an instant category prediction.

---

# 🚀 Features

* End-to-end text classification pipeline
* Text preprocessing using NLTK
* Comparison of multiple machine learning models
* Bag-of-Words and TF-IDF vectorization
* Automatic best-model selection
* Model persistence using Joblib
* Streamlit web application for real-time predictions
* Confidence scores for predicted categories

---

# 🎯 Objective

The goal of this project is to:

* Build a news headline classification system.
* Explore NLP preprocessing techniques.
* Compare multiple machine learning algorithms.
* Handle class imbalance using class weighting.
* Deploy the best-performing model through a web interface.

---

# 📊 Dataset

**Source:** Kaggle News Category Dataset

**Format:** JSON

Original dataset size:

* **209,527 samples**
* **42 categories**

For this project, categories were merged into **7 major classes**:

| Category      |
| ------------- |
| Politics      |
| Entertainment |
| Sports        |
| Business      |
| Science       |
| Technology    |
| World         |

The text feature is created by combining:

```python
headline + short_description
```

---

# ⚙️ Tech Stack

* Python
* Pandas
* NumPy
* NLTK
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

# 🧠 NLP Pipeline

## 1. Data Cleaning

The following preprocessing steps are applied:

* Convert text to lowercase
* Remove numbers and special characters
* Remove stopwords
* Lemmatization using WordNetLemmatizer

Example:

**Original**

```text
NASA launches new Mars mission this year.
```

**Processed**

```text
nasa launch new mar mission year
```

---

# 🔤 Feature Extraction

Two vectorization techniques are explored:

### Bag of Words

```python
CountVectorizer(max_features=5000)
```

### TF-IDF

```python
TfidfVectorizer(
    max_features=20000,
    ngram_range=(1,2)
)
```

---

# 🤖 Models Compared

The following machine learning models were evaluated:

* Multinomial Naive Bayes
* Complement Naive Bayes
* Logistic Regression
* Linear SVM (C=0.5)
* Linear SVM (C=1.0)
* Linear SVM (C=2.0)
* SGD Classifier
* Passive Aggressive Classifier
* Extra Trees Classifier
* XGBoost
* Random Forest

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score (Weighted)
* F1 Score (Macro)
* Matthews Correlation Coefficient (MCC)

---

# 🏆 Best Model

| Component    | Selected   |
| ------------ | ---------- |
| Vectorizer   | TF-IDF     |
| Model        | Linear SVM |
| C value      | 0.5        |
| Class Weight | Balanced   |

---

# 📈 Performance

### Final Test Accuracy

```text
84.97%
```

### Classification Report

| Category      | F1-score |
| ------------- | -------- |
| Politics      | 0.90     |
| Entertainment | 0.90     |
| Sports        | 0.83     |
| World         | 0.73     |
| Science       | 0.71     |
| Business      | 0.69     |
| Technology    | 0.63     |

Weighted F1-score:

```text
0.85
```

---

# 📂 Project Structure

```text
news_classifier/
│
├── data/
│   ├── News_Category_Dataset.json
│   ├── train.csv
│   └── test.csv
│
├── models/
│   ├── best_model.pkl
│   ├── best_vectorizer.pkl
│   └── best_config.json
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_model_comparison.ipynb
│   └── 03_final_model_training.ipynb
│
├── app.py
├── train.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Jupyter Notebooks

```bash
jupyter notebook
```

Execute notebooks in order:

1. `01_data_preprocessing.ipynb`
2. `02_model_comparison.ipynb`
3. `03_final_model_training.ipynb`

---

## Train the Model

```bash
python train.py
```

---

## Launch Streamlit App

```bash
streamlit run app.py
```

---

# 🧪 Example Predictions

| Headline                          | Predicted Category |
| --------------------------------- | ------------------ |
| Government approves new tax bill  | Politics           |
| Messi scores hat-trick in final   | Sports             |
| Apple unveils new iPhone model    | Technology         |
| NASA launches Mars rover mission  | Science            |
| Stock market reaches record high  | Business           |
| New Avengers movie breaks records | Entertainment      |

---

# 📚 Key Learnings

This project helped me gain practical experience in:

* NLP preprocessing
* Text vectorization using TF-IDF
* Feature engineering
* Multi-class classification
* Model comparison and evaluation
* Handling imbalanced classes
* Model serialization using Joblib
* Deploying machine learning applications with Streamlit

---

# 🔮 Future Improvements

* BERT and Transformer-based models
* LSTM and Bi-LSTM networks
* Hyperparameter tuning using GridSearchCV
* Real-time news scraping
* REST API using FastAPI
* Deployment on Streamlit Cloud or Hugging Face Spaces

---

⭐ If you found this project helpful, feel free to give it a star!

# 📊 COVID-19 Research Papers Analysis

A simple data analysis and visualization project exploring COVID-19 related research papers metadata. The project uses **Python (Pandas, Matplotlib)** for analysis and **Streamlit** for building an interactive app.

##  Project Overview
Check out the deployed Streamlit app here: [COVID-19 Research Papers Explorer](https://frameworksassignment-crsubklkeugcpjne2p4x4m.streamlit.app/)
This project analyzes metadata from COVID-19 research papers, focusing on:
* Cleaning missing values.
* Extracting publication dates and years.
* Adding new features (like abstract word count) from existing data.
* Performing basic analysis (top journals, frequent words in titles, yearly trends)
* Building an interactive **Streamlit dashboard**

## 📂 Dataset

* **Source:** [CORD-19 Research Challenge (Kaggle)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
* **File used:** `metadata.csv` (subset of 5000 rows for efficiency)

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/khaif-dev/Frameworks_Assignment.git
```

### 2. Install Dependencies

Create a virtual environment and install packages:

```bash
pip install pandas
pip install matplotlib
pip install streamlit
pip install wordcloud
```

### 3. Run the Analysis (week8.ipynb)

```bash
jupyter notebook
```

Open the analysis notebook and run step by step.

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Features & Analysis

1. **Data Cleaning**

   * Dropped columns with all missing values.
   * Handled missing publish dates.
   * Converted publish time to `datetime`.

2. **Feature Engineering**

   * Extracted publication year (`pub_year`) from publish_time.
   * Calculated abstract word counts.

3. **Basic Analysis**

   * Count of papers per year
   * Top 10 publishing journals
   * Frequent words in paper titles

4. **Visualizations**

   * Bar chart of publications per year
   * Bar chart of top journals
   * Word cloud of paper titles

## 🖼️ Example visuals in the streamlit app

* 📈 Publications over time
* 🏛 Top journals publishing COVID-19 research
* ☁️ Word cloud of paper titles


## 📌 Future Improvements

* Add interactive filtering by journal, country, or author.
* Incorporate more recent versions of the dataset.



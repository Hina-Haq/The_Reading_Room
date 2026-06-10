<div align="center">
  <img src="./src/logo_dark.svg" alt="The Reading Room logo" width="180">

# The Reading Room

### An Unsupervised Machine Learning Book Recommender

A book recommender built with web scraping, API collection, unsupervised machine learning, and Streamlit.

**Team:** Gabriela Cascione · Hina Haq
</div>

---

## Project Overview

**The Reading Room** is a book recommender project that suggests books based on genre, description, and metadata similarity.

It combines web scraping, API collection, data cleaning, unsupervised machine learning, and a Streamlit app to create an interactive book discovery experience.

---

## The Problem

Readers face too many choices and often do not know where to start.

Many recommendation systems feel too generic, so this project explores whether book metadata and text similarity can produce more meaningful suggestions.

---

## Our Solution

We built a personalised book recommender using data collected from **Goodreads** and **Open Library**.

The project includes:
- a combined and cleaned dataset,
- unsupervised clustering,
- text-based similarity,
- and a Streamlit app for interactive exploration.

---

## Data

The final dataset contains **2,004 books**:
- **1,004 from Goodreads**
- **1,000 from Open Library**

The final cleaned and concatenated file used for the app is: **books_streamlit.csv**

---

## Machine Learning Approach

This project uses **unsupervised machine learning**.

Main steps:
- **TF-IDF** for book descriptions,
- **PCA** for dimensionality reduction,
- **MultiLabelBinarizer** for genre encoding,
- **MinMaxScaler** for numeric features,
- **K-Means** for clustering.

The final model uses **K-Means with k=6**.

---

## The App

The app is designed to let users:
- search for a book they already like,
- get similar recommendations,
- browse by genre,
- receive a random recommendation,
- and open Goodreads or Google Books links.

---

## Project Structure

```text
The_Reading_Room/
│
├── 01. Data/
│   ├── books_cleaned.csv
│   ├── books_combined.csv
│   ├── books_streamlit.csv
│   ├── books_with_clusters.csv
│   ├── goodreads_1000_full.csv
│   └── openlibrary_1000.csv
│
├── 02. Notebooks/
│   ├── API_scraping.ipynb
│   ├── Concat_feature_fixing_reading_room.ipynb
│   ├── Database_Streamlit_Cleaning.ipynb
│   ├── Prep_and_ML.ipynb
│   ├── Web_scraping.ipynb
│   ├── trials_scraping.ipynb
│   └── app.py
│
├── src/
│   └── logo_dark.svg
│
├── the_reading_room_presentation.pptx
└── README.md
```


---

## Links

- **Deployed Streamlit App:** [Add app link here]
- **Presentation:** [Add presentation link here]


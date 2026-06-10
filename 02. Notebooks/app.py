import streamlit as st
import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page config 
st.set_page_config(
    page_title="The Reading Room",
    page_icon="📚",
    layout="wide")

st.markdown("""
<style>
    .stApp {
        background-color: #F1EFE8;
    }
    .navbar {
        background-color: #0C447C;
        padding: 1.2rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }
    .navbar-title {
        font-family: Georgia, serif;
        font-size: 2rem;
        color: #EF9F27;
        font-weight: bold;
        margin: 0;
    }
    .navbar-sub {
        font-size: 0.75rem;
        color: #B5D4F4;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin: 0;
    }
    .tagline {
        font-family: Georgia, serif;
        font-size: 0.85rem;
        color: #0C447C;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    h1, h2, h3 {
        font-family: Georgia, serif;
        color: #0C447C;
    }
    .stSelectbox > div > div {
        background-color: white;
        border-color: #185FA5;
    }
    .stButton > button {
        background-color: #0C447C;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-family: Georgia, serif;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background-color: #185FA5;
        color: white;
    }
    .stLinkButton > a {
        background-color: #F1EFE8;
        color: #0C447C !important;
        border: 1px solid #0C447C;
        border-radius: 8px;
    }
    .stLinkButton > a:hover {
        background-color: #B5D4F4;
        color: #0C447C !important;
    }
    [data-testid="stImage"] {
        height: 280px;
        overflow: hidden;
    }
    [data-testid="stImage"] img {
        height: 280px !important;
        width: 100% !important;
        object-fit: cover !important;
    }
    [data-testid="stExpander"] {
        border: 1px solid #B5D4F4;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="navbar" style="display:flex; align-items:center; gap:1rem;">
    <div style="background:#EF9F27; border-radius:8px; width:45px; height:45px; 
                display:flex; flex-direction:column; justify-content:center; 
                align-items:center; gap:5px; padding:8px; flex-shrink:0;">
        <div style="background:#0C447C; height:3px; width:80%; border-radius:2px;"></div>
        <div style="background:#0C447C; height:3px; width:80%; border-radius:2px;"></div>
        <div style="background:#0C447C; height:3px; width:80%; border-radius:2px;"></div>
        <div style="background:#0C447C; height:3px; width:50%; border-radius:2px; align-self:flex-start; margin-left:10%;"></div>
    </div>
    <div>
        <p class="navbar-title">The Reading Room</p>
        <p class="navbar-sub">Book Recommender</p>
    </div>
</div>
<p class="tagline">Your next great read awaits</p>
""", unsafe_allow_html=True)


# Load data 
df = pd.read_csv("01. Data/books_streamlit.csv")

# Upgrade cover image quality
df["cover_img_url"] = df["cover_img_url"].str.replace("-M.jpg", "-L.jpg", regex=False)

# Clean bad descriptions
df["description"] = df["description"].apply(
    lambda x: None if pd.notna(x) and str(x).startswith("Duplicate of") else x)

# Build TF-IDF similarity matrix 
df["content"] = df["genres_clean"].fillna("") + " " + df["description"].fillna("")
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
tfidf_matrix = tfidf.fit_transform(df["content"])
similarity_matrix = cosine_similarity(tfidf_matrix)

# Helper function — show short description with read more
def show_description(text):
    if pd.isna(text) or text is None:
        return
    words = str(text).split()
    if len(words) <= 15:
        st.markdown(" ".join(words))
    else:
        short = " ".join(words[:15])
        st.markdown(short + "...")
        with st.expander("Read more"):
            chunks = [text[i:i+500] for i in range(0, len(text), 500)]
            for chunk in chunks:
                st.markdown(chunk)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; margin-bottom:1rem;">
        <img src="https://media.giphy.com/media/3o84U1nWRzyqOEOKpa/giphy.gif" 
             style="width:70%; border-radius:8px;">
    </div>
    <p style="font-family:Georgia,serif; font-size:17px; font-style:italic; color:#0C447C; margin:0">
        "A book is a dream you hold in your hands."
    </p>
    <p style="color:#EF9F27; font-weight:500; font-size:13px; margin:6px 0 0">— Neil Gaiman</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    messages = [
        "Pick my next read — I dare you! 🎲",
        "I'm feeling lucky 🎲",
        "Let fate choose my next book ✨",
        "Spin the bookshelf 🎡",
        "Mystery pick from the shelf 📚",
        "Bookish roulette 🎲",
        "I trust the algorithm 🤖",
        "A book I didn't know I needed 💎"
    ]

    st.markdown("### Discover by Genre")
    all_genres = ["All"] + sorted(set(
        genre.strip()
        for genres in df["genres_clean"].dropna()
        for genre in genres.split(",")
    ))
    selected_genre = st.selectbox("Pick a genre", options=all_genres, index=0)

    if selected_genre == "All":
        button_label = "Let the Universe Decide 🔮"
    else:
        button_label = random.choice(messages)
    if selected_genre == "All":
        button_label = "Let the Universe Decide 🔮"
    else:
        if "button_label" not in st.session_state or st.session_state.get("last_genre") != selected_genre:
            st.session_state.button_label = random.choice(messages)
            st.session_state.last_genre = selected_genre
        button_label = st.session_state.button_label

    random_book = None
    if st.button(button_label):
        if selected_genre == "All":
            st.session_state.random_book = df.sample(1).iloc[0]
        else:
            filtered = df[df["genres_clean"].str.contains(selected_genre, na=False)]
            if filtered.empty:
                st.warning(f"No books found in {selected_genre}")
                st.session_state.random_book = None
            else:
                st.session_state.random_book = filtered.sample(1).iloc[0]

    if "random_book" in st.session_state and st.session_state.random_book is not None:
        rb = st.session_state.random_book
        st.image(rb["cover_img_url"] if pd.notna(rb["cover_img_url"]) else "no_cover_placeholder.png", width=150)
        st.markdown(f"**{rb['title']}**")
        st.markdown(f"{rb['author']}")
        if pd.notna(rb["avg_rating"]):
            st.markdown(f"⭐ {rb['avg_rating']:.1f}")
        if pd.notna(rb.get("goodreads_url")):
            st.link_button("View on GoodReads", rb["goodreads_url"])
        elif pd.notna(rb.get("google_url")):
            st.link_button("View on Google Books", rb["google_url"])

    st.markdown("---")

    st.markdown("### About")
    st.markdown("""
    This app is based on a dataset of **2,004 books** collected 
    from GoodReads and Open Library. It is part of a student 
    data analytics project and is not intended for commercial use.
    """)

# ── Search box ───────────────────────────────────────────────
selected_title = st.selectbox(
    "Search for a book you love",
    options=sorted(df["title"].tolist()),
    index=None,
    placeholder="Type a book title..."
)

if selected_title:

    book = df[df["title"] == selected_title].iloc[0]

    st.subheader("Your book:")
    col1, col2 = st.columns([1, 3])

    with col1:
        if pd.notna(book["cover_img_url"]):
            st.image(book["cover_img_url"], width=150)
        else:
            st.image("src/no_cover_placeholder.png", width=200)

    with col2:
        st.markdown(f"### {book['title']}")
        st.markdown(f"by **{book['author']}**")
        if pd.notna(book["year_published"]):
            st.markdown(f"First Published: {int(book['year_published'])}")
        if pd.notna(book["avg_rating"]):
            st.markdown(f"⭐ {book['avg_rating']}")
        else:
            st.markdown("⭐ N/A")
        st.markdown(f"*{book['genres_clean']}*")
        show_description(book["description"])
        if pd.notna(book.get("goodreads_url")):
            st.link_button("View on GoodReads", book["goodreads_url"])
        elif pd.notna(book.get("google_url")):
            st.link_button("View on Google Books", book["google_url"])

    how_many = st.slider(
        "How many recommendations?",
        min_value=1,
        max_value=9,
        value=3,
        step=1)

    show_recommendations = st.button("Take Me To My Next Adventure 📚")

    if show_recommendations:
        st.subheader("Recommended for you:")

        idx = df[df["title"] == selected_title].index[0]
        scores = list(enumerate(similarity_matrix[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:20]
        random.shuffle(scores)
        scores = scores[:how_many]
        rec_indices = [i[0] for i in scores]
        recommendations = df.iloc[rec_indices]

        if recommendations.empty:
            st.warning("No recommendations found.")
        else:
            cols = st.columns(3)
            for i, (_, rec) in enumerate(recommendations.iterrows()):
                with cols[i % 3]:
                    if pd.notna(rec["cover_img_url"]):
                        st.image(rec["cover_img_url"], use_container_width=True)
                    else:
                        st.image("no_cover_placeholder.png", use_container_width=True)

                    st.markdown(f"""
                        <div style="height:55px; overflow:hidden; font-weight:bold; font-size:16px;">
                            {rec['title']}
                        </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                        <div style="height:25px; overflow:hidden; font-size:14px; color:#555;">
                            {rec['author']}
                        </div>
                    """, unsafe_allow_html=True)

                    if pd.notna(rec["year_published"]):
                        st.markdown(f"First Published: {int(rec['year_published'])}")
                    if pd.notna(rec["avg_rating"]):
                        st.markdown(f"⭐ {rec['avg_rating']:.1f}")
                    else:
                        st.markdown("⭐ N/A")

                    if pd.notna(rec["description"]):
                        words = str(rec["description"]).split()
                        short = " ".join(words[:12])
                        st.markdown(f"""
                            <div style="height:25px; overflow:hidden; font-size:14px; color:#555;">
                                {short}...
                            </div>
                        """, unsafe_allow_html=True)
                        with st.expander("Read more"):
                            chunks = [str(rec["description"])[i:i+500] for i in range(0, len(str(rec["description"])), 500)]
                            for chunk in chunks:
                                st.markdown(chunk)

                    if pd.notna(rec.get("goodreads_url")):
                        st.link_button("View on GoodReads", rec["goodreads_url"])
                    elif pd.notna(rec.get("google_url")):
                        st.link_button("View on Google Books", rec["google_url"])
                    st.markdown("---")

# ── Footer ───────────────────────────────────────────────────
st.markdown("<br>" * 15, unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#666; font-size:0.8rem; padding:1rem;">
    © 2026 The Reading Room · All Rights Reserved<br>
    Created by Gabriela Cascione & Hina Haq · 
    Ironhack Data Analytics Bootcamp
</div>
""", unsafe_allow_html=True)
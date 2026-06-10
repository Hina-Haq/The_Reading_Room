# The Reading Room — Brand Guidelines

> Book Recommender Project · Visual Identity Reference

---

## Logo

Two versions available in `/assets/`:

| File | Usage |
|---|---|
| `logo_dark.svg` | Dark backgrounds, navy sections, hero areas |
| `logo_light.svg` | Light backgrounds, white sections, default use |

**Logo elements:**
- Book icon — lines representing text on a page
- Separator line — divides company name from tagline
- Tagline — *BOOK RECOMMENDER*

**Do not** stretch, recolor, or remove any logo element.

---

## Color Palette

| Name | Hex | Usage |
|---|---|---|
| Navy | `#0C447C` | Primary — backgrounds, headings, buttons |
| Ocean | `#185FA5` | Secondary — links, borders, hover states |
| Gold | `#EF9F27` | Accent — highlights, icons, CTAs |
| Parchment | `#F1EFE8` | Background — page bg, light sections |
| Sky | `#B5D4F4` | Highlight — tags, badges, subtle accents |

### Streamlit config (`~/.streamlit/config.toml`)

```toml
[theme]
primaryColor = "#EF9F27"
backgroundColor = "#F1EFE8"
secondaryBackgroundColor = "#E6F1FB"
textColor = "#0C447C"
font = "serif"
```

---

## Typography

| Role | Font | Size | Weight |
|---|---|---|---|
| Headings | Georgia, serif | 24–32px | 700 |
| Subheadings | Georgia, serif | 18–22px | 700 |
| Body | System Sans | 15–16px | 400 |
| Labels & tags | System Sans | 12–13px | 500 |
| Tagline | Georgia, serif | 12–13px | 400, letter-spacing 3px |

---

## Voice & Tone

- Warm, welcoming, literary
- Knowledgeable but not pretentious
- Encourages discovery and curiosity

**Tagline:** *Your next great read awaits*

---

## App UI Guidelines

- Use **Parchment** (`#F1EFE8`) as the main background
- Use **Navy** (`#0C447C`) for all primary headings
- Use **Gold** (`#EF9F27`) for buttons, highlights, and star ratings
- Use **Ocean** (`#185FA5`) for links and secondary actions
- Use **Sky** (`#B5D4F4`) for genre tags and badges
- Book cards: white background, subtle border, rounded corners
- Avoid pure black — use Navy for dark text instead

---

## File Structure (suggested)

```
the-reading-room/
├── assets/
│   ├── logo_dark.svg
│   ├── logo_light.svg
│   └── brand_guidelines.md
├── data/
├── notebooks/
└── app/
    └── streamlit_app.py
```

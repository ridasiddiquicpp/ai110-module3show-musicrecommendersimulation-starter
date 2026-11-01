# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Algorithm Recipe:
  +2.0  if genre matches the user's favorite_genre
  +1.0  if mood matches the user's favorite_mood
  +2.0 × (1 − |song.energy − target_energy|)   ← closer energy = more points
  +1.0 × (1 − |song.valence − target_valence|)
  +0.5 × (1 − |song.acousticness − target_acousticness|)
  

Then: sort all songs by score, highest first, and return the top k.

...............................................

potential biases are...
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 19

Top 5 recommendations
============================================================

#1  Sunrise City by Neon Echo
    Score: 5.56 / 6.50 (86%)
    Reasons:
      - genre match (pop) +2.0
      - mood match (happy) +1.0
      - energy 0.82 vs target 0.8 +1.96
      - valence 0.84 vs target 0.2 +0.36
      - acousticness 0.18 vs target 0.7 +0.24

#2  Gym Hero by Max Pulse
    Score: 4.34 / 6.50 (67%)
    Reasons:
      - genre match (pop) +2.0
      - energy 0.93 vs target 0.8 +1.74
      - valence 0.77 vs target 0.2 +0.43
      - acousticness 0.05 vs target 0.7 +0.18

#3  Rooftop Lights by Indigo Parade
    Score: 3.63 / 6.50 (56%)
    Reasons:
      - mood match (happy) +1.0
      - energy 0.76 vs target 0.8 +1.92
      - valence 0.81 vs target 0.2 +0.39
      - acousticness 0.35 vs target 0.7 +0.33

#4  Night Drive Loop by Neon Echo
    Score: 2.87 / 6.50 (44%)
    Reasons:
      - energy 0.75 vs target 0.8 +1.90
      - valence 0.49 vs target 0.2 +0.71
      - acousticness 0.22 vs target 0.7 +0.26

#5  Iron Requiem by Black Anvil
    Score: 2.81 / 6.50 (43%)
    Reasons:
      - energy 0.97 vs target 0.8 +1.66
      - valence 0.22 vs target 0.2 +0.98
      - acousticness 0.04 vs target 0.7 +0.17

============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this




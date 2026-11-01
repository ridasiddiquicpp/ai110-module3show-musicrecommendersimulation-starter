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

Real-world recommenders, like Spotify or YouTube use two type of filtering, collaborative and content-based.

Collaborative filtering looks at your behaviour and matches it with other users who have similar behavior. If you and other users played the same songs, then it would recommend songs that those users liked that you haven't heard yet.

Content-based filtering looks at the actual items features, like genre, mood, or certain keywords, and then uses that to find similar items. So if the user listens to certain song, this system will find songs similar in genre, mood, or other features.

These systems work in 3 stages: 
It collects input data, which are things like song features and user history, such as likes, listening time, skips, etc

User preferences are a summary of that history, basically a profile that tells the system what the user likes.

Ranking is when the system scores every song against that profile, sorts the scores, and show the top results. 

My version uses content-based filtering. It scores each song by comparing its genre, mood, energy, valence, and acousticness to the user's profile. It prioritizes genre and energy.


Some prompts to answer:

- What features does each `Song` use in your system

    Each song has genre, mood, energy, tempo_bpm, valence, danceability, and acousticness, along with the id, title, and artist. 

- What information does your `UserProfile` store

    The UserProfile stores a favorite genre and mood and target values for energy, valence, and acousticness

- How does your `Recommender` compute a score for each song

    The scoring works by comparing a song to the profile and adding points

    This is the scoring breakdown (Algorithm Recipe):
      +2.0  if genre matches the user's favorite_genre
      +1.0  if mood matches the user's favorite_mood
      +2.0 × (1 − |song.energy − target_energy|)   ← closer energy = more points
      +1.0 × (1 − |song.valence − target_valence|)
      +0.5 × (1 − |song.acousticness − target_acousticness|)

    The maximum score is 6.5. The points for mood and genre are only given if there is exact matches. 
    Energy, valence, and acousticness give partial points, so closer values on the user profile get a higher score.

    Potential biases include:
    The system might over prioritize genre and mood because they are both 3 points combined out of 6.5 points. 

    Genre and mood require exact matches, which doesn't give related genres or moods a chance.

- How do you choose which songs to recommend

    The system recommend songs by first scoring every song in the songs.csv file against the user profile. Then it sorts the scores from highest to lowest, and return the top k (default is 5) songs, with a list of reasons explaining the score. 

You can include a simple diagram or bullet list if helpful.



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

## Output for Different Profiles

User Profile #1:
```
user_prefs = {"favorite_genre": "classical", "favorite_mood": "melancholic", "target_energy": 0.2, "target_valence": 0.2,"target_acousticness": 0.7}
```

Output #1:
```
Top 5 recommendations
============================================================

#1  Moonlit Sonata Remix by Elena Voss
    Score: 4.95 / 6.50 (76%)
    Reasons:
      - genre match (classical) +2.0
      - energy 0.18 vs target 0.2 +1.96
      - valence 0.58 vs target 0.2 +0.62
      - acousticness 0.97 vs target 0.7 +0.36

#2  Autumn Letters by Willow & Pine
    Score: 4.08 / 6.50 (63%)
    Reasons:
      - mood match (melancholic) +1.0
      - energy 0.31 vs target 0.2 +1.78
      - valence 0.29 vs target 0.2 +0.91
      - acousticness 0.93 vs target 0.7 +0.38

#3  Blue Monday Rain by Delta Smoke
    Score: 3.06 / 6.50 (47%)
    Reasons:
      - energy 0.39 vs target 0.2 +1.62
      - valence 0.24 vs target 0.2 +0.96
      - acousticness 0.74 vs target 0.7 +0.48

#4  Spacewalk Thoughts by Orbit Bloom
    Score: 2.78 / 6.50 (43%)
    Reasons:
      - energy 0.28 vs target 0.2 +1.84
      - valence 0.65 vs target 0.2 +0.55
      - acousticness 0.92 vs target 0.7 +0.39

#5  Library Rain by Paper Lanterns
    Score: 2.72 / 6.50 (42%)
    Reasons:
      - energy 0.35 vs target 0.2 +1.70
      - valence 0.6 vs target 0.2 +0.60
      - acousticness 0.86 vs target 0.7 +0.42
============================================================
```


User Profile #2:
```
user_prefs = {"favorite_genre": "classical", "favorite_mood": "angry", "target_energy": 0.97, "target_valence": 0.2, "target_acousticness": 0.04}
```

Output #2:
```
Top 5 recommendations
============================================================

#1  Iron Requiem by Black Anvil
    Score: 4.48 / 6.50 (69%)
    Reasons:
      - mood match (angry) +1.0
      - energy 0.97 vs target 0.97 +2.00
      - valence 0.22 vs target 0.2 +0.98
      - acousticness 0.04 vs target 0.04 +0.50

#2  Moonlit Sonata Remix by Elena Voss
    Score: 3.08 / 6.50 (47%)
    Reasons:
      - genre match (classical) +2.0
      - energy 0.18 vs target 0.97 +0.42
      - valence 0.58 vs target 0.2 +0.62
      - acousticness 0.97 vs target 0.04 +0.04

#3  Storm Runner by Voltline
    Score: 3.07 / 6.50 (47%)
    Reasons:
      - energy 0.91 vs target 0.97 +1.88
      - valence 0.48 vs target 0.2 +0.72
      - acousticness 0.1 vs target 0.04 +0.47

#4  Gym Hero by Max Pulse
    Score: 2.85 / 6.50 (44%)
    Reasons:
      - energy 0.93 vs target 0.97 +1.92
      - valence 0.77 vs target 0.2 +0.43
      - acousticness 0.05 vs target 0.04 +0.49

#5  Neon Pulse Festival by Circuit Bloom
    Score: 2.75 / 6.50 (42%)
    Reasons:
      - energy 0.95 vs target 0.97 +1.96
      - valence 0.9 vs target 0.2 +0.30
      - acousticness 0.03 vs target 0.04 +0.49

============================================================
```

User Profile #3:
```
user_prefs = {"favorite_genre": "metal", "favorite_mood": "peaceful", "target_energy": 0.95, "target_valence": 0.9, "target_acousticness": 0.95}
```

Output #3:
```
Top 5 recommendations
============================================================

#1  Iron Requiem by Black Anvil
    Score: 4.33 / 6.50 (67%)
    Reasons:
      - genre match (metal) +2.0
      - energy 0.97 vs target 0.95 +1.96
      - valence 0.22 vs target 0.9 +0.32
      - acousticness 0.04 vs target 0.95 +0.05

#2  Neon Pulse Festival by Circuit Bloom
    Score: 3.04 / 6.50 (47%)
    Reasons:
      - energy 0.95 vs target 0.95 +2.00
      - valence 0.9 vs target 0.9 +1.00
      - acousticness 0.03 vs target 0.95 +0.04

#3  Gym Hero by Max Pulse
    Score: 2.88 / 6.50 (44%)
    Reasons:
      - energy 0.93 vs target 0.95 +1.96
      - valence 0.77 vs target 0.9 +0.87
      - acousticness 0.05 vs target 0.95 +0.05

#4  Sunrise City by Neon Echo
    Score: 2.79 / 6.50 (43%)
    Reasons:
      - energy 0.82 vs target 0.95 +1.74
      - valence 0.84 vs target 0.9 +0.94
      - acousticness 0.18 vs target 0.95 +0.11

#5  Rooftop Lights by Indigo Parade
    Score: 2.73 / 6.50 (42%)
    Reasons:
      - energy 0.76 vs target 0.95 +1.62
      - valence 0.81 vs target 0.9 +0.91
      - acousticness 0.35 vs target 0.95 +0.20

============================================================
```
---



## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users


    In a user profile, which was classical and angry, Moonlit Sonata, which is a quiet classical song, ranked second. This was ranked ahead of Gym Hero that had higher energy (closer to the user profiles energy). So the genre outweighed the energy and possibly created a biased result. 


    I experimented and changed the weights to compare the results. I changed genre from 2.0 to 1.0 points, energy from 2.0 to 1.5 points, valence from 1.0 to 1.5 points, and acousticness from 0.5 to 1.0 point.

    For the classical and angry user profile (with energy 0.97), the second recommended song went from Moonlit Sonata to Storm Runner, which has a similar energy level. I feel like this change balanced the values out, rather than giving more important to genre.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

Some limitations are that it doesn't have song language in the dataset, so if the user likes songs in a language other than English, there is no way in the current dataset for that.

Another limitation is that genre and mood have a heavy influence on if the song will be scores highly. Genre and mood combined (3 points) outweigh any possible energy gap (1.5 points). So a song can score high based on labels even if the sound is not a good fit.


---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this




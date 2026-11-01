import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts with numeric fields converted."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user profile and return (score, reasons)."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append(f"genre match ({song['genre']}) +2.0")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append(f"mood match ({song['mood']}) +1.0")

    energy_points = 2.0 * (1 -abs(song["energy"] - user_prefs["target_energy"]))
    score += energy_points
    reasons.append(f"energy {song['energy']} vs target {user_prefs['target_energy']} +{energy_points:.2f}")

    valence_points = 1.0 * (1 -abs(song["valence"] - user_prefs["target_valence"]))
    score += valence_points
    reasons.append(f"valence {song['valence']} vs target {user_prefs['target_valence']} +{valence_points:.2f}")

    acoustic_points = 0.5 * (1 -abs(song["acousticness"] - user_prefs["target_acousticness"]))
    score += acoustic_points
    reasons.append(f"acousticness {song['acousticness']} vs target {user_prefs['target_acousticness']} +{acoustic_points:.2f}")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k as (song, score, explanation), best first."""
    scored = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]

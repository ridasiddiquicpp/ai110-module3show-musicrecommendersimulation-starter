"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print("Loaded songs: " + str(len(songs)))


    # Starter example profile
    #user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8, "target_valence": 0.2,"target_acousticness": 0.7}

    #1
    #user_prefs = {"favorite_genre": "classical", "favorite_mood": "melancholic", "target_energy": 0.2, "target_valence": 0.2,"target_acousticness": 0.7}
    
    #2 - genre and mood match different songs
    #user_prefs = {"favorite_genre": "classical", "favorite_mood": "angry", "target_energy": 0.97, "target_valence": 0.2, "target_acousticness": 0.04}

    #3 - contradictory vibe
    #user_prefs = {"favorite_genre": "metal", "favorite_mood": "peaceful", "target_energy": 0.95, "target_valence": 0.9, "target_acousticness": 0.95}

    #4 - uses the new features: late-night studying, instrumental, 2020s, niche songs
    #user_prefs = {"favorite_genre": "lofi", "favorite_mood": "focused", "target_energy": 0.4, "target_valence": 0.55, "target_acousticness": 0.75,
    #              "favorite_language": "none", "favorite_decade": 2020, "preferred_vocals": "instrumental", "target_popularity": 50, "favorite_activity": "study"}

    #5 - uses the new features: workout with vocals, mainstream hits, 2010s
    #user_prefs = {"favorite_genre": "pop", "favorite_mood": "intense", "target_energy": 0.93, "target_valence": 0.7, "target_acousticness": 0.1,
    #              "favorite_language": "english", "favorite_decade": 2010, "preferred_vocals": "vocal", "target_popularity": 90, "favorite_activity": "workout"}

    #6 - language preference: a Spanish-language listener who wants upbeat party music
    user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.7, "target_valence": 0.85, "target_acousticness": 0.3,
                  "favorite_language": "spanish", "favorite_decade": 2020, "preferred_vocals": "vocal", "target_popularity": 70, "favorite_activity": "party"}

    # Maximum possible score: 6.5 for the original features, plus each new feature the profile asks for
    max_score = 6.5
    for key, bonus in (("favorite_language", 1.0), ("favorite_decade", 0.5), ("preferred_vocals", 0.5),
                       ("target_popularity", 0.5), ("favorite_activity", 1.0)):
        if key in user_prefs:
            max_score += bonus

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\nTop {len(recommendations)} recommendations")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} by {song['artist']}")
        percentage = score / max_score * 100
        print(f"    Score: {score:.2f} / {max_score:.2f} ({percentage:.0f}%)")
        print("    Reasons:")
        for reason in explanation.split("; "):
            print(f"      - {reason}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

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
    user_prefs = {"favorite_genre": "classical", "favorite_mood": "angry", "target_energy": 0.97, "target_valence": 0.2, "target_acousticness": 0.04}
    
    #3 - contradictory vibe
    #user_prefs = {"favorite_genre": "metal", "favorite_mood": "peaceful", "target_energy": 0.95, "target_valence": 0.9, "target_acousticness": 0.95}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\nTop {len(recommendations)} recommendations")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} by {song['artist']}")
        percentage = score / 6.5 * 100
        print(f"    Score: {score:.2f} / 6.50 ({percentage:.0f}%)")
        print("    Reasons:")
        for reason in explanation.split("; "):
            print(f"      - {reason}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

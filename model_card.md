# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

MusicMatcher

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender gives song recommendation from a small dataset based on the user's preferences. Given a favorite genre, a favorite mood, and target values for energy, valence, and acousticness, it scores every song and returns the top 5.

The recommender assumes that the user's music tastes can be described by genre, mood, energy, valence, and acousticness. The system doesn't learn from the user's music history, likes, or skips. It also assumes that every user wants to listen to songs that are similar to their profile and not have much variety.

This is a classroom project to see how recommender's works, not for real users. The dataset is quite small and the system isn't able to learn from the user's choices, such as liking a song, or replaying it, so it's not very accurate for real use.


---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  

    The features for a song that are used are genre, mood, energy, tempo_bpm, valence, danceability, and acousticness

- What user preferences are considered

    The user preferences that are considered are genre, mood, energy, valence, and acousticness


- How does the model turn those into a score  

    Every song in the dataset gets scored by how well it matches the users choices

    A song gets 2 points if the genre matches the user's favorite genre.
    It gets 1 point if the mood matches
    For energy, valence, and acousticness, the closer the song is to the user's preferred energy, valence, and acousticness, the more points it gets.

    Energy is worth up to 2 points
    Valence is worth up to 1 point
    Acousticness is worth up to 0.5 point
    Then these points are added up to a total of 6.5

    The system counts points for each song. Then it sort them from highest to lowest points, and recommends the top 5 songs.
    

- What changes did you make from the starter logic  

    The starter logic only returned the first few songs in the list without scoring them. 

    So I built the scoring system and used the points I mentioned above to rank the songs, and then return the most relevant ones. 
    I also chose the weight myself, choosing genre and mood combined to be the most relevant.


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  

    There are 19 songs in the catalog

- What genres or moods are represented  

    There are 16 genres, including pop, indie pop, lofi, rock, metal, ambient, jazz, hip hop, and classical
    Lofi has 3 songs and pop has 2, and the other 14 genres have 1 each. 

    There are 15 moods, including happy, chill, intense, relaxed, moody, peaceful, romantic, euphoric, and melancholic. 
    Most moods appear on only one song.

- Did you add or remove data  

    Yes, I added 9 songs to catalog. The songs after line 11 in the songs.csv are the ones I added. I put some songs with different genres and moods than were in the catalog before, including hip hop, classical, country and more. 

- Are there parts of musical taste missing in the dataset  

    Yes, there are many parts of musical taste missing in the dataset. There are no songs in K-pop songs or Latin songs and many more. 


---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  

    The system gives reasonable results when a user's preferences agree with each other, meaning their genre, mood, and
    sound targets all point the same way.
    For example, a pop and happy listener with high energy got Sunrise City first. It matched on genre, mood, and energy.

- Any patterns you think your scoring captures correctly  

    Matching on genre or mood gives the most points, so a song that fits the user's labels ranks higher on the list.


- Cases where the recommendations matched your intuition  

    In some of the user profiles the top result was one I would have picked myself.
    Like for this user preferences:
    user_prefs = {"favorite_genre": "classical", "favorite_mood": "melancholic", "target_energy": 0.2, "target_valence": 0.2,"target_acousticness": 0.7}

    I got  Moonlit Sonata Remix by Elena Voss, which is what I picked as well.


---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  


Some biases are that genre and mood have a heavy influence on if the song will be scored highly. Genre and mood combined (3 points) outweigh any possible energy gap (1.5 points). So a song can score high based on labels even if the sound is not a good fit.

Every song in the dataset that has acousticness 0.7 or higher has energy 0.48 or lower. So users who want acoustic but energetic music can't get any relevant songs

Since genre and mood rely on exact matches to give points, related genres or moods get no partial credit and possibly don't get recommended to the user.

For improving the system, genre can be changed to 1 point.

For improving even more and make scoring more accurate, I think a dictionary can be used to define how the genres relate to one another and give weights through that. This would make genre and mood not rely on exact matches

Something like this table can be used:
GENRE_SIMILARITY = {
    "pop":       {"indie pop": 0.7, "r&b": 0.4, "edm": 0.4, "synthwave": 0.3},
    "indie pop": {"pop": 0.7, "folk": 0.4},
    "rock":      {"metal": 0.6, "indie pop": 0.3},
    "metal":     {"rock": 0.6},
    "lofi":      {"ambient": 0.6, "jazz": 0.5, "classical": 0.3},
    "ambient":   {"lofi": 0.6, "classical": 0.5},
    "jazz":      {"blues": 0.6, "lofi": 0.5, "r&b": 0.4},
    ....
}


---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  

    I ran four profiles and compared the top 5 for each:
    - A pop and happy listener (the starter example) with high energy.

    - A classical and melancholic listener with low energy and high acousticness.

    - A classical and angry listener with very high energy. Here the genre and the mood point to different songs, which tests how the two compete.

    - A metal and peaceful listener who wants high energy, high valence, and high acousticness. These preferences contradict each other on purpose.


- What you looked for in the recommendations  

    In the recommendations I looked for if the top song actually matched the vibe of the user's profile. Basically, if I would have picked that from the dataset.
    And looked at if the rest of the list was in similar territory as the user profile.



- What surprised you  

    In the user profile, which was classical and angry, Moonlit Sonata, which is a quiet classical song, ranked second. This was ranked ahead of Gym Hero that had higher energy (closer to the user profiles energy). So the genre outweighed the energy and possibly created a biased result. 


- Any simple tests or comparisons you ran  

    I checked each recommendation's reasons against the song's data to make sure the score matched the rule. 

    I also changed the weights and compared the results.
    I changed genre from 2.0 to 1.0 points,
    energy from 2.0 to 1.5 points,
    valence from 1.0 to 1.5 points
    and acousticness from 0.5 to 1.0 point

    For the classical and angry user profile (with energy 0.97), the second recommended song went from Moonlit Sonata to Storm Runner, which has a similar energy level. I feel like this change balanced the values out, rather than giving more important to genre.



---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  

    I think letting users define a range for certain features, like energy, instead of a single number could be good.

    Use a dictionary or table to know which genres are related, so if a user's favorite genre is pop, a song that is indie pop also gets a point.

- Better ways to explain recommendations  

    To improve the recommendation explanation, I think one way is to have a simple one-line summary on top of the points/reasons breakdown, explaining why the song is ranked like that.

- Improving diversity among the top results  

    One idea to improve diversity among top results is to recommend one song that doesn't fit the user's favorite genre but still fits the overall sound, such as energy, etc.


- Handling more complex user tastes  

    I think one way to do this is by letting the user add multiple favorite genres to their profile. 

    Also learning user preferences from their behavior, like replaying, skipping, or liking a song would help understand the user's preferences better. 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I already had learned a bit about collaborative filtering, and content-based filtering. And had a basic understanding of how recommender systems work in the real-world, like on Spotify and Netflix.

One interesting thing I found was how much a single weight changes the system. So I think that is something that should be very carefully chosen.


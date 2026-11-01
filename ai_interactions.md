# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

I asked the agent for recommendations for the 5 new song features. 

I decided on language, release_decade, vocals (vocal or instrumental), popularity (0-100),and best_activity.

Then I asked the agent to update songs.csv and add these feature values to each song. I worked on deciding how much weight to give to each new attribute, and asked the agent to update scoring code based on that. 


**Prompts used:**
<!-- Paste the key prompts you gave the agent -->

- What other attributes should be used?
- Can you fill the values for each song with these attributes in mind?"
- Do you have suggestions on what points we can give to each new feauture?
- Can you help update the scoring logic? 
- Can we update main.py based on the new scoring function?


**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

The agent added 5 new columns for all 19 songs in songs.csv
Updated load_songs method to read the new columns
Updated score_song method to add 5 new scoring rules:
    - Language match: +1.0
    - Release decade: +0.5 for the same decade, +0.25 for one decade apart
    - Vocals match: +0.5
    - Popularity: up to +0.5, scaled by how close the song is to the target
    - Activity match: +1.0

Made sure that old user profiles that don't include the new features still work

Added two user profiles that use the new features and made the maximum score depend on which preferences a profile includes (up to 10 points instead 6.5)


**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

I reviewed the features the agent suggested and picked the ones I felt were most relevant in scoring the songs. 

I checked that the values in songs.csv had variety. I changed some songs' languages to Spanish, Korean, and French.

I read through the scoring logic to make sure each new rule made sense.

The agent made the maximum score depend on which preferences a profile includes (6.5 for old profiles, up to 10.0 for new ones) and I confirmed the percentages looked right.


---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->



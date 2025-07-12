# ASSIGNMENT #1 (COMPLETE)

# General instructions
- If this is your first time working on the project, follow the instructions for working with Git and answer the essay questions. 
- If you worked on this project in a previous class, you will participate in additional exercises about the theme of AI (See "Advanced Exercises").  You may recycle your answers from the previous class (the "Foundation Exercises").



## Objective
This week you will:  
1. Learn how git works
2. Create your own account in GitHub
3. Create a remote repo in GitHub
4. Create a local Repo on your Windows, MAC, or Linux system

# FOUNDATION EXERCISES (for everyone)

## ACTIVITY 1: Research git

### Part 1
- Using your prefered research methodology (books, web seraches, ChatGPT), research how Git works at a high level. At a minimum
cover the following: 
    - Types of version control systems.  What type is Git?
    - Snapshots
    - What is a repository? Remote vs. local. 
    - What is commit?
    - What is working directory?
    - What is Staging Area
    - Find a good diagram that illustrates the architecture and the flow
- Take notes on this.  You will need it later.

### Part 2 
- If you are using Windows, install Git Bash (not necessary for Mac and Linux)
- Install Visual Studio Code

## ACTIVITY 2:  Setting up a new github and local repo

- Create a GitHub account if you don't already have one
- Create a rep for this class
- When you create the repo you will see instructions about how to set up your local repo.  Below is a slighly modified version of the 
instructions you will see.
- In a Bash shell (Git Bash for Windows or terminal for Mac or Linux) run the following commands.  
- NOTE:  you will be accessing the repo via HTTPS and you will be storing your configuration in your local repo, not globally.  This will make it easier to use multiple Git Hub accounts. 

```
echo "# MSSE640-2025summer" >> README.md
git init
git add README.md


git config --local user.email "rgranier@regis.edu"
git config --local user.name "Randall Granier"


git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/granierregis/msse642-2025summer.git
git push -u origin main
```

## ACTIVITY 3: Edit the README.md file and push to your GitHub Repo.  

- On your local machine, use an editor like Visual Studio Code to edit the README.md file you created in the previous Activity. 
- Add the results of the research in the first Activity. 
- push your edited file to your git hub repo.  

# ADVANCED EXERCISES
### For those who did this project in a previous class

### Read one or more of following articles 
- In the next step, you will answer a question that referres to one or two of the articles.
- You can based your reading on the question that you pick (see reference in the question).

[Blurry JPG](./files/articles/BlurryJPG.pdf)

[Challenging the Myths](./files/articles/ChallengingTheMyths.pdf)

[Stochastic Parrots](./files/articles/Parrots.pdf)

[Can't spell Strawberry](./files/articles/Strawberry.pdf)

### Answer one of the following questions.  Pick the one that interests you. 

1. What responsibilities do software engineers have in mitigating the environmental and social impacts of large language models (LLMs)?
Refer to: “On the Dangers of Stochastic Parrots” and “Challenging the Myths of Generative AI”

Discuss the trade-offs between model size, performance, and environmental cost. Should engineers prioritize technical excellence over equity and sustainability?

2. How do myths and metaphors about AI (e.g., “learning,” “creativity,” “productivity”) influence public perception and policy?
Refer to: “Challenging the Myths of Generative AI”

Explore how language shapes beliefs about AI’s capabilities and limitations. How can software engineers and educators challenge misleading narratives?

3. If ChatGPT is a “blurry JPEG of the Web,” what are the risks of using such tools in academic, journalistic, or legal settings?
Refer to: “ChatGPT Is a Blurry JPEG of the Web”

Evaluate the implications of lossy AI-generated content. How do accuracy, originality, and accountability suffer or thrive in such systems?

4. What does the inability of LLMs to spell “strawberry” reveal about the architecture of current AI systems?
Refer to: “Why AI Can’t Spell 'Strawberry’”

Analyze the technical limitations of transformer-based models with respect to fine-grained symbolic understanding. How might future designs address this gap?

5. Are larger AI models inherently better? When might smaller, curated models be preferable in software engineering practice?
Refer to: “On the Dangers of Stochastic Parrots” and “Challenging the Myths of Generative AI”

Debate the scaling myth and consider real-world scenarios (e.g., edge devices, local AI) where model size might not correlate with usefulness or trustworthiness.

# WHAT TO TURN IN

- Your assignment will be completed in a markdown file. 
- Name the markdown file:

```
Assignment1<Lastname>
```
- Follow the directions above to ensure that your markdown file contains everything required for the assignment.
- Ensure that your markdown file for the assignment includes appropriate screen shots. 
- In the Slack channel #github-project, post the link to your GitHub repo that you created above when you are done.

### NOTE: 
- Ensure in the root directory of your repository, you have a markdown file called "README.md."  In that file, include a link to the assignment this week. 
- Example: 

```
[Assignment #X](./Assignment#<Lastname>.md)
``` 

### For advanced users (those who did the project before)
- Follow the directions for "ADVANCED EXERCISES" and include your work in the markdown assignment for the week.  
- Ensure that the "ADVANCED EXERCISES" section is clearly labeled with appropriate "header markdown." 

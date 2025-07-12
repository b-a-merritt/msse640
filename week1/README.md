# Assignment 1

## FOUNDATION EXERCISES
[Previous coursework from MSSE 642](https://github.com/b-a-merritt/msse642/tree/main/assignment1)

## ADVANCED EXERCISES

[Can't Spell Strawberry](https://github.com/granierregis/MSSE640-2025summer/blob/main/files/articles/Strawberry.pdf)

### What does the inability of LLMs to spell “strawberry” reveal about the architecture of current AI systems?

The inability of LLMs to count the rs in strawberry reveals that they do not think or reason like humans do. They tokenize words and letters to recognize patterns of speech that are then used to generate responses. They use statistical heuristics to write responses to prompts, but have no ability to parse the meaning of individual words. In the training data of the LLMs, there were no references to the number of rs in strawberry, so they pull likely responses from other occurrences of those tokens. Thus, LLMs do not perform well in executing novel tasks.

LLMs have improved this flaw by broadening the training data and introducing finite-state automata and external scripts. LLMs can then use those automata or scripts to execute algorithms related to the prompt (i.e., if there is a prompt to count something, those automata can take over and find an answer). While these solutions help the accuracy of the responses from an LLM, they are patches. Until AI comes up with a way to mimic reasoning more naturally, this will be one of its major flaws.

A practical example of this problem recently occurred while doing a simple task at work: a cron job that fetches entities and batch updates them needed to start paginating the requests to handle more items (it was getting behind because the response was consistently maxing its limit). I asked Copilot to write unit tests while I added the pagination. It did impressive work and must have used an automata to determine what it would do because for one line of code, it wrote four tests to cover each branch.

if not cursor or len(item) < limit:
    has_more = False

It wrote test cases for when both statements of the disjoint are true, both are false, and when either one is true. It was impressive. However, the code coverage showed that these lines were only partially covered. Why? I have no idea. The logic from the LLM was sound. And no matter how I asked it to rewrite the tests, the code coverage failed. I ended up spending more time with the LLM than if I had not used it to begin with. In the end, only after giving up with the LLM did I realize I didn't need to branch the logic at all.

has_more = bool(cursor) and len(item) == limit

It is those types of things that LLMs just do not get yet. 
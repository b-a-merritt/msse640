# Assignment 4 — Selenium

## Introduction

The project uses Python and pytest to run Selenium tests. A shared `chrome_browser` fixture in conftest.py launches headless Chrome (1920×1080, implicit wait 5s) and quits after each test. Tests were executed with the command `pytest week8`. Part 1 automates an e-commerce flow; Part 2 validates three user-centric flows on my personal site.

## Environment & How to Run

Dependencies: selenium, pytest, Chrome + chromedriver available on PATH.

Run: `pytest week8`

Files: 
- `./conftest.py` [(setup)](./conftest.py)
- `./marketplace_test.py` [(Part 1)](./marketplace_test.py)
- `./personal_site_test.py` [(Part 2)](./personal_site_test.py)

## Part 1:

Target: GCP’s Online Boutique (Cymbal Shops demo) at https://cymbal-shops.retail.cymbal.dev/.
Goal: When adding Sunglasses to the cart, the cart price equals the product page price.
Method: Navigate to the product, capture its listed price, click through to the detail view, Add To Cart, open the cart, and assert the cart display matches the captured price.
Result: Pass — price remained consistent from product listing to cart.

## Part 2:

### Test 1 — Prolog Terminal Skills Query

User story: As a visitor, I want to query the on-site Prolog terminal for the developer’s languages so I can quickly see their skill set.
Automation: Focus the Prolog input, submit `skill(X, language).`, wait for terminal output, and verify it lists the expected languages (TypeScript, Python, SQL, Go, Prolog, Java) in order.
Result: Pass — terminal returns the expected series of bindings.

### Test 2 — Resume Availability

User story: As a hiring manager, I want to open the developer’s resume directly so I can review qualifications.
Automation: Use the site’s keyboard shortcut (Ctrl+S) to open the resume in a new tab, switch to it, and assert the URL ends with `ben_merritt_resume.pdf`.
Result: Pass — resume loads at the expected URL.

### Test 3 — LinkedIn Navigation

User story: As a visitor, I want to jump to the developer’s LinkedIn profile so I can validate work history and connect.
Automation: Trigger the LinkedIn shortcut (Ctrl+O) to open a new tab, switch to it, and assert the page title contains “LinkedIn.”
Result: Pass — LinkedIn opens successfully.

### What I Learned

I used Cypress and Playwright tests before. While the setup and configuration for Selenium using Python is much easier, it lacks some component querying functionalities that made the others easier to use. For test suites that run in CI, I think I prefer Selenium. In other contexts, I would prefer Cypress.

## Recommendations

My experience with E2E frameworks like Selenium is pretty bad. I had to spend a few months trying to fix flaky tests at my first job. I think making students purposefully write flaky tests (like make them target things that change) so that they understand there are some things they should not do would be really helpful. I don't know exactly how that could be done, but it was a really difficult lesson for me to learn. (Perhaps they could target CSS classes that change on each render or target advertisements that sometimes change?).


## Evidence

![video of selenium tests](./assets/selenium-tests.mp4)

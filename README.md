# lab04-MiniNet
## Who Did What 
| Member | GitHub Username | File |
|---|---|---|
| Steven Naing | StevenNaing | test_deposit.py |
| Hnin Inzali | Inzali30 | test_withdraw.py |
| Chu Myat Sandi Tun | Chumyat | test_teardown.py |
| Tanvir Ali | 6805140002-Tanvir | test_shared.py |
| Htoo Eain Lwin | 6805140016-htoo | conftest.py |

## Our Merge Conflict

We encountered two related Git issues while working on our team repository.

First, our `git push` was rejected because another team member had
already pushed new commits to GitHub. Our local branch was therefore
behind the remote branch, so Git required us to get the latest changes
before pushing our own changes.

We then used:

`git pull --rebase`

During the rebase, we encountered a merge conflict in `README.md`
while working on the Who Did What table. My local changes included my
row:

| Hnin Inzali | Inzali30 | test_withdraw.py |

Another team member had also modified the same section of `README.md`.
Git could not automatically combine the changes because both versions
modified the same part of the file.

We resolved the conflict manually by keeping all required team-member rows in the final README and removing the conflict markers.

After resolving the conflict, we ran:

`git add README.md`

and:

`git rebase --continue`

The rebase completed successfully after resolving the conflict, and we
then ran `git push` to upload the resolved changes to GitHub.

## Git Contribution Summary 
    12  Henry
     7  Steven
     6  Hnin Inzali
     5  Chu Myat Sandi Tun
     5  Tanvir Ali

## Reflection Questions
**Why was your push rejected, and how did you fix it?**

The push was rejected because another team member had already pushed new commits to GitHub, making our local branch out of date. We resolved this by executing git pull to fetch and integrate the latest changes before running git push again.   

**Why could Git not resolve the README conflict automatically?**

Git could not resolve the conflict automatically because two contributors modified the exact same lines in README.md simultaneously. Git cannot infer user intent or decide which text to preserve without human input. 

**What is the difference between committing and pushing?**

Committing saves a snapshot of staged changes into your local Git repository on your machine, while pushing uploads those local commits to the remote GitHub repository so team members can view and access them. 

**How do fixtures reduce duplicated setup code in tests?**

Fixtures provide a centralized, reusable setup function that automatically initializes and supplies pre-configured objects or state to test functions, eliminating the need to repeatedly write setup code across multiple test cases. This makes the tests shorter and easier to maintain.

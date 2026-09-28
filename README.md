# lab04-MiniNet
# Who Did What 
| Steven | 6805140018@siam.edu | test_deposit.py |
| Hnin Inzali | Inzali30 | test_withdraw.py |
| Chu Myat Sandi Tun | Chumyat | test_teardown.py |
| Tanvir Ali | 6805140002-Tanvir | test_shared.py |
| Htoo Eain Lwin @ Henry | 6805140016@siam.edu | conftest.py |

Reflection Questions
Why was your push rejected, and how did you fix it?
The push was rejected because another team member had already pushed new commits to GitHub, making our local branch out of date. We resolved this by executing git pull to fetch and integrate the latest changes before running git push again.   

Why could Git not resolve the README conflict automatically?
Git could not resolve the conflict automatically because two contributors modified the exact same lines in README.md simultaneously. Git cannot infer user intent or decide which text to preserve without human input.   
What is the difference between committing and pushing?
Committing saves a snapshot of staged changes into your local Git repository on your machine, while pushing uploads those local commits to the remote GitHub repository so team members can view and access them.   
How do fixtures reduce duplicated setup code in tests?
Fixtures provide a centralized, reusable setup function that automatically initializes and supplies pre-configured objects or state to test functions, eliminating the need to repeatedly write setup code across multiple test cases. 

# Instructions

For the final project, you are expected to work in groups of 3 to 5 members on a web app project that aims to put into practice key software engineering practices discussed througout the semester. You, together with your team, will have the freedom to choose what to implement during this final project, as long as the requirements described below are met. 

# Requirements 

A successful project must meet the following requirements: 

* The software must be a web app written in Python with the possibility of creating and authenticating users.
* Scrum must be used as the software development methodology. 
* The project must have a vision statement that describes what the purpose of the software is, the type of problem it tries to solve, and the target audience.
* A use case diagram must be constructed to provide a high-level view of possible user interactions with the system.
* At least six user stories must be described in detail, including their acceptance criteria and point estimates. 
* User stories must be referred to as US#1, US#2, etc. 
* At least one of the user stories, not related to user creation or authentication, must be detailed by a sequence diagram. 
* A class diagram must be built with the main classes used in the project and their associations. 
* A GitHub repository must be created for the project. 
* The GitHub repository must follow the file structure explained (later) in this document. 
* All team members and the [instructor](https://github.com/thyagomota) must be added as collaborators to the project's GitHub repository. 
* There should be two long-lived branches on this project: **main** (for the stable release) and **dev** for the (unstable release). 
* The stable release is the one that is usually updated at the end of each sprint and have the user stories that were considered to be done. 
* The unstable release is the one that has one or more updates during sprints. 
* The **main** branch must be protected and require a code review before a pull request approval. 
* All source code must have a consistent header comment with a brief description and its author. 
* Code written for this project must comply to PEP8 code style standard. 
* Code will be inspected for best practices of commenting, naming, formatting, function decomposition, OOP, error handling, etc. 
* At least one white-box and one black-box test, none of them related to user creation or authentication, must be provided. 
* Test coverage report must be generated using Python's **coverage**. 
* The final product must be deployed using docker containerization technology. 
* All requirements needed for the project must be frozen into **requirements.txt**. 

# GitHub Repository Structure 

```
README.md
Dockerfile
requirements.txt
src/
tests/
```
Use README_TEMPLATE.md for information about the format that you should use for the project's README file. 

Feel free to add other folders as you see fit.

# Project Management 

The team must use [Jira](https://onlinejira.com/) to keep track of the product backlog and sprint progress. The team should elect a scrum master among themselves. The scrum master will create a project on Jira and invite the instructor and all other members of the team to join. Jira should be used to manage the tasks created for this project. The Scrum Master should organize daily scrums and sprint retrospective meetings with the developers, which should be done outside class time. Teams should meet with the instructor during the last week of class for a checkpoint before the final deadline. 

# Project Submission

Commit this **README.md** file with the link of your project's GitHub repository below: 

```
GitHub repository: <URL>
```

# Rubric

+5 Project's README file: mission statement

+5 Project's README file: use case diagram 

+10 Project's README file: user stories (~ 6 x 1.5)

+5 Project's README file: sequence diagram 

+5 Project's README file: class diagram 

+5 GitHub repository organization

+20 Project's README file and Jira Project: evidences of using scrum. 

+5 Code inspection: PEP8 compliance 

+10 Code inspection: comments, naming, functions, formatting, OOP best practices, error handling, etc.

+10 Code execution: white-box and black-box testing

+5 Project's README file: test coverage report using Python's **coverage**

+5 Project's README file: deployment instructions

+15 team/self evaluation

Deductions: 

-10 user creation not available/working

-10 user authentication not available/working 

-5 for each user story not completed 

-5 **main** branch does not have consistent commits 

-5 **dev** branch does not have consistent commmits

-5 deployment does not work
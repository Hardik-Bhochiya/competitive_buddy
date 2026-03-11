Competitive Buddy

Competitive Buddy is a web application designed to assist competitive programmers in tracking contests, analyzing their coding statistics, and getting guidance while solving algorithmic problems. The platform integrates data from major competitive programming sites and provides a simple interface to monitor progress and improve problem-solving skills.

The application combines contest tracking, profile management, statistics visualization, and an AI-based mentor that helps users with algorithms and competitive programming concepts.

Features
1. Dashboard

The dashboard serves as the main entry point of the application. It provides quick access to all important tools and features.

Functions:

Quick navigation to AI Mentor, Contest Tracker, Stats, and Profile

Practice links for Codeforces, LeetCode, and CodeChef

Competitive programming tips

Clean overview of the platform tools

2. Contest Tracker

The contest tracker collects contest information from multiple platforms and organizes them into useful sections.

Platforms Supported:

Codeforces

LeetCode

CodeChef

Sections Available:

Running Contests

Upcoming Contests

Past Contests

Features:

Contest name

Platform indicator

Start time

Duration

Direct contest link

This helps users keep track of upcoming programming contests in one place.

3. Statistics Page

The statistics page gathers user performance data from competitive programming platforms and presents it in an organized format.

Supported Platforms:

Codeforces

LeetCode

CodeChef

Displayed Data:

Codeforces

Handle

Current Rating

Rank

Maximum Rating

Maximum Rank

Number of solved problems

Activity heatmap based on submissions

LeetCode

Handle

Rating

Total problems solved

Easy problems solved

Medium problems solved

Hard problems solved

Global ranking

Activity heatmap

CodeChef

Handle

Rating

Star rating

Total solved problems

Global rank

Country rank

Activity heatmaps visualize user submissions over time.

4. AI Mentor

The AI Mentor helps users with competitive programming concepts and problem-solving strategies.

Capabilities:

Explains algorithms and data structures

Provides guidance on dynamic programming, graphs, greedy algorithms, etc.

Helps with Codeforces and LeetCode preparation

Gives short and concise answers focused on competitive programming

Restrictions:

Only answers questions related to competitive programming

Keeps responses short and practical

5. User Profile

Users can maintain their personal competitive programming profile.

Profile Information Includes:

Profile image

Username

College / Institution

Country

Bio

Competitive programming handles

Supported Handles:

Codeforces

LeetCode

CodeChef

Users can edit and update their details anytime.

Authentication System

The application includes a simple authentication system.

Features:

User registration

User login

User logout

Profile editing

Authentication is handled using Django's built-in authentication system.

Technologies Used
Backend

Python

Django Framework

Frontend

HTML

CSS

JavaScript

APIs

The application integrates several APIs to fetch data.

Codeforces API

Used for:

User statistics

Contest information

Submission activity

API:

https://codeforces.com/api
LeetCode GraphQL API

Used for:

User statistics

Contest information

Submission calendar

CodeChef API / Web Scraping

Used for:

User rating

Stars

Rank

Solved problems

Contest data

Groq AI API

Used for:

AI Mentor functionality

Model used:

llama-3.1-8b-instant
Project Structure
competitive_buddy
│
├── accounts        → User authentication and profile
├── contests        → Contest tracking system
├── stats           → User statistics from platforms
├── mentor          → AI mentor functionality
├── core            → Dashboard and base views
│
├── templates       → HTML templates
├── static          → CSS and frontend assets
├── media           → Uploaded profile images
│
└── manage.py
Installation
1. Clone the repository
git clone https://github.com/yourusername/competitive_buddy.git
2. Navigate to project directory
cd competitive_buddy
3. Create virtual environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate
4. Install dependencies
pip install django requests beautifulsoup4 groq
5. Set environment variable for AI API

Windows PowerShell

setx GROQ_API_KEY "your_api_key_here"

Restart terminal after setting this.

6. Run database migrations
python manage.py migrate
7. Run the development server
python manage.py runserver

Open browser:

http://127.0.0.1:8000
Future Improvements

Possible enhancements for the platform include:

Contest reminder notifications

Rating graph visualization

Personalized problem recommendations

Problem difficulty analysis

AI mentor conversation history

Improved heatmap visualization

Leaderboard and ranking system

Purpose of the Project

The goal of this project is to provide competitive programmers with a unified platform where they can:

Track programming contests

Analyze coding progress

Manage competitive programming profiles

Get guidance from an AI mentor

The project also demonstrates practical integration of APIs, web scraping, and AI systems in a Django web application.
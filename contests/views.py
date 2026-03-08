from django.shortcuts import render
import requests
from datetime import datetime, timedelta


# -------- Duration Formatter --------

def format_duration(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    mins = minutes % 60

    if mins == 0:
        return f"{hours}h"
    return f"{hours}h {mins}m"


def format_duration_minutes(minutes):
    minutes = int(minutes)
    hours = minutes // 60
    mins = minutes % 60

    if mins == 0:
        return f"{hours}h"
    return f"{hours}h {mins}m"


# -------- Main View --------

def contests(request):

    running = []
    upcoming = []
    past = []

    now = datetime.now()

# ---------------- CODEFORCES ----------------

    try:

        url = "https://codeforces.com/api/contest.list"
        response = requests.get(url, timeout=5)

        print("CF STATUS:", response.status_code)

        if response.status_code == 200:

            data = response.json()

            if data["status"] == "OK":

                for contest in data["result"]:

                    start = datetime.fromtimestamp(contest["startTimeSeconds"])
                    duration = format_duration(contest["durationSeconds"])

                    contest_data = {
                        "platform": "Codeforces",
                        "name": contest["name"],
                        "start": start,
                        "duration": duration,
                        "url": f"https://codeforces.com/contest/{contest['id']}"
                    }

                    if contest["phase"] == "BEFORE":
                        upcoming.append(contest_data)

                    elif contest["phase"] == "CODING":
                        running.append(contest_data)

                    elif contest["phase"] == "FINISHED":
                        past.append(contest_data)

    except Exception as e:
        print("CF ERROR:", e)


# ---------------- LEETCODE ----------------

    try:

        url = "https://leetcode.com/graphql"

        query = {
            "query": """
            query {
              allContests {
                title
                startTime
                duration
              }
            }
            """
        }

        response = requests.post(url, json=query, timeout=5)

        print("LC STATUS:", response.status_code)

        if response.status_code == 200:

            result = response.json()

            if result.get("data") and result["data"].get("allContests"):

                lc_contests = result["data"]["allContests"]

                for contest in lc_contests:

                    start = datetime.fromtimestamp(contest["startTime"])
                    duration = format_duration(contest["duration"])

                    end = start + timedelta(seconds=contest["duration"])

                    contest_data = {
                        "platform": "LeetCode",
                        "name": contest["title"],
                        "start": start,
                        "duration": duration,
                        "url": "https://leetcode.com/contest/"
                    }

                    if start <= now <= end:
                        running.append(contest_data)

                    elif start > now:
                        upcoming.append(contest_data)

                    else:
                        past.append(contest_data)

    except Exception as e:
        print("LC ERROR:", e)


# ---------------- CODECHEF ----------------

    try:

        url = "https://www.codechef.com/api/list/contests/all"
        response = requests.get(url, timeout=5)

        print("CC STATUS:", response.status_code)

        if response.status_code == 200:

            data = response.json()

            # RUNNING CONTESTS
            for contest in data["present_contests"]:

                start = datetime.strptime(
                    contest["contest_start_date_iso"],
                    "%Y-%m-%dT%H:%M:%S+05:30"
                )

                contest_data = {
                    "platform": "CodeChef",
                    "name": contest["contest_name"],
                    "start": start,
                    "duration": format_duration_minutes(contest["contest_duration"]),
                    "url": f"https://www.codechef.com/{contest['contest_code']}"
                }

                running.append(contest_data)

            # UPCOMING CONTESTS
            for contest in data["future_contests"]:

                start = datetime.strptime(
                    contest["contest_start_date_iso"],
                    "%Y-%m-%dT%H:%M:%S+05:30"
                )

                contest_data = {
                    "platform": "CodeChef",
                    "name": contest["contest_name"],
                    "start": start,
                    "duration": format_duration_minutes(contest["contest_duration"]),
                    "url": f"https://www.codechef.com/{contest['contest_code']}"
                }

                upcoming.append(contest_data)

            # PAST CONTESTS
            for contest in data["past_contests"][:5]:

                start = datetime.strptime(
                    contest["contest_start_date_iso"],
                    "%Y-%m-%dT%H:%M:%S+05:30"
                )

                contest_data = {
                    "platform": "CodeChef",
                    "name": contest["contest_name"],
                    "start": start,
                    "duration": format_duration_minutes(contest["contest_duration"]),
                    "url": f"https://www.codechef.com/{contest['contest_code']}"
                }

                past.append(contest_data)

    except Exception as e:
        print("CC ERROR:", e)


# ---------------- SORT ----------------

    running = sorted(running, key=lambda x: x["start"])
    upcoming = sorted(upcoming, key=lambda x: x["start"])
    past = sorted(past, key=lambda x: x["start"], reverse=True)


# ---------------- CONTEXT ----------------

    context = {
        "running": running[:5],
        "upcoming": upcoming[:10],
        "past": past[:5],
    }

    return render(request, "contests/contests.html", context)
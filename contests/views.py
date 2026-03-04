from django.shortcuts import render
import requests
from datetime import datetime


def contests(request):

    running = []
    upcoming = []
    past = []

    now = datetime.now()

# ---------------- CODEFORCES ----------------

    try:

        url = "https://codeforces.com/api/contest.list"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:

            data = response.json()

            if data["status"] == "OK":

                for contest in data["result"]:

                    start = datetime.fromtimestamp(contest["startTimeSeconds"])
                    duration = contest["durationSeconds"] // 3600

                    contest_data = {
                        "platform": "Codeforces",
                        "name": contest["name"],
                        "start": start,
                        "duration": f"{duration}h",
                        "url": f"https://codeforces.com/contest/{contest['id']}"
                    }

                    if contest["phase"] == "BEFORE":
                        upcoming.append(contest_data)

                    elif contest["phase"] == "CODING":
                        running.append(contest_data)

                    else:
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

        if response.status_code == 200:

            contests = response.json()["data"]["allContests"]

            for contest in contests:

                start = datetime.fromtimestamp(contest["startTime"])
                duration = contest["duration"] // 60

                contest_data = {
                    "platform": "LeetCode",
                    "name": contest["title"],
                    "start": start,
                    "duration": f"{duration}m",
                    "url": "https://leetcode.com/contest/"
                }

                end = start.timestamp() + contest["duration"]

                if start > now:
                    upcoming.append(contest_data)

                elif start <= now <= datetime.fromtimestamp(end):
                    running.append(contest_data)

                else:
                    past.append(contest_data)

    except Exception as e:
        print("LC ERROR:", e)


# ---------------- CODECHEF ----------------

    try:

        url = "https://www.codechef.com/api/list/contests/all"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:

            data = response.json()

            for contest in data["future_contests"]:

                start = datetime.strptime(
                    contest["contest_start_date_iso"],
                    "%Y-%m-%dT%H:%M:%S+05:30"
                )

                contest_data = {
                    "platform": "CodeChef",
                    "name": contest["contest_name"],
                    "start": start,
                    "duration": contest["contest_duration"],
                    "url": f"https://www.codechef.com/{contest['contest_code']}"
                }

                upcoming.append(contest_data)

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
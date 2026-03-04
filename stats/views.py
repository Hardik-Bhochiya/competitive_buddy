from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup
import json
from collections import defaultdict
import datetime


@login_required
def stats(request):

    profile = request.user.profile

    cf_handle = profile.codeforces
    lc_handle = profile.leetcode
    cc_handle = profile.codechef

    cf_data = None
    cf_solved = 0
    cf_heatmap = defaultdict(int)

    lc_data = None
    cc_data = None


# ---------------- CODEFORCES ----------------

    if cf_handle:

        info_url = f"https://codeforces.com/api/user.info?handles={cf_handle}"
        info = requests.get(info_url).json()

        if info["status"] == "OK":

            user = info["result"][0]

            cf_data = {
                "handle": user["handle"],
                "rating": user.get("rating", "Unrated"),
                "maxRating": user.get("maxRating", "Unrated"),
                "rank": user.get("rank", "Unrated"),
                "maxRank": user.get("maxRank", "Unrated"),
            }

        status_url = f"https://codeforces.com/api/user.status?handle={cf_handle}"
        status = requests.get(status_url).json()

        if status["status"] == "OK":

            solved = set()

            for sub in status["result"]:

                if sub.get("verdict") == "OK":

                    problem = sub["problem"]
                    solved.add(str(problem["contestId"]) + problem["index"])

                    # heatmap logic
                    timestamp = sub["creationTimeSeconds"]
                    date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

                    cf_heatmap[date] += 1

            cf_solved = len(solved)


# ---------------- LEETCODE ----------------

    if lc_handle:

        url = "https://leetcode.com/graphql"

        query = {
            "query": """
            query getUserProfile($username: String!) {
              matchedUser(username: $username) {
                submitStats {
                  acSubmissionNum {
                    difficulty
                    count
                  }
                }
                profile {
                  ranking
                }
                submissionCalendar
              }
              userContestRanking(username: $username) {
                rating
              }
            }
            """,
            "variables": {"username": lc_handle}
        }

        response = requests.post(url, json=query)

        if response.status_code == 200:

            result = response.json()["data"]

            user = result["matchedUser"]
            stats = user["submitStats"]["acSubmissionNum"]
            contest = result["userContestRanking"]

            calendar = json.loads(user["submissionCalendar"])

            lc_data = {
                "handle": lc_handle,
                "totalSolved": stats[0]["count"],
                "easy": stats[1]["count"],
                "medium": stats[2]["count"],
                "hard": stats[3]["count"],
                "ranking": user["profile"]["ranking"],
                "rating": contest["rating"] if contest else "No contest rating",
                "calendar": calendar
            }


# ---------------- CODECHEF ----------------

    if cc_handle:

        try:

            cc_url = f"https://www.codechef.com/users/{cc_handle}"

            response = requests.get(cc_url)

            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                rating = soup.find("div", class_="rating-number")
                stars = soup.find("span", class_="rating")

                global_rank = "N/A"
                country_rank = "N/A"

                rating_header = soup.find_all("div", class_="rating-ranks")

                if rating_header:

                    ranks = rating_header[0].find_all("strong")

                    if len(ranks) >= 2:
                        global_rank = ranks[0].text.strip()
                        country_rank = ranks[1].text.strip()

                cc_data = {
                    "handle": cc_handle,
                    "rating": rating.text.strip() if rating else "N/A",
                    "stars": stars.text.strip() if stars else "N/A",
                    "global_rank": global_rank,
                    "country_rank": country_rank,
                }

        except Exception as e:

            print("CodeChef ERROR:", e)


# ---------------- CONTEXT ----------------

    context = {
        "cf": cf_data,
        "cf_solved": cf_solved,
        "cf_heatmap": dict(cf_heatmap),
        "lc": lc_data,
        "cc": cc_data,
    }

    return render(request, "stats/stats.html", context)
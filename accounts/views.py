from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# ---------------- SIGNUP ----------------
def signup(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("/accounts/signup/")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect("/")

    return render(request, "accounts/signup.html")


# ---------------- LOGIN ----------------
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,
                            username=username,
                            password=password)

        if user:
            login(request, user)
            return redirect("/")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect("/")


# ---------------- PROFILE ----------------
@login_required
def profile(request):

    profile = request.user.profile

    if request.method == "POST":

        profile.college = request.POST.get("college")
        profile.country = request.POST.get("country")
        profile.bio = request.POST.get("bio")

        profile.codeforces = request.POST.get("codeforces")
        profile.leetcode = request.POST.get("leetcode")
        profile.codechef = request.POST.get("codechef")

        profile.save()

        return redirect("/accounts/profile/")

    return render(request, "accounts/profile.html")
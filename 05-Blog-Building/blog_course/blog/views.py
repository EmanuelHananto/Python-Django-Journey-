from django.shortcuts import render
from datetime import date
all_posts = [
    {
        "slug": 'Feeding-Frogies',
        "image": "froggies.jpg",
        'author': "Pepe",
        "date": date(2026, 11, 28),
        "title": "Feeding Frogies",
        "excerpt": "There's nothing like the feeling of feeding a good boi, it's just a good mood lifter", 
        "content": "Feeding sand avocado frogs makes em goes brr and squeek. Instant dopamine boost for the feeder",
    },
    {
        "slug": "the-origin-of-pepe",
        "image": "pepe-classic.jpg",
        "author": "Pepe",
        "date": date(2026, 11, 29),
        "title": "The Origin of Pepe",
        "excerpt": "There's nothing like the feeling of discovering where the iconic feels good man meme started",
        "content": "Pepe the Frog originally started as a super laid-back comic character created by artist Matt Furie in his 2005 series Boy's Club, where Pepe loved playing video games, eating snacks, and hanging out with his roommates. His famous catchphrase 'feels good man' came from a simple, funny panel that resonated deeply with early internet users because of how relaxed and relatable his expression looked. Over the next decade, that single illustration evolved across forums and social media into thousands of expressive variations that people still use every single day to share their exact mood.",
    },
    {
        "slug": "comfy-pepe-vibes",
        "image": "comfy-pepe.jpg",
        "author": "Pepe",
        "date": date(2026, 11, 30),
        "title": "Comfy Pepe Vibes",
        "excerpt": "Sometimes the best thing you can do is wrap up in a warm blanket and enjoy the quiet",
        "content": "Out of all the countless variations out there, Comfy Pepe wrapped up tightly in a warm blanket with a hot mug of tea remains the undisputed champion of wholesome internet culture. It perfectly captures that peaceful weekend feeling when there are zero deadlines to worry about, rain is tapping gently against the window, and your only plan is to relax. Embracing that cozy frog energy is a great reminder to step away from the chaos of a busy week and just enjoy doing nothing for a little while.",
    },
]

def get_date(post):
    return post["date"]

def mainpage (request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts [-3:]
    return render(request, "blog/index.html", {"latest":latest_posts})

def posts (request):
    return render (request, "blog/posts.html", {"all_posts": all_posts})

def postlists (request,slug):
    identified_post = next(post for post in all_posts if post["slug"] ==slug)
    return render (request, "blog/postlists.html",{"post":identified_post})
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

"""
def january(request):
    return HttpResponse("This is January's challenge!")
def february(request):
    return HttpResponse("This is February's challenge!")

#Manual before we had dynamic urls
"""

"""
def monthly_challenge_int(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This is January's challenge!"
    elif month == "february":
        challenge_text = " This is February's challange!"
    elif month == "march":
        challenge_text = "This is March's challenge!"
    elif month == "april":
        challenge_text = "This is April's challenge!"
    elif month == "may":
        challenge_text = "This is May's challenge!"
    elif month == "june":
        challenge_text = "This is June's challenge!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)

#before we had dictionary
"""

monthly_challenges = {
    "january": "This is January's challenge!",
    "february": "This is February's challenge!",
    "march": "This is March's challenge!",
    "april": "This is April's challenge!",
    "may": "This is May's challenge!",
    "june": "This is June's challenge!",
    "july": "This is July's challenge!",
    "august": "This is August's challenge!",
    "september": "This is September's challenge!",
    "october": "This is October's challenge!",
    "november": "This is November's challenge!",
    "december": "This is December's challenge!"
}
month_list = list(monthly_challenges.keys())

def index(request):
    list_keys = ""
    
    for month in month_list:
        capitalized_month = month.capitalize()
        month_reverse = reverse ("monthly_challenge", args=[month])
        list_keys += f"<li><a href=\"{month_reverse}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_keys}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_int(request, month):
    if month > len(month_list):
        return HttpResponseNotFound("<h2>There are only twelve months in a year!</h2>")
    month_int = month_list [month-1]
    redirect_path = reverse ("monthly_challenge", args=[month_int])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    challenge_text = monthly_challenges.get(month)
    return_challenge = f"<h3>{challenge_text}</h3>"
    if not challenge_text:
        return HttpResponseNotFound("<h2> The only available months are: " + ", ".join(monthly_challenges.keys()) + "</h2>")
    return HttpResponse(return_challenge)
    
"""
def monthly_challenge_int(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
#another variant of monthly_challenge function using dictionary
"""

#To be able to create available links on wrong month, i used loop to pull the keys from the items.
#For the key u can use: for x in monthly_challenges.keys(): and for the value u can use for x in monthly_challenges.values(): to get the value of the key.
#And then combine it via print (", ".join(monthly_challenges.keys())) to get the list of available months in a string format.



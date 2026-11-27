from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}
month_list = list(monthly_challenges.keys())

"""def index(request):
    list_keys = ""
    
    for month in month_list:
        capitalized_month = month.capitalize()
        month_reverse = reverse ("monthly_challenge", args=[month])
        list_keys += f"<li><a href=\"{month_reverse}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_keys}</ul>"
    return HttpResponse(response_data)
    #Before adding templates (tags)"""

def index(request):
    return render(request, "challenge/index.html", {"months": month_list})

def monthly_challenge_int(request, month):
    if month > len(month_list):
        return HttpResponseNotFound("<h2>There are only twelve months in a year!</h2>")
    month_int = month_list [month-1]
    redirect_path = reverse ("monthly_challenge", args=[month_int])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenge/challenge.html", {"text": challenge_text, "month_name": month.capitalize(), "month_title": month})
    except:
        error_html = render_to_string("404.html")
    return HttpResponseNotFound(error_html)

"""# raise Http404()
    Above line is used to raise a 404 error when the month is not found in the dictionary. but require false debug
    # use render_to_string to render the template and return the response without adding request""" 
   
    
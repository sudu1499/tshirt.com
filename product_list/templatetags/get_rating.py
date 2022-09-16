from django import template
import math
register=template.Library()



@register.simple_tag
def get_rating(obj):

    rating=obj.rating
    full_rating=int(rating)
    half=False if (rating-full_rating)==0.0 else True
    remaining=5-math.ceil(rating)
    r=[]
    print(full_rating,half,remaining)
    for i in range(full_rating):
        r.append('full.jpeg')
    if half:
        r.append('half.jpeg')
    for i in range(remaining):
        r.append('zero.jpeg')
    print(r)
    return r
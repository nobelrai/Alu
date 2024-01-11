# utils.py
from .models import ReviewRating, Items
from django.db.models import Avg

def user_based_collaborative_filtering(user):
    # Get the ratings of the given user
    user_ratings = ReviewRating.objects.filter(user=user)

    # Find users similar to the given user based on their ratings
    similar_users = ReviewRating.objects.exclude(user=user).filter(
        item__in=user_ratings.values('item'),
        rating__gte=user_ratings.aggregate(Avg('rating'))['rating__avg']
    ).values('user').distinct()

    # Get items rated by similar users but not by the given user
    recommended_items = Items.objects.filter(
        ratings__user__in=similar_users
    ).exclude(ratings__user=user).distinct()

    return recommended_items

from django.contrib.auth.models import User
from quiz_app.models import Badge, EarnedBadge

user = User.objects.filter(is_staff=False).first()
if user:
    badges = Badge.objects.all()
    for b in badges:
        EarnedBadge.objects.get_or_create(user=user, badge=b)
    print(f"Successfully awarded all {badges.count()} badges to {user.username}")
else:
    print("No student user found.")

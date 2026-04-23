from django.utils import timezone
from .models import StudentProfile

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Try to update last_activity for students
            try:
                # We use update() to avoid triggering the save() method and for better performance
                # But we only update if it's been more than 1 minute since last update to save DB writes
                profile = request.user.student_profile
                now = timezone.now()
                
                # Update last activity
                if not profile.last_activity or (now - profile.last_activity).total_seconds() > 60:
                    profile.last_activity = now
                    profile.save(update_fields=['last_activity'])

                # Update section view timestamps
                path = request.path
                updated_ts = False
                if '/quiz-list/' in path or '/quiz/' in path:
                    profile.view_timestamps['quizzes'] = now.isoformat()
                    updated_ts = True
                elif '/assignments/' in path:
                    profile.view_timestamps['assignments'] = now.isoformat()
                    updated_ts = True
                elif '/resources/' in path:
                    profile.view_timestamps['resources'] = now.isoformat()
                    updated_ts = True
                elif '/notices/' in path:
                    profile.view_timestamps['notices'] = now.isoformat()
                    updated_ts = True
                
                if updated_ts:
                    profile.save(update_fields=['view_timestamps'])
            except Exception:
                pass
        
        response = self.get_response(request)
        return response

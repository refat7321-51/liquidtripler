from .models import Notice, ReadNotice, Quiz, Assignment, Resource, StudentAttempt, AssignmentSubmission
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db.models import Q

def unread_notices_count(request):
    if request.user.is_authenticated:
        # Existing Notice logic
        active_notices = Notice.objects.filter(
            Q(recipient__isnull=True) | Q(recipient=request.user),
            is_active=True,
            publish_at__lte=timezone.now()
        ).order_by('-publish_at')
        
        read_notice_ids = ReadNotice.objects.filter(user=request.user, notice__is_active=True).values_list('notice_id', flat=True)
        
        unread_notices = active_notices.exclude(id__in=read_notice_ids)
        unread_count = unread_notices.count()
        unread_ids = set(unread_notices.values_list('id', flat=True))
        
        view_ts = {}
        if not request.user.is_staff:
            try:
                view_ts = request.user.student_profile.view_timestamps
            except Exception:
                view_ts = {}
        
        # New Quizzes: Published, not expired, not attempted, and created after last view
        attempted_quiz_ids = StudentAttempt.objects.filter(student=request.user).values_list('quiz_id', flat=True)
        quizzes_qs = Quiz.objects.filter(is_published=True, expires_at__gt=timezone.now()).exclude(id__in=attempted_quiz_ids)
        
        quiz_last_view = view_ts.get('quizzes')
        if quiz_last_view:
            dt = parse_datetime(quiz_last_view)
            if dt:
                quizzes_qs = quizzes_qs.filter(created_at__gt=dt)
        new_quizzes_count = quizzes_qs.count()

        # New Assignments: Not submitted yet and created after last view
        submitted_assignment_ids = AssignmentSubmission.objects.filter(student=request.user).values_list('assignment_id', flat=True)
        assignments_qs = Assignment.objects.filter(deadline__gt=timezone.now()).exclude(id__in=submitted_assignment_ids)
        
        assignment_last_view = view_ts.get('assignments')
        if assignment_last_view:
            dt = parse_datetime(assignment_last_view)
            if dt:
                assignments_qs = assignments_qs.filter(created_at__gt=dt)
        new_assignments_count = assignments_qs.count()

        # New Resources: Created after last view (default to last 3 days if never seen)
        resources_qs = Resource.objects.all()
        resource_last_view = view_ts.get('resources')
        if resource_last_view:
            dt = parse_datetime(resource_last_view)
            if dt:
                resources_qs = resources_qs.filter(created_at__gt=dt)
        else:
            three_days_ago = timezone.now() - timezone.timedelta(days=3)
            resources_qs = resources_qs.filter(created_at__gte=three_days_ago)
        new_resources_count = resources_qs.count()

        return {
            'unread_notices_count': unread_count,
            'unread_notice_ids': unread_ids,
            'new_quizzes_count': new_quizzes_count,
            'new_assignments_count': new_assignments_count,
            'new_resources_count': new_resources_count,
            'latest_notices': active_notices[:6],
        }
    return {
        'unread_notices_count': 0, 
        'unread_notice_ids': [],
        'new_quizzes_count': 0,
        'new_assignments_count': 0,
        'new_resources_count': 0,
        'latest_notices': []
    }

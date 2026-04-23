# Liquid_Triple_R - Full Stack Quiz Application

A comprehensive Django-based quiz application with admin dashboard, student interface, anti-cheat mechanisms, and real-time performance tracking.

## Features

### 🎓 Student Features
- ✅ Student registration (name entry before quiz)
- ✅ Timer countdown with visual indicator
- ✅ Random question order (different for each attempt)
- ✅ Multiple choice questions with 4 options
- ✅ Navigation between questions (Previous/Next)
- ✅ Change answers before submission
- ✅ Auto-submit when time expires
- ✅ View detailed results with correct/wrong answers
- ✅ Score percentage and performance feedback

### 🛡️ Anti-Cheat System
- 🚫 Tab switch detection
- 🚫 Page refresh detection
- 🚫 Page exit detection
- 🚫 Focus loss detection
- 🚫 IP address logging
- 🚫 User-agent tracking
- 🚫 Right-click prevention

### 👨‍💼 Admin Features
- ✅ Admin login with authentication
- ✅ Create, edit, delete quizzes
- ✅ Add multiple questions per quiz
- ✅ Set 4 options per question with correct answer
- ✅ Set time limit per quiz
- ✅ View all student attempts
- ✅ View detailed student performance
- ✅ View warning logs
- ✅ Dashboard with statistics

### 📊 Dashboard Analytics
- Student attempt tracking
- Score monitoring
- Warning logs visualization
- Quiz management statistics

---

## Project Structure

```
quiz_app/
├── quiz_project/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── quiz_app/                   # Main Django app
│   ├── models.py               # Database models
│   ├── views.py                # View logic
│   ├── urls.py                 # URL routing
│   ├── admin.py                # Django admin configuration
│   └── __init__.py
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── home.html               # Home page
│   ├── start_quiz.html         # Quiz start (name entry)
│   ├── take_quiz.html          # Quiz interface
│   ├── quiz_result.html        # Results page
│   ├── admin_login.html        # Admin login
│   ├── admin_dashboard.html    # Admin dashboard
│   ├── create_quiz.html        # Create quiz
│   ├── edit_quiz.html          # Edit quiz
│   ├── quiz_detail.html        # Quiz details
│   ├── add_question.html       # Add question
│   ├── edit_question.html      # Edit question
│   └── view_attempt.html       # View student attempt
├── static/
│   ├── css/
│   │   └── style.css           # Main stylesheet
│   └── js/
│       └── main.js             # Main JavaScript
├── manage.py                   # Django management
└── requirements.txt            # Python dependencies
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Extract the Project
```bash
unzip quiz_app.zip
cd quiz_app
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash

```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

When prompted:
```
Username: admin
Email: admin@example.com
Password: admin123
Password (again): admin123
```

### Step 6: Create Sample Admin User
```bash
python manage.py createsuperuser
```

Or use Django shell:
```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
exit()
```

### Step 7: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 8: Run Development Server
```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000**

---

## Usage Guide

### For Students

1. **Visit Home Page**
   - Open http://127.0.0.1:8000
   - See list of available quizzes

2. **Start Quiz**
   - Click "Start Quiz" button
   - Enter your name
   - Read the rules and click "Start Quiz"

3. **Take Quiz**
   - Answer questions by clicking option buttons
   - Use Previous/Next buttons to navigate
   - Click on question numbers on the left to jump
   - Selected options turn blue
   - Change answers anytime before submission
   - View timer at top right

4. **Submit Quiz**
   - Click "Submit Quiz" button
   - Quiz auto-submits when time expires
   - Cannot be interrupted once submitted

5. **View Results**
   - See score percentage and performance message
   - View detailed answer breakdown
   - Correct answers highlighted in green
   - Wrong answers highlighted in red
   - Unanswered questions marked with question mark

### For Admins

1. **Admin Login**
   - Click "Admin Login" in navigation
   - Username: 
   - Password: 

2. **Dashboard**
   - View statistics (total quizzes, attempts, warnings)
   - Switch between tabs:
     - **Manage Quizzes**: Create/Edit/Delete quizzes
     - **Student Attempts**: View all student results
     - **Warning Logs**: Monitor anti-cheat alerts

3. **Create Quiz**
   - Click "Create New Quiz"
   - Enter title, description, time limit
   - Click "Create Quiz"

4. **Add Questions**
   - Click "Add Question" on quiz detail page
   - Enter question text
   - Enter 4 options
   - Select correct answer
   - Click "Add Question"

5. **Edit Question**
   - Click "Edit" button on question
   - Modify text and options
   - Select new correct answer if needed
   - Click "Save Changes"

6. **Delete Question/Quiz**
   - Click "Delete" button
   - Confirm deletion

7. **View Student Results**
   - Go to "Student Attempts" tab
   - Click "Details" to see detailed performance
   - View warning logs for that student
   - See all their answers with correct/wrong indicators

---

## Database Models

### Quiz
- `title`: Quiz title
- `description`: Quiz description
- `time_limit`: Time limit in minutes
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Question
- `quiz`: Foreign Key to Quiz
- `text`: Question text
- `order`: Question order
- `created_at`: Creation timestamp

### Option
- `question`: Foreign Key to Question
- `text`: Option text
- `is_correct`: Boolean indicating correct answer

### StudentAttempt
- `quiz`: Foreign Key to Quiz
- `student_name`: Student name
- `session_id`: Unique session ID
- `started_at`: Start time
- `submitted_at`: Submission time
- `score`: Number of correct answers
- `total_questions`: Total questions in quiz
- `is_submitted`: Submission status
- `question_order`: JSON array of randomized question IDs

### StudentAnswer
- `attempt`: Foreign Key to StudentAttempt
- `question`: Foreign Key to Question
- `selected_option`: Foreign Key to Option
- `created_at`: Answer time

### WarningLog
- `attempt`: Foreign Key to StudentAttempt
- `warning_type`: Type of warning (tab_switch, page_refresh, page_exit, focus_lost)
- `timestamp`: When warning occurred
- `ip_address`: Student's IP address
- `user_agent`: Browser information

---

## API Endpoints

### Save Answer
```
POST /api/save-answer/
{
    "attempt_id": 1,
    "question_id": 1,
    "option_id": 1
}
```

### Submit Quiz
```
POST /api/submit-quiz/
{
    "attempt_id": 1
}
```

### Log Warning
```
POST /api/log-warning/
{
    "attempt_id": 1,
    "warning_type": "tab_switch"
}
```

---

## Configuration

### Time Limit
- Default: 30 minutes per quiz
- Configurable per quiz in admin panel
- Auto-submit when time reaches 0:00

### Questions Per Quiz
- Unlimited questions per quiz
- Each question must have exactly 4 options
- One option marked as correct answer

### Session Management
- Session timeout: 24 hours
- Session auto-saves on every action
- Cleared after quiz submission

---

## Anti-Cheat Mechanism

The application tracks:
1. **Tab Switches** - When student switches to another tab
2. **Page Refresh** - When student refreshes the page
3. **Page Exit** - When student leaves the quiz page
4. **Focus Lost** - When browser window loses focus

All events are logged with:
- Timestamp
- Student name
- Quiz name
- IP address
- User agent

---

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Issues
```bash
# Reset database
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Migration Errors
```bash
python manage.py migrate --run-syncdb
```

---

## Security Considerations

1. **CSRF Protection**: Enabled on all forms
2. **Session Security**: Secure session backend
3. **SQL Injection**: Django ORM protection
4. **XSS Protection**: Django template escaping
5. **Authentication**: Django auth system
6. **Password Hashing**: Django user model

### Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a strong random value
3. Update `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Set up proper logging
6. Enable HTTPS
7. Use environment variables for sensitive data

---

## Sample Quiz Creation

### Quiz 1: Python Basics
- **Title**: Python Basics
- **Time Limit**: 30 minutes
- **Questions**: 
  - What is Python? (A, B, C, D)
  - What is a list? (A, B, C, D)
  - How to create a function? (A, B, C, D)

---

## Performance Tips

1. Use database indexing for large datasets
2. Cache quiz questions
3. Use connection pooling for database
4. Optimize static file delivery with CDN
5. Enable gzip compression

---

## Browser Compatibility

- Chrome/Edge: ✅ Full Support
- Firefox: ✅ Full Support
- Safari: ✅ Full Support
- IE 11: ❌ Not Supported

---

## License

This project is provided as-is for educational purposes.

---

## Support & Maintenance

For issues or improvements, consider:
1. Checking the error logs
2. Reviewing Django documentation
3. Testing in different browsers
4. Checking network connectivity

---

## Future Enhancements

- [ ] User authentication for students
- [ ] Question bank and question categories
- [ ] Multiple quiz types (True/False, Short Answer)
- [ ] Detailed analytics and reports
- [ ] Email notifications
- [ ] Mobile app
- [ ] Video explanations
- [ ] Peer comparison
- [ ] Question randomization options
- [ ] Difficulty levels

---

## Contact & Feedback

For questions or feedback about this application, please review the code and documentation carefully.

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: Production Ready

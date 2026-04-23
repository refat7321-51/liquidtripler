# Quick Start Guide - Liquid_Triple_R

## 🚀 Fast Setup (5 minutes)

### Windows Users

1. **Extract the zip file**
   ```
   Right-click quiz_app.zip → Extract All
   ```

2. **Run setup script**
   ```
   Double-click setup.bat
   ```
   This will automatically:
   - Create virtual environment
   - Install dependencies
   - Run migrations
   - Create admin user
   - Collect static files

3. **Start the server**
   ```
   Open Command Prompt in quiz_app folder
   Run: venv\Scripts\activate.bat
   Run: python manage.py runserver
   ```

4. **Access the application**
   - Student Portal: http://127.0.0.1:8000
   - Admin Login: http://127.0.0.1:8000/admin/login/

---

### Linux/Mac Users

1. **Extract and navigate**
   ```bash
   unzip quiz_app.zip
   cd quiz_app
   ```

2. **Run setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Start the server**
   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```

4. **Access the application**
   - Student Portal: http://127.0.0.1:8000
   - Admin Login: http://127.0.0.1:8000/admin/login/

---

## 📝 Default Admin Credentials

**Username:** admin  
**Password:** admin123

*Change these immediately in production!*

---

## 🎯 First Steps

### As an Admin

1. Go to http://127.0.0.1:8000/admin/login/
2. Login with admin/admin123
3. Click "Create New Quiz"
4. Add quiz details:
   - Title: "Python Basics"
   - Description: "Test your Python knowledge"
   - Time Limit: 30 minutes
5. Click "Create Quiz"
6. Click "Add Question"
7. Add 5-10 questions with 4 options each
8. Mark the correct answer for each question

### As a Student

1. Go to http://127.0.0.1:8000
2. Click "Start Quiz"
3. Enter your name
4. Read the rules
5. Click "Start Quiz"
6. Answer all questions
7. Click "Submit Quiz"
8. View your results

---

## 🛠️ Troubleshooting

### Port 8000 Already in Use
```bash
python manage.py runserver 8001
# Then visit: http://127.0.0.1:8001
```

### Database Error
```bash
# Delete database and restart
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### ImportError or Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📊 Features Overview

### Student Features
- ✅ Random question order
- ✅ Timer countdown
- ✅ Navigate between questions
- ✅ Change answers anytime
- ✅ View results immediately
- ✅ See correct/wrong answers

### Admin Features
- ✅ Create/Edit/Delete quizzes
- ✅ Add unlimited questions
- ✅ View student attempts
- ✅ Monitor anti-cheat warnings
- ✅ Dashboard with statistics

### Security Features
- 🔒 Tab switch detection
- 🔒 Page refresh detection
- 🔒 IP logging
- 🔒 Session management
- 🔒 CSRF protection

---

## 📚 Sample Quiz Data

To quickly test the app, create this quiz:

**Quiz: General Knowledge**
- Time Limit: 20 minutes

**Question 1:** What is the capital of France?
- A) London
- B) Berlin
- C) **Paris** ✓
- D) Madrid

**Question 2:** Which planet is largest in our solar system?
- A) Saturn
- B) **Jupiter** ✓
- C) Neptune
- D) Earth

**Question 3:** What is 2+2?
- A) 3
- B) **4** ✓
- C) 5
- D) 6

---

## 🔐 Important Security Notes

1. **Change SECRET_KEY in production**
   - File: quiz_project/settings.py
   - Generate new: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

2. **Set DEBUG = False in production**
   - File: quiz_project/settings.py

3. **Use strong passwords**
   - Don't use 'admin123' in production

4. **Use PostgreSQL in production**
   - SQLite is for development only

---

## 📞 Need Help?

1. Check the full README.md
2. Review error messages in console
3. Check Django documentation: https://docs.djangoproject.com/
4. Verify Python version: `python --version` (should be 3.8+)

---

## ✨ Next Steps

1. Create multiple quizzes
2. Add 10-15 questions per quiz
3. Test as student - take quiz
4. Check admin dashboard
5. Review student results
6. Check warning logs
7. Customize with your own content

---

**Enjoy using Liquid_Triple_R! 🎓**

For detailed documentation, see README.md

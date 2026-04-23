import os

target_files = [
    'add_assignment.html',
    'edit_assignment.html',
    'add_question.html',
    'edit_question.html',
    'create_quiz.html',
    'edit_quiz.html',
    'admin_profile.html',
    'admin_reports.html',
    'resources.html',
    'leaderboard.html',
    'assignment_detail.html',
    'quiz_result.html',
    'take_quiz.html',
    'expired_quiz_answers.html',
    'assignment_list.html',
    'student_profile.html',
    'notices.html'
]

back_btn = '''    <div style="margin-bottom: 1rem;">
        <a href="javascript:history.back()"
           style="width:34px;height:34px;border-radius:10px;background:white;
                  border:1px solid #e2e8f0;display:inline-flex;align-items:center;
                  justify-content:center;color:#64748b;text-decoration:none;
                  box-shadow:0 1px 4px rgba(0,0,0,0.05);transition:all .2s;"
           onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='white'">
            <i class="fas fa-arrow-left" style="font-size:0.8rem;"></i>
        </a>
    </div>'''

# Alternative format that might exist in some files depending on how it was inserted
back_btn_alt1 = "\n" + back_btn
back_btn_alt2 = back_btn + "\n"

templates_dir = r"h:\files\quiz_app\templates"

for filename in target_files:
    filepath = os.path.join(templates_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        if back_btn_alt1 in content:
            content = content.replace(back_btn_alt1, "")
            modified = True
        elif back_btn_alt2 in content:
            content = content.replace(back_btn_alt2, "")
            modified = True
        elif back_btn in content:
            content = content.replace(back_btn, "")
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Reverted {filename}")
        else:
            print(f"No changes needed in {filename}")

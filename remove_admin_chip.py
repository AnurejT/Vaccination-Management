import os, re

dir_path = r'c:\Users\anure\PycharmProjects\VaxCore\templates\admins'

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(
            r'\{%\s*block topbar_user\s*%\}.*?\{%\s*endblock\s*%\}',
            '{% block topbar_user %}{% endblock %}',
            content,
            flags=re.DOTALL
        )
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
print('Done!')

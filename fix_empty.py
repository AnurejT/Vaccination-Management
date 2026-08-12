import os
import re

def fix_templates(directory):
    count = 0
    pattern = re.compile(r'\s*\{%\s*empty\s*%\}\s*\n\s*<tr.*?>.*?</tr>\s*\n', re.IGNORECASE | re.DOTALL)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = pattern.sub('\n', content)
                
                # Also handle case where it's on a single line or something slightly different
                # A more robust regex just to be sure:
                new_content = re.sub(r'\s*\{%\s*empty\s*%\}\s*<tr.*?>.*?</tr>', '', new_content, flags=re.IGNORECASE|re.DOTALL)
                
                # Wait, what if the `<tr>` is on the next line but there are multiple lines?
                # Usually it's just one line. Let's see if there are any `{% empty %}` left.
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed {filepath}")
                    count += 1
    print(f"Fixed {count} files.")

if __name__ == '__main__':
    fix_templates('c:/Users/anure/PycharmProjects/VaxCore/templates')

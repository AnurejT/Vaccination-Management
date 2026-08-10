import os, re

# ADMIN
p_admin = r'c:\Users\anure\PycharmProjects\VaxCore\templates\admins\adminhomepage.html'
with open(p_admin, 'r', encoding='utf-8') as f:
    c_admin = f.read()
new_admin = re.sub(
    r'<!-- Large Professional Hero Banner -->.*?<div style=\"display:grid;',
    r'''<!-- Large Professional Hero Banner -->
<div style="position:relative; width:100%; height:320px; border-radius:var(--r-lg); overflow:hidden; box-shadow:var(--sh-md); margin-bottom:30px; background:#ebf5ff;">
  <div style="position:absolute; top:0; right:0; width:65%; height:100%; z-index:1; background:url('/media/admin_hero.png') no-repeat center right; background-size:cover; mask-image:linear-gradient(to right, transparent, black 40%); -webkit-mask-image:linear-gradient(to right, transparent, black 40%);"></div>
  
  <div style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:3; display:flex; flex-direction:column; justify-content:center; padding:0 60px;">
    <h1 style="color:#0f172a; font-size:38px; font-weight:800; letter-spacing:-0.5px; margin-bottom:12px;">Welcome Admin</h1>
    <p style="color:#475569; font-size:16px; max-width:400px; line-height:1.6; margin-bottom:28px;">
      Manage users, hospitals, vaccines and appointments efficiently from one place.
    </p>
    <div>
      <a href="/myapp/adm_viewhospitals_get/" class="btn" style="background:#1d4ed8; color:#fff; padding:12px 28px; font-size:15px; font-weight:600; border-radius:var(--r-sm); box-shadow:0 4px 12px rgba(29,78,216,0.25); border:none;">Go to Dashboard <i class="fa fa-arrow-right" style="margin-left:8px;font-size:13px;"></i></a>
    </div>
  </div>
</div>

<div style="display:grid;''',
    c_admin,
    flags=re.DOTALL
)
with open(p_admin, 'w', encoding='utf-8') as f: f.write(new_admin)

# USER
p_user = r'c:\Users\anure\PycharmProjects\VaxCore\templates\users\userhomepage.html'
with open(p_user, 'r', encoding='utf-8') as f:
    c_user = f.read()
new_user = re.sub(
    r'<!-- Large Professional Hero Banner -->.*?<div style=\"display:grid;',
    r'''<!-- Large Professional Hero Banner -->
<div style="position:relative; width:100%; height:320px; border-radius:var(--r-lg); overflow:hidden; box-shadow:var(--sh-md); margin-bottom:30px; background:#ecfdf5;">
  <div style="position:absolute; top:0; right:0; width:65%; height:100%; z-index:1; background:url('/media/user_hero.png') no-repeat center right; background-size:cover; mask-image:linear-gradient(to right, transparent, black 40%); -webkit-mask-image:linear-gradient(to right, transparent, black 40%);"></div>
  
  <div style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:3; display:flex; flex-direction:column; justify-content:center; padding:0 60px;">
    <h1 style="color:#064e3b; font-size:38px; font-weight:800; letter-spacing:-0.5px; margin-bottom:12px;">Your Health, Our Priority</h1>
    <p style="color:#065f46; font-size:16px; max-width:400px; line-height:1.6; margin-bottom:28px;">
      Book your vaccine appointment easily and secure your protection today. Welcome back, {{ data.name }}.
    </p>
    <div>
      <a href="/myapp/user_generalvaccineavailability_get/" class="btn" style="background:#059669; color:#fff; padding:12px 28px; font-size:15px; font-weight:600; border-radius:var(--r-sm); box-shadow:0 4px 12px rgba(5,150,105,0.25); border:none;">Book Appointment <i class="fa fa-arrow-right" style="margin-left:8px;font-size:13px;"></i></a>
    </div>
  </div>
</div>

<div style="display:grid;''',
    c_user,
    flags=re.DOTALL
)
with open(p_user, 'w', encoding='utf-8') as f: f.write(new_user)

# HOSPITAL
p_hos = r'c:\Users\anure\PycharmProjects\VaxCore\templates\hospitals\hospitalhomepage.html'
with open(p_hos, 'r', encoding='utf-8') as f:
    c_hos = f.read()
new_hos = re.sub(
    r'<!-- Large Professional Hero Banner -->.*?<div style=\"display:grid;',
    r'''<!-- Large Professional Hero Banner -->
<div style="position:relative; width:100%; height:320px; border-radius:var(--r-lg); overflow:hidden; box-shadow:var(--sh-md); margin-bottom:30px; background:#f3e8ff;">
  <div style="position:absolute; top:0; right:0; width:65%; height:100%; z-index:1; background:url('/media/hospital_hero.png') no-repeat center right; background-size:cover; mask-image:linear-gradient(to right, transparent, black 40%); -webkit-mask-image:linear-gradient(to right, transparent, black 40%);"></div>
  
  <div style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:3; display:flex; flex-direction:column; justify-content:center; padding:0 60px;">
    <h1 style="color:#2e1065; font-size:38px; font-weight:800; letter-spacing:-0.5px; margin-bottom:12px;">Welcome {{ data.name }}</h1>
    <p style="color:#4c1d95; font-size:16px; max-width:400px; line-height:1.6; margin-bottom:28px;">
      Manage appointments, vaccine stock and schedules seamlessly.
    </p>
    <div>
      <a href="/myapp/hos_viewslot_get/" class="btn" style="background:#7c3aed; color:#fff; padding:12px 28px; font-size:15px; font-weight:600; border-radius:var(--r-sm); box-shadow:0 4px 12px rgba(124,58,237,0.25); border:none;">Go to Dashboard <i class="fa fa-arrow-right" style="margin-left:8px;font-size:13px;"></i></a>
    </div>
  </div>
</div>

<div style="display:grid;''',
    c_hos,
    flags=re.DOTALL
)
with open(p_hos, 'w', encoding='utf-8') as f: f.write(new_hos)
print('Done!')

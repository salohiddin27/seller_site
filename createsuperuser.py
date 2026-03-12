import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings') # 'root' o'rniga loyiha papkangiz nomi bo'lishi mumkin
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
email = 'admin@example.com'
password = '1'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' muvaffaqiyatli yaratildi!")
else:
    print(f"Superuser '{username}' allaqachon mavjud.")
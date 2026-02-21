# 🔐 Django Custom Authentication System

A production-ready authentication system built with Django featuring email-based login, account activation, password reset, and role-based access control.

This project replaces Django’s default username authentication with a fully customized user model using **email as the unique identifier**.

---

## 🚀 Features

### 🔐 Custom Authentication
- Custom `AbstractBaseUser` implementation
- Email used as `USERNAME_FIELD`
- Custom `UserManager`
- Secure password hashing
- Superuser auto-enabled with full permissions

---

### 👥 Role-Based Access Control
- `is_customer`
- `is_seller`
- `is_staff`
- `is_superuser`
- Role-based dashboard redirection
- Custom decorator:
  ```python
  @login_and_role_required('customer')
  @login_and_role_required('seller')
  ```
- Custom 403 Forbidden page

---

### 📝 Registration System
- Email-based registration
- Password & Confirm Password validation
- Unique email validation
- Inactive account until email verification
- Styled form widgets

---

### ✉️ Email Verification
- Token-based activation
- Base64 encoded user ID
- Secure activation link
- HTML email templates
- Asynchronous email sending (threaded)

---

### 🔑 Login System
- Email + Password authentication
- Activation status check
- Automatic role-based redirection:
  - Seller → `seller_dashboard`
  - Customer → `customer_dashboard`

---

### 🔁 Password Reset
- Email-based password reset request
- Secure token validation
- Reset link expiration handling
- `SetPasswordForm` integration
- HTML email template
- Threaded email sending

---

### 🛠 Admin Panel Customization
- Custom `UserAdmin`
- Extended fields:
  - Roles
  - Activation status
  - Timestamps
- Email-based search
- Structured fieldsets
- Custom ordering

---

### 🔐 Security
- Django `default_token_generator`
- URL-safe encoding
- Built-in authentication system
- Protected role-based decorators
- Secure password hashing

---

## 🏗 Project Structure

```
project/
│
├── account/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── utils.py
│   ├── decorators.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│
└── manage.py
```

---

## ⚙ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Md-Hasibul-Hasan/Django-Authentication.git
cd Django-Authentication
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django
```

Or if using requirements:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Settings

Add to `settings.py`:

```python
AUTH_USER_MODEL = 'account.User'

SITE_NAME = "Your Site Name"
SITE_DOMAIN = "http://127.0.0.1:8000"
```

Configure Email Backend:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'  # or your SMTP provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email'
EMAIL_HOST_PASSWORD = 'your_password'
```

---

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

## 🌐 Available Routes

| URL | Description |
|------|-------------|
| `/` | Home |
| `/register/` | Register |
| `/activate/<uidb64>/<token>/` | Activate Account |
| `/login/` | Login |
| `/password_reset/` | Request Password Reset |
| `/password_reset_confirm/<uidb64>/<token>/` | Reset Password |
| `/logout/` | Logout |

---

## 🧠 Tech Stack

- Python 3
- Django
- SMTP Email Service
- HTML Templates
- Threading (for async email)

---

## 📌 Use Cases

- E-commerce platforms
- SaaS applications
- Multi-role systems
- Email-based authentication systems
- Secure login implementations

---

## 📄 License

This project is open-source and available under the MIT License.

from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden


error_messages = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>403 Forbidden</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            max-width: 600px;
            padding: 20px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 2.5rem;
            color: #dc3545;
        }
        p {
            font-size: 1.2rem;
            margin: 10px 0;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
        }
        a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>403 Forbidden</h1>
        <p>You do not have permission to access this page.</p>
        <a href="/">Go to Homepage</a>
    </div>
</body>
</html>
"""

def login_and_role_required(required_role):
    """
    Decorator to check if the user is logged in and has the required role.
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if required_role == 'customer' and not user.is_customer:
                return HttpResponseForbidden(error_messages)
            if required_role == 'seller' and not user.is_seller:
                return HttpResponseForbidden(error_messages)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
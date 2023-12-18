import functools

from loguru import logger


def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_decorator
def add_numbers(a, b):
    return a + b


@log_decorator
def multiply_numbers(a, b):
    return a * b


# Test the decorated functions
result = add_numbers(3, 4)
print(result)  # Output: 7

result = multiply_numbers(2, 5)
print(result)  # Output: 10

# Check the logs


def authorize(allowed_roles):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_role = None  # Assume this function retrieves the user's role
            if user_role in allowed_roles:
                return func(*args, **kwargs)
            else:
                raise PermissionError("Unauthorized access")

        return wrapper

    return decorator


@authorize(allowed_roles=["admin", "editor"])
def create_post(title, content):
    # Logic to create a new post
    pass


@authorize(allowed_roles=["admin"])
def delete_post(post_id):
    # Logic to delete a post
    pass


# Test the decorated functions
create_post("Sample Title", "Sample Content")  # Raises PermissionError

delete_post(
    42
)  # Executes successfully if user role is "admin", raises PermissionError otherwise

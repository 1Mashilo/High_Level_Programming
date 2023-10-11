import sys

def safe_function(fct, *args):
    """
    Execute a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        Any: The result of the function execution, or None if an error occurs.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None

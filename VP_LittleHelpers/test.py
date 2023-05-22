def check_new_version_available(current_version, last_version):
    current_parts = current_version[1:].split('.')
    last_parts = last_version[1:].split('.')

    for current, last in zip(current_parts, last_parts):
        if int(current) < int(last):
            return True
        elif int(current) > int(last):
            return False

    return False  # Both versions are equal

# Example usage:
current = "v1.2.0"
last = "v1.1.12312"
result = check_new_version_available(current, last)
print(result)  # Output: True

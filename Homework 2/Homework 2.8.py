from typing import Callable


def create_user_settings() -> Callable:
    """Creates a system of settings"""
    settings = {
        'theme': 'light',
        'language': 'en',
        'notifications': True
    }

    def settings_manager(key=None, value=None) ->str|dict:
        """Settings management"""
        if key is None:
            return settings.copy()
        if value is None:
            return settings.get(key)
        settings[key] = value
        return f"Setting '{key}' updated"

    return settings_manager


user_settings = create_user_settings()

print(user_settings())
print(user_settings('theme'))

user_settings('theme', 'dark')
user_settings('language', 'uk')

print(user_settings('theme'))
print((user_settings('language')))
print(user_settings())
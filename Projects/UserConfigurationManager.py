test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
    }

key = ('Theme', 'Dark')

def add_setting(settings, key):
    key_lower = key[0]
    value_lower = key[1]
    key = (key_lower.lower(), value_lower.lower())

    if key[0] in settings:
        return f"Setting '{key[0]}' already exists! Cannot add a new setting with this name."

    if not key[0] in settings:
        settings[key[0]] = key[1]
        return f"Setting '{key[0]}' added with value '{key[1]}' successfully!"

add_setting({'theme': 'light'}, ('volume', 'high'))

def update_setting(settings, key):
    key_lower = key[0]
    value_lower = key[1]
    key = (key_lower.lower(), value_lower.lower())

    if key[0] in settings:
        settings[key[0]] = key[1]
        return f"Setting '{key[0]}' updated to '{key[1]}' successfully!"

    if not key[0] in settings:
        return f"Setting '{key[0]}' does not exist! Cannot update a non-existing setting."

update_setting({'theme': 'light'}, ('volume', 'high'))

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    if not key in settings:
        return f"Setting not found!"

delete_setting({'theme': 'light'}, 'theme')

def view_settings(settings):
    if not settings:
        return 'No settings available.'
    else:
        display_values = ''
        for word in settings:
            hi += f"{word.capitalize()}: {settings[word]}\n"
        return f'Current User Settings:\n{display_values}'

view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})




import os

def load_flags():
    try:
        flags_directory = "flags"
        if not os.path.exists(flags_directory):
            os.makedirs(flags_directory)

        flags = []
        for filename in os.listdir(flags_directory):
            if filename.endswith(".png"):
                country_name = filename[:-4].title()
                flag = {
                    "name": country_name,
                    "filename": os.path.join(flags_directory, filename)
                }
                flags.append(flag)

        return flags
    except Exception as e:
        print(f"Error while loading flags: {e}")
        return []


def clear_console():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"Error while clearing console: {e}")

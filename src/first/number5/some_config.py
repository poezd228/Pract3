def load_config(filename):
    """
    Load configuration from a Python script file.

    :param filename: The filename of the Python script containing configuration.
    :return: A dictionary representing the configuration.
    """
    config = {}
    try:
        with open(filename, 'r') as file:
            exec(file.read(), config)
    except FileNotFoundError:
        print(f"Error: Config file '{filename}' not found.")
    except Exception as e:
        print(f"Error loading config from '{filename}': {e}")
    return config
# config.py
CONFIG_VARIABLE = "value"

# main.py
config = load_config("config.py")
print(config)  # Output: {'CONFIG_VARIABLE': 'value'}

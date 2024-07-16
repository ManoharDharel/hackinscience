import pyfiglet


def create_banner(text):
    banner = pyfiglet.figlet_format(text)
    return banner


if __name__ == "__main__":
    banner_text = "Port Scanner"
    print(create_banner(banner_text))

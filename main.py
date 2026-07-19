from financeos.config import Config


def main():
    print("=" * 50)
    print(Config.PROJECT_NAME)
    print(f"Version : {Config.VERSION}")
    print(f"Author  : {Config.AUTHOR}")
    print("=" * 50)


if __name__ == "__main__":
    main()
    
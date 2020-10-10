flag_file_path = "[REDACTED]"

def main():
    print("Capturing a flag! How exciting.")
    with open(flag_file_path, "r") as flagfile:
        print("Flag contents are " + flagfile.read())


if __name__ == "__main__":
    main()

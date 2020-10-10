flag_file_path = "/etc/owasp/flags/flag.txt"

def main():
    print("Capturing a flag! How exciting.")
    with open(flag_file_path, "r") as flagfile:
        print(flagfile.read())


if __name__ == "__main__":
    main()

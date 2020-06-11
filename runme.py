#!/usr/bin/env python3

import glob
import base64

def print_all_resources():
    # Find all paths in the "script_resources" directory
    for resource_path in glob.glob("./runme_resources/*"):
        # Read the resource, decode it, and print the contents
        with open(resource_path, "r") as resource_file:
            print("\n=== Printing resource " + resource_path + " ===\n")
            resource = resource_file.read()
            decoded_resource = base64.b64decode(resource).decode()
            print(decoded_resource)

def main():
    print("Script started.")
    print_all_resources()

if __name__ == "__main__":
    main()


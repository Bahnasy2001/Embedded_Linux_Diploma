import sys

def main():
    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        # Print all command-line arguments
        print("Command-line arguments:")
        for index, arg in enumerate(sys.argv):
            print(f"Argument {index}: {arg}")
    else:
        print("No command-line arguments were Provided")
        
if __name__ == "__main__":
    main()
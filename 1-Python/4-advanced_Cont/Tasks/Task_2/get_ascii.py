def get_ascii_value(character):
    #Ensure that the input is a single  character
    if len(character) != 1:
        raise ValueError("Input must be a single character. ")
    #Get ASCII Value
    return ord(character)

def main():
    #Prompt user for input
    ch = input("Enter a character: ")
    
    try:
        #Get and Print ASCII Value
        ascii_value = get_ascii_value(ch)
        print(f"The ASCII Value of '{ch}' is {ascii_value}.")
    except ValueError as e:
        print(e)
        
if __name__ == "__main__":
    main()
# This is the main Python script executing Function(s)/Module(s) as required for the Application to run

# Main function
def main():
    print("Hello, World!")

    import Modules.select_directory

    directory = Modules.select_directory.select_directory()

    if not directory:
        print ("Null or empty directory.")
    else:
        print (directory)

# Main execution
if __name__ == "__main__":
    main()
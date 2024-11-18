# This is the main Python script executing Function(s)/Module(s) as required for the Application to run

# Main function
def main():
    import Modules.directory_services
    import Modules.openai_whisper

    # Get directory of video(s)
    # directory = Modules.directory_services.select_directory()

    ###############
    ### TESTING ###
    ###############

    directory = "C:/Users/zichu/Downloads/2024-11-17/video.mp4"
    
    print (directory)

    print ("End")

# Main execution
if __name__ == "__main__":
    main()
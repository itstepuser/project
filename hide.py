if __name__ == "__main__":
    import os
    from jaraco import path

    CHECK_STATE: bool = True # If True, the code only tells you if the parent folder is hidden (R)
    HIDDEN_FILE_LOCATION: str = "C:/Users/student/Documents/GitHub"

    if CHECK_STATE:
        print(path.is_hidden(HIDDEN_FILE_LOCATION))
        exit()

    HIDE: bool = True

    if path.is_hidden(HIDDEN_FILE_LOCATION):
        HIDE = False

    if HIDE:
        os.system("attrib +h " + HIDDEN_FILE_LOCATION)
        print("File hidden")
    else:
        os.system("attrib -h " + HIDDEN_FILE_LOCATION)
        print("File shown")
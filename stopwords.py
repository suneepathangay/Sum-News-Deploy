import string


def get_stopwords():
    with open('stopwords.txt', 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

    # Split the contents into words (this example splits by spaces)
    words = file_contents.split()

    # Optionally, you can remove any punctuation from the words
    # For a simple approach, you can use str.maketrans and str.translate
    translator = str.maketrans('', '', string.punctuation)
    words = [word.translate(translator) for word in words]

    # Remove empty strings if any
    words = list(filter(None, words))

    return words

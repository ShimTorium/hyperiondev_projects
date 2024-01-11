# Fuction to print dictionary values given the keys


def print_values_of(dictionary, *keys):  # Changed keys parameter to accept multiple arguments
    for key in keys:
        print(dictionary[key])  # Changed k to key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
                         "lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                        "homer": "d'oh!",  # changed the the phrase to 1 set of quotes
                         "maggie": "(Pacifier Suck)"
}

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

'''
    Expected console output:

    
    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''


# def pretty_print_dict(dictionary):
#     for key, value in sorted(dictionary.items()):
#         print(key, value)
#
# numbers = {
#     "one": "uno",
#     "two": "dos",
#     "three": "tres"
# }
#
# pretty_print_dict(numbers)
# print(numbers)

# answer = input("")
# def translate_shorthand(dict):
#     for key, value in dict.items():
#         if answer in key:
#             print(value)
#
# shorthand = {
#     "omg": "oh my gawd",
#     "l8r": "later",
#     "ttyl": "talk to you later",
#     "g9": "good night",
#     "gg": "good game",
#     "wtf": "what the fark",
#     "w/e": "whatever"
# }
#
# translate_shorthand(shorthand)

def letter_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency.keys():
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    print(frequency)

letter_frequency("pen pineapple apple pen")

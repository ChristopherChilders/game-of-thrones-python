from characters import characters
import requests # makes API requests (this is a third-party module)
import json # convert the API data into python dictionaries and arrays
import time # module for working with timestamps
print('there are ',len(characters), ' characters')
jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # # print out the key names individually
# for k in jon_snow:
#     print(k)

# # # print out just the values
# for k in jon_snow:
#     print(jon_snow[k])

# # # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))


#How many characters names start with "A"?
a_word_count = 0


for character in characters:
    if character['name'][0] == 'A':
        a_word_count += 1

print(a_word_count, " names start with the letter 'a'")

#How many characters names start with "Z"?

z_word_count = 0

for character in characters:
    if character['name'][0] == 'Z':
        z_word_count += 1

print(z_word_count, " names start with the letter 'z'.")


#How many characters are dead?
death_toll = 0

for death in characters:
    if death['died'] != '':
        death_toll +=1
print(death_toll, " characters are dead.")



# #Who has the most titles?
# for title in characters:
#     return len(characters['titles'])
# all_the_titles = characters["titles"]
#let assume that we have seen no titles yet

most_titles = 0
person_with_most_titles = ''
#vist each character and see if they have more than 'most_titles'
for person in characters:
        num_titles = len(person['titles'])
        if num_titles > most_titles:
                most_titles=num_titles
                # person_with_most_titles = person['name']
#print out the names of each person with the same number of titles as 'most_titles
for person in characters:
        num_titles = len(person['titles'])
        if num_titles == most_titles:
                print("%s has %d titles" %(person_with_most_titles, most_titles))

#if so, save that new value to 'most_titles.
#if not, ignore them

# print("%s has %d titles" %(person_with_most_titles, most_titles)


#Histogram
#count the number of people who are part of a house
def make_house_historgram(character_list):
        histogram = {}
        # 2. do the thing!
        #loop through all the characters
        for person in character_list:
                allegiances = person['allegiances']
                #allegiances is a list of URLs
                for house in allegiances:
                        #do something with that house
                        if house in histogram:
                                histogram[house] = histogram[house] + 1
                        else:
                                histogram[house] = 1
        return histogram

def pretty_print_histogram(histogram):
        for house in histogram:
                print('%s has %d members' %(house, histogram[house]))
def translate_address_to_house_name(URL):
        house_name = ''
        r = requests.get(URL)
        house_info = r.json()
        house_name = house_info['name']
        return house_name

def convert_to_nice_names(histogram):
        nice_histogram = {}

        for url in histogram:
                house_name = translate_address_to_house_name(url)
                nice_histogram[house_name] = histogram[url]
                time.sleep(0.1) #tells python to take a pause before returning to the loop

        return nice_histogram


# print(translate_address_to_house_name("https://www.anapioficeandfire.com/api/houses/362"))


# ugly_histogram = make_house_historgram(characters)
# pretty_histogram = convert_to_nice_names(ugly_histogram)
# pretty_print_histogram(pretty_histogram)
# # 1. check to see if it works:
print(pretty_print_histogram(make_house_historgram(characters)))
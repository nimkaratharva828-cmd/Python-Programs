db = {
    "id": 1,
    "name": "Alice",
    "age": 30,
    "city": "Delhi"
}

# Key's Method ---> It wil return all keys of our dict
all_keys = db.keys()
print("Result of keys() method:")
# for k in db.keys():
#     print(k)
for k in all_keys:
    print(k)
# for i in db:
#     print(i)
# Above all three for loops are same



# Values() method--> It will return all values of dict in list form
print("Result of values() method:")
names = db.values()
for n in names:
    print(n)


# items() method ---> It will return keys and values both in list of tuple format
print("Result of items() method:")
for h in db.items():
    print(h)


print()
print()
print()
print()
print()
print()
print()

# Level 2 : 
# Create 2025 movies dictionary with movie name is key and list of all cast is value of dictionary
movies2025 = {
    "Dhurandhar": [
        "Ranveer Singh",
        "Akshaye Khanna",
        "Arjun Rampal",
        "Sanjay Dutt",
        "Sara Arjun",
        "Rakesh Bedi",
        "R. Madhavan",
        "Danish Pandor"
    ],
    "Chhaava": [
        "Vicky Kaushal",
        "Akshaye Khanna",
        "Rashmika Mandanna",
        "Ashutosh Rana",
        "Divya Dutta",
        "Vineet Kumar Singh",
        "Neil Bhoopalam",
        "Diana Penty"
    ],
    "Saiyaara": [
        "Ahaan Panday",
        "Aneet Padda",
        "Krish Kapoor",
        "Vaani Batra",
        "Rajesh Kumar"
    ],
    "Dude": [
        "Pradeep Ranganathan",
        "Mamitha Baiju",
        "Neha Shetty",
        "Hridhu Haroon",
        "R. Sarathkumar",
        "Rohini",
        "Aishwarya Sharma"
    ],
    "Housefull 5": [
        "Akshay Kumar",
        "Abhishek Bachchan",
        "Riteish Deshmukh",
        "Jacqueline Fernandez",
        "Sonam Bajwa",
        "Nargis Fakhri",
        "Dino Morea",
        "Sanjay Dutt",
        "Jackie Shroff",
        "Nana Patekar",
        "Chitrangda Singh",
        "Fardeen Khan",
        "Chunky Panday",
        "Johnny Lever",
        "Soundarya Sharma",
        "Nikitin Dheer"
    ],
    "Badass Ravi Kumar": [
        "Himesh Reshammiya",
        "Prabhu Deva",
        "Simona J",
        "Kirti Kulhari",
        "Sunny Leone",
        "Sanjay Mishra",
        "Johnny Lever",
        "Pawan Malhotra",
        "Manish Wadhwa"
    ],
    "Kaalidhar Laapata": [
        "Abhishek Bachchan",
        "Mohammed Zeeshan Ayyub",
        "Daivik Baghela",
        "Nimrat Kaur",
        "Vishwanath Chatterjee"
    ],
    "Deva": [
        "Shahid Kapoor",
        "Pooja Hegde",
        "Pavail Gulati"
    ]
}

# Print name of all movies from dict
print("Name of all movies from dict:")
for j in movies2025.keys():
    print(j)

print()
print()
print()
print()
print()


# Print count of all actor and actress from all movies:
# count = 0
# mob = movies2025.values()
# for j in movies2025: # give name of all movies
#     for j in mob:
#         count = count + 1
#         print(j,"---->",count) 
for movie_names,casts in movies2025.items():
    print(movie_names,"-->Total cast:",len(casts))

print()
print()
print()
print()
print()
print()


# Print movies names whose having Akshay Khanna in it?
count = 0 
for movie_name, cast in movies2025.items():
    if "Akshaye Khanna" in cast:
        print("Movies with Akshay Khanna:",movie_name)
        count=count+1
print("Total movies with Akshay Khanna:",count)



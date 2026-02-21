# Create a dictionary with key:value pairs to store information about me
me = {
    "name": "John",
    "age": 47,
    "city": "Leeds",
    "job": "Head of Blogs"
}

# Loop through every key:value pair in the dictionary and print them
for key, value in me.items():
    print(f"{key}: {value}")

# Update an existing value in the dictionary
me["job"] = "Python Developer"

# Add a brand new key:value pair to the dictionary
me["language"] = "Python"

# Print the final updated dictionary to see all changes
print(me)
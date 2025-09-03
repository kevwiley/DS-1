from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products[0:3])

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference) #adds customer preferences input to customer_preferences list.
    response = input("Do you want to add another preference? (Y/N): ").upper()
print(customer_preferences)

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences_set = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.

products_with_sets = [] #new product list with sets instead of lists inside
for item in products:
    list_to_set = {"name":item["name"],"tags":set(item["tags"])} #"name" part isn't changing anything just remaking list. "tags" mkaes item a set.
    products_with_sets.append(list_to_set) #adds new dictionary to list.

# TODO: Step 5 - Write a function to calculate the number of matching tags

def count_matches(product_tags, customer_tags): 
    tag_matches = [] #list contains matches
    for item in product_tags: #loops through every item in the list.
        x = item["tags"].intersection(customer_tags) #searches the tags values in dictionary, uses intersection to compare with customer preferences
        if len(x) > 0: #makes sure that empty set isn't returned.
            tag_matches.append(x) #adds matches to list.
    print(f"This list containes {len(tag_matches)} matches") #prints total matches using len().

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches

def recommend_products(products, customer_tags):
    item_matches = [] #list contains item names
    for items in products:
        matches = len(items["tags"].intersection(customer_tags)) #gets the number of matches on a per item basis.
        if matches > 0: #also makes sure empty list isn't returned.
            item_matches.append([items["name"], matches]) #makes a list of item and amount of matches
    print("Recommended Products:")
    for product, total_matches in item_matches: #code loops through item_matches list, takes first and second item in nested list
        print(f"- {product} ({total_matches} match(es))") #prints product name and matches.
# TODO: Step 7 - Call your function and print the results

count_matches(products_with_sets,customer_preferences_set)
recommend_products(products_with_sets,customer_preferences_set)


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

#response in response.txt
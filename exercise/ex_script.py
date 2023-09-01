import requests

def fetch_product_data(product_id):
    url = f"https://fakestoreapi.com/products/{product_id}"
    response = requests.get(url)
    
    try:
        response.raise_for_status()  # Raise an exception if the response status code is not 200
        product_data = response.json()
        return product_data
    except requests.exceptions.HTTPError as e:
        print("Error:", e)
    except requests.exceptions.JSONDecodeError as e:
        print("Error: Invalid JSON response")
    
    return None

def display_product_data(product_data):
    if product_data is not None:
        print("Product Name:", product_data["title"])
        print("Product Category:", product_data["category"])
        print("Product Price:", product_data["price"])
        print("Product Description:", product_data["description"])
    else:
        print("Error: No product data to display.")

# Interactive version (Bonus)
product_id = input("Enter the product ID: ")
product_data = fetch_product_data(product_id)
display_product_data(product_data)
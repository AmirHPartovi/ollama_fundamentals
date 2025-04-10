import ollama
import os

model="llama3.2"

input_dir = "./data/grocery_list.txt"
output_dir = "./data/grocery_list_categorized"

if not os.path.exists(input_dir):
    print(f"Input file {input_dir} does not exist.")
    exit(1)



#read input file
with open(input_dir, "r") as f:
    items = f.read().strip()


# Prepare the prompt for the model
prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""

# Send the prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("==== Categorized List: ===== \n")
    print(generated_text)

    # Write the categorized list to the output file
    with open(output_dir, "w") as f:
        f.write(generated_text.strip())

    print(f"Categorized grocery list has been saved to '{output_dir}'.")
except Exception as e:
    print("An error occurred:", str(e))

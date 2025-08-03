# 1. Create dictionary with 4 categories
categories = {
    "fruits": {"apple": [10, 30], "banana": [20, 10]},
    "vegetables": {"carrot": [15, 5], "tomato": [10, 8]},
    "electronics": {"phone": [5, 10000], "laptop": [3, 50000]},
    "clothes": {"shirt": [10, 500], "jeans": [5, 1200]}
}

# 2. Print category items in asc or desc
def print_items(order="asc"):
    for category, items in categories.items():
        print(f"\nCategory: {category}")
        sorted_items = sorted(items.items(), reverse=(order == "desc"))
        for item, data in sorted_items:
            print(f"  {item} -> Quantity: {data[0]}, Price: {data[1]}")

# 3. Print average of quantity and price per category
def print_averages():
    for category, items in categories.items():
        total_qty = sum(data[0] for data in items.values())
        total_price = sum(data[1] for data in items.values())
        count = len(items)
        avg_qty = total_qty / count
        avg_price = total_price / count
        print(f"\nCategory: {category}")
        print(f"  Avg Quantity: {avg_qty:.2f}, Avg Price: {avg_price:.2f}")

# 4. Frequency of letters in a string using dictionary
def letter_frequency(s):
    freq = {}
    for ch in s:
        if ch.isalpha():
            ch = ch.lower()
            freq[ch] = freq.get(ch, 0) + 1
    print("\nLetter Frequencies:")
    for k, v in freq.items():
        print(f"  {k} -> {v}")

# ----- Call Functions -----
print("🔸 Items in Ascending Order:")
print_items("asc")

print("\n🔸 Items in Descending Order:")
print_items("desc")

print("\n🔸 Averages of Quantity and Price:")
print_averages()

print("\n🔸 Letter Frequency:")
letter_frequency("Dictionary Example for Frequency of Letters")

#Every Function

fruits = ["mango", "apple", "banana", "strawberry", "grape",
          "orange", "pineapple", "watermelon", "kiwi", "peach"]

print(f"Total fruits: {len(fruits)}")

print(f"\nOriginal list:")
print(fruits)

print(f"\nTemporary sorted (sorted()):")
print(sorted(fruits))

print(f"\nAfter sorted(), original is unchanged:")
print(fruits)

fruits.sort()
print(f"\nAfter sort() - permanent ascending:")
print(fruits)

fruits.reverse()
print(f"\nAfter reverse():")
print(fruits)
#Sandwiches

def make_sandwich(*items):
    print("Sandwich berisi:")
    for item in items:
        print("-", item)

make_sandwich("keju", "tomat")
make_sandwich("ayam", "selada", "saus")
make_sandwich("telur", "keju", "mayones", "selada")

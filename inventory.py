#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print (v, k)
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        if item in inventory:
            inventory[item]+= 1
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

#print (inv)
displayInventory(inv)
#displayInventory(stuff)
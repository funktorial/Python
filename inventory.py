stuff = {'rope': 3, 'gold': 4214, 'mana': 5, 'weapon': 2, 'antidote': 99}
inv = {'gold coin': 42, 'ruby': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        if v > 1:
            print(str(v) + ' ' + k + 's')
        else:
            print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
    
def addToInventory(inventory,addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] = inventory[item]+1
    displayInventory(inventory) 

class HiddenList:
    def __init__(self, items):
        self.items = items
        self.hidden_indices = set()

    def hide(self, index):
        if 0 <= index < len(self.items):
            self.hidden_indices.add(index)
        else:
            print("Index out of range")

    def show(self, index):
        if index in self.hidden_indices:
            self.hidden_indices.remove(index)
        else:
            print("Index not hidden")

    def __getitem__(self, index):
        if index in self.hidden_indices:
            print("This element is hidden")
            return None
        return self.items[index]

    def __len__(self):
        return len(self.items) - len(self.hidden_indices)

    def __str__(self):
        visible_items = [self.items[i] for i in range(len(self.items)) if i not in self.hidden_indices]
        return str(visible_items)


my_list = HiddenList([1, 2, 3, 4, 5])

print("Original List:", my_list)

my_list.hide(2)  # Hide element at index 2
print("After hiding index 2:", my_list)

my_list.hide(0)  # Hide element at index 0
print("After hiding index 0:", my_list)


# create a class
# 
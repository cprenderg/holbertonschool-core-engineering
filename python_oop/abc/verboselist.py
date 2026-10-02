#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        i = 0
        for item in items:
            i += 1
        print(f"Extended the list with [{i}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)

    def pop(self, item=None):
        if item is None:
            popped = super().pop()
        else:
            popped = super().pop(item)
        print(f"Popped [{popped}] from the list.")
        return popped

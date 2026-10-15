# -*- coding: utf-8 -*-


def increase_quality(item):
    if item.quality < 50:
        item.quality += 1
    
def decrease_quality(item):
    if item.quality > 0:
        item.quality -= 1

def decrease_sell_in(item):
    item.sell_in = item.sell_in - 1
    
def update_item(item):
    ageBrie = "Aged Brie"
    backstage = "Backstage passes to a TAFKAL80ETC concert"
    sulfuras = "Sulfuras, Hand of Ragnaros"

    if item.name == sulfuras:
        return
    
    if item.name != ageBrie and item.name != backstage:
        decrease_quality(item)
    else:
        increase_quality(item)
        if item.name == backstage:
            if item.sell_in < 11:
                increase_quality(item)
            if item.sell_in < 6:
                increase_quality(item)

    decrease_sell_in(item)

    if item.sell_in < 0:
        if item.name != ageBrie:
            if item.name != backstage:
                decrease_quality(item)
            else:
                item.quality = 0
        else:
            increase_quality(item)

def update_quality(items):
    for item in items:
        update_item(item)
    return items

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

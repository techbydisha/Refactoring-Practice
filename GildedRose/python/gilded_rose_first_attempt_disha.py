# -*- coding: utf-8 -*-

MAX_QUALITY = 50
MIN_QUALITY = 0
MIN_SELL_IN = 0

def increase_quality(item):
    if item.quality < MAX_QUALITY:
        item.quality += 1
    
def decrease_quality(item):
    if item.quality > MIN_QUALITY:
        item.quality -= 1

def decrease_sell_in(item):
    item.sell_in -= 1
     
def update_regular_item(item):
    decrease_quality(item)
    decrease_sell_in(item)
    if item.sell_in < MIN_SELL_IN:
        decrease_quality(item)
    
def update_aged_brie(item):
    increase_quality(item)
    decrease_sell_in(item)
    if item.sell_in < MIN_SELL_IN:
        increase_quality(item)
    
def update_backstage(item):
    increase_quality(item)
    if item.sell_in < 11:
        increase_quality(item)
    if item.sell_in < 6:
        increase_quality(item)
    decrease_sell_in(item)
    if item.sell_in < MIN_SELL_IN:
        item.quality = MIN_QUALITY

def update_item(item):
    ageBrie = "Aged Brie"
    backstage = "Backstage passes to a TAFKAL80ETC concert"
    sulfuras = "Sulfuras, Hand of Ragnaros"

    if item.name == sulfuras:
        return
    elif item.name == ageBrie:
        update_aged_brie(item)
    elif item.name == backstage:
        update_backstage(item)
    else:
        update_regular_item(item)
    
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

"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}


ice_cream["vanilla"] += 110
print(ice_cream["vanilla"])

ice_cream.pop("strawberry")
print(ice_cream)

print("pbj" in ice_cream)

total_orders: int = 0
for flavor in ice_cream:
    total_orders += ice_cream[flavor]
print(total_orders)

print(ice_cream["pecan"])

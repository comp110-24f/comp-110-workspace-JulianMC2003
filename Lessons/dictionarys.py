ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

print(len(ice_cream))

ice_cream["vanilla"] += 10

ice_cream.pop("strawberry")

total_orders: int = 0

for flavor in ice_cream:
    total_orders += ice_cream[flavor]

print(total_orders)

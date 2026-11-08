"""Netflix."""


def get_available_plans(laptop_tv, hd_req, ultra_hd_req):
    """Determine available plans based on requirements."""
    if ultra_hd_req == "Yes":
        return [("Premium", 419, 4)]
    if hd_req == "Yes":
        return [("Premium", 419, 4), ("Standard", 349, 2)]
    if laptop_tv == "Yes":
        return [("Premium", 419, 4), ("Standard", 349, 2), ("Basic", 279, 1)]
    return [
        ("Premium", 419, 4),
        ("Standard", 349, 2),
        ("Basic", 279, 1),
        ("Mobile", 99, 1),
    ]


def find_best_combo(available_plans, target):
    """Find cheapest package combination for target units."""
    max_cap = max(cap for _, _, cap in available_plans)
    limit = target + max_cap

    dp = [
        (float("inf"), {p[0]: 0 for p in available_plans})
        for _ in range(limit + 1)
    ]
    dp[0] = (0, {p[0]: 0 for p in available_plans})

    for cap in range(limit):
        if dp[cap][0] == float("inf"):
            continue
        for name, price, capacity in available_plans:
            next_cap = cap + capacity
            if next_cap <= limit:
                new_cost = dp[cap][0] + price
                if new_cost < dp[next_cap][0]:
                    new_combo = dp[cap][1].copy()
                    new_combo[name] += 1
                    dp[next_cap] = (new_cost, new_combo)

    best_cost = float("inf")
    best_combo = None
    for cap in range(target, limit + 1):
        if dp[cap][0] < best_cost:
            best_cost = dp[cap][0]
            best_combo = dp[cap][1]

    return best_cost, best_combo


def main():
    """Run Netflix package recommendation."""
    screens = int(input())
    downloads = int(input())
    _ = input()  # unlimited movies
    _ = input()  # mobile phone and tablet
    laptop_tv = input().strip()
    hd_req = input().strip()
    ultra_hd_req = input().strip()

    target = max(screens, downloads)
    available_plans = get_available_plans(laptop_tv, hd_req, ultra_hd_req)
    total_cost, combo = find_best_combo(available_plans, target)

    order = ["Premium", "Standard", "Basic", "Mobile"]
    for plan_name in order:
        if plan_name in combo and combo[plan_name] > 0:
            print(f"{plan_name} x {combo[plan_name]}")

    print(f"Total = {total_cost} THB")


main()

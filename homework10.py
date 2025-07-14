def unicorns_to_rainbows(unicorns: list[dict]) -> list[str]:
    return [f"Rainbow unicorn of color {u['color']}" for u in unicorns]
if __name__ == "__main__":
    unicorns = [{"color": "pink"}, {"color": "blue"}, {"color": "sparkly"}]
    print(unicorns_to_rainbows(unicorns))
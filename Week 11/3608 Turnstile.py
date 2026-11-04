"""Turnstile"""

def main():
    """Simulate turnstile state machine and count people."""
    is_locked = True
    passed = 0

    while True:
        action = input().strip()
        if action == "END":
            break
        if action == "C":
            is_locked = False
        elif action == "P" and not is_locked:
            passed += 1
            is_locked = True
    print(passed)
main()

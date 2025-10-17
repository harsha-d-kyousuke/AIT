facts = [
    "john_is_cold.",
    "raining.",
    "john_Forgot_His_Raincoat.",
    "fred_lost_his_car_keys.",
    "peter_footballer."
]

def verify_fact(fact):
    fact = fact.rstrip(".")
    fact = fact.lower()
    if fact == "john_forgot_his_raincoat":
        return True
    elif fact == "raining":
        return True
    elif fact == "foggy":
        return True
    elif fact == "cloudy":
        return False
    else:
        return False

for f in facts:
    result = verify_fact(f)
    print(f"{f} → {result}")

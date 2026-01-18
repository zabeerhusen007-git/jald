def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))

    si = calculate_simple_interest(p, r, t)
    print("Simple Interest:", si)

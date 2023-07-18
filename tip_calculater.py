def main():
    dollars_to_float()
    _dollars_to_float()
    d_ollars_to_float()


def dollars_to_float():
    print("Type meal amount $50.0")
    d=input("$ meal amount ").strip("$")
    dollars=float(d)
    print("percentage tip $15%")
    p=input("$ tip percentage ").strip("$").strip("%")
    pp=(int(p))/100
    percent=pp
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def _dollars_to_float():
    print("Type meal amount $100.0")
    d=input("$ meal amount ").strip("$")
    dollars=float(d)
    print("percentage tip $18%")
    p=input("$ tip percentage ").strip("$").strip("%")
    pp=(int(p))/100
    percent=pp
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def d_ollars_to_float():
    print("Type meal amount $15.0")
    d=input("$ meal amount ").strip("$")
    dollars=float(d)
    print("percentage tip $25%")
    p=input("$ tip percentage ").strip("$").strip("%")
    pp=(int(p))/100
    percent=pp
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()
def add(a, b):
    return a + b

def main():
    res = addd(2, 3)  # BUG: 'addd' is not defined
    print("Result:", res)

if __name__ == "__main__":
    main()

#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add

    def main():
        a = 1
        b = 2

        result = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, result))

    main()

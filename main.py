from circle import Circle


def main():
    while True:
        n = int(input("n> "))
        m = int(input("m> "))
        o = int(input("o> "))

        if n > 0 and m >= 0 and o >= 0 and (m + o) > 0:
            break
        print("Invalid input. Please enter again.")

    circle = Circle()
    for i in range(1, n + 1):
        circle.append(i)

    circle.print_circle()
    while circle.size > 0:
        circle.move_current(m, clockwise=True)
        removed = circle.remove_next()
        print(f"{removed} is removed")
        circle.print_circle()
        circle.move_current(o, clockwise=False)


if __name__ == "__main__":
    main()

# Samir Rodriguez
# Module 1.3 Assignment
# 10/27/24

def countdown(number_of_bottles):
    for bottles in range(number_of_bottles, 0, -1):
        if bottles >1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottles of the beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of the beer on the wall.\n")

    print("No more bottles of beer on the wall. Buy more beer!")

def main():
    try:
        number_of_bottles = int(input("How many bottles of beer are on the wall?"))
        if number_of_bottles < 0:
            print("Please enter a non-negative number.")
        else:
            countdown(number_of_bottles)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()                
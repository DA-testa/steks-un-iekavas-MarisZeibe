# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or not are_matching(opening_brackets_stack.pop().char, next):
                return i+1
            pass

    return "Success" if len(opening_brackets_stack) == 0 else opening_brackets_stack.pop(0).position+1


def main():
    # Printing answer, write your code here
    inputType = input()
    text = input()
    if inputType == "F":
        mismatch = find_mismatch(open("test/" + text, "r").read())
    elif inputType == "I":
        mismatch = find_mismatch(text)
    else:
        return
    print(mismatch)


if __name__ == "__main__":
    main()

def balanced(str):
    stack = []
    for char in str:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                current_char = stack.pop()
                if current_char == "(":
                    if char != ")":
                        return False
                if current_char == "{":
                    if char != "}":
                        return False
                if current_char == "[":
                    if char != "]":
                        return False

    if stack:
        return False
    else:
        return True

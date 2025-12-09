RUN_INDENTED = True

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello my function is executed"
    return greet


print(my_function())

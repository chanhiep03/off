def greet(name: str = "World") -> None:
    """
    打印问候语。

    :param name: 要问候的名字，默认为"World"
    :type name: str
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
def build_pipeline(operation_names):
    operations = {
        "add_one": lambda x: x + 1,
        "double": lambda x: x * 2,
        "triple": lambda x: x * 3,
        "square": lambda x: x * x,
        "negate": lambda x: -x
    }

    for name in operation_names:
        if name not in operations:
            raise KeyError(name)

    def pipeline(x):
        for name in operation_names:
            x = operations[name](x)
        return x

    return pipeline




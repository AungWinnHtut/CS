while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
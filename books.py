def getting_fullname(first_name: str, last_name: str):
    full_name = first_name.title()+ " " + last_name.title()
    return full_name

if __name__ == "__main__":
    first_name = "bahodir"
    last_name = "Erkinov"
    print(getting_fullname(first_name, last_name))
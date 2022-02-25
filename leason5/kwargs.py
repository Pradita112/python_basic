def fullname(**kwargs):
    print(kwargs)
    print(f"nama saya adalah {kwargs['first_name']}{kwargs['last_name']}")

    fullname(last_name="pradita",first_name="adit")

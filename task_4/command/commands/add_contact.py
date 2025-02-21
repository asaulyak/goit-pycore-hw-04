COMMAND_NAME = 'add'

def run(args, context):
    stop = False

    if len(args) < 2:
        message = "Invalid arguments"

        return message, context, stop

    name, phone = args

    if not name or not phone:
        message = "Invalid arguments"

        return message, context, stop

    if not name.isalpha():
        message = "Invalid name"

        return message, context, stop

    if not phone.isdigit():
        message = "Invalid phone number"

        return message, context, stop

    contact = {name: phone}

    message = "Contact added."
    updated_context = {**context, **contact}

    return message, updated_context, stop
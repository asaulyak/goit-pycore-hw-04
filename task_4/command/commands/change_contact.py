COMMAND_NAME = 'change'

def run(args, context):
    stop = False

    if len(args) < 2:
        message = "Invalid arguments"

        return message, context, stop

    name, phone = args

    if not name or not phone:
        message = "Invalid arguments"

        return message, context, stop

    if name not in context:
        message = "Contact not found"

        return message, context, stop

    if not phone.isdigit():
        message = "Invalid phone number"
        return message, context, stop

    contact = {name: phone}

    message = "Contact updated."
    updated_context = {**context, **contact}

    return message, updated_context, stop
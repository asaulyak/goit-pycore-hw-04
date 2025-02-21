COMMAND_NAME = 'phone'

def run(args, context):
    if len(args) < 1:
        message = "Invalid arguments"

        return message, context

    contact = args[0]
    updated_context = context
    stop = False

    if not contact:
        message = "Invalid arguments."

        return message, updated_context, stop

    phone = context.get(contact)

    if not phone:
        message = "Contact not found."
    else:
        message = str(phone)

    return message, updated_context, stop
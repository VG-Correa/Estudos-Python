def simple_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("oi","ola","olá"):
        return("E ai, beleza?")
    elif "beleza e você?" in user_message:
        return "Tudo bom frô"
    elif "eu te amo" in user_message:
        return "Eu te amo muuuuuuuuuito mais, muuuuito mais u.u, sua coisa linda, delícia, gotosa, coisa mais show de bola, te amo muuuuuito frô S2\nÉ noix tamo junto!"
    else:
        return "Não fui programado para responder isso :/!"


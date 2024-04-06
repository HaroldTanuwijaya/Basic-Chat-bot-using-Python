from chatbot import Chat, register_call
import wikipedia


@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query

first_question=" Tugas DPJ 1 \n\nInput dimulai dengan kalimat berikut dan dilanjutkan dengan query yang ingin ditanya :\n-do you know about \n-what is  \n-who is  \n-tell me about\n\n\n Example : tell me about Jupiter"
Chat("examples/Example.template").converse(first_question)


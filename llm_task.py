
def generate_prompt(user_text):
    return f"Skaidrojamais teksts: {user_text}"


def local_llm_explainer(text):
    explanations = {
        "mākslīgais intelekts": "datorprogramma, kas mēģina domāt līdzīgi cilvēkam",
        "algoritms": "noteikumu kopums, kas pasaka datoram, ko darīt",
        "dati": "informācija, ko izmanto dators",
        "neironu tīkls": "modelis, kas atdarina smadzeņu darbību",
        "mašīnmācīšanās": "veids, kā dators mācās no piemēriem"
    }

    simplified = text.lower()

    for term, explanation in explanations.items():
        if term in simplified:
            simplified = simplified.replace(term, explanation)

    return (
        "Vienkāršots skaidrojums:\n"
        + simplified.capitalize()
    )


# Ievade
user_input = input("Ievadi tekstu, kuru paskaidrot: ")

# Prompt
prompt = generate_prompt(user_input)

# Lokālā modeļa rezultāts
result = local_llm_explainer(user_input)

# Izvade konsolē
print("\n-Prompt-")
print(prompt)

print("\n-AI skaidrojums-")
print(result)

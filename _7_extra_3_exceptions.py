def process_data(data: list[str]):


    if not data:
        raise ValueError("No data available")

    for record in data:
        try:
            print(record)
        except:
            print("error in processing... ")

process_data(["kosik", "rohlik", "svacina"])

process_data([])


def vydel_dve_cisla(a, b):
    return a / b


vydel_dve_cisla(5, 1)
vydel_dve_cisla(5, 0)

a, b = 17, 0
vydel_dve_cisla(a, b)

try:
    vydel_dve_cisla(a, b)
except:
    print("Hmm, nastala nejaka chyba.")

##############
try:
    vydel_dve_cisla(a, b)
    ...
    ...
except ValueError:
    print("Hmm, nastala value error.")
except TypeError:
    print("Hmm, nastala type error.")
except ZeroDivisionError:
    print("Hmm, nastala chyyba pri deleni nulou.")
except:
    print("chyba.... ")



########################################



try:
    process_data([])
except ValueError:
    ...
    ...
    print("chybu jsme zachytili ... ")
    # logger.error()

try:
    ...
except ValueError:
    ...


print("program pokracuje...")

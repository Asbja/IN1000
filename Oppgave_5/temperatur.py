def hoved():
    månedTemp = open("max_temperatures_per_month.csv", "r")
    ordbok = lagOrdbok(månedTemp)

    dagligTemp = open("max_daily_temperature_2018.csv")
    ordbok2 = sammenlignTemp(ordbok, dagligTemp)

    månedTemp2 = open("max_temperatures_per_month_updated.csv", "w")
    endreMånedTemp(ordbok2, månedTemp2)

    repVarmebølge(dagligTemp)



def lagOrdbok(månedTemp):
    ordbok = {}

    for ln in månedTemp:
        biter = ln.split(",")
        ordbok[biter[0]] = float(biter[1])

    return ordbok



def sammenlignTemp(ordbok, dagligTemp):
    print(dagligTemp)

    for ln in dagligTemp:
        biter = ln.split(",")

        if float(biter[2]) > ordbok[biter[0]]:
            # print(f"Ny varmerekord på {biter[1]} {biter[0]}: {float(biter[2])} grader celcius (gammel varmerekord var {ordbok[biter[0]]} grader celcius)")
            ordbok[biter[0]] = float(biter[2])

    return ordbok



def endreMånedTemp(ordbok, månedTemp):
    for el in ordbok:
        månedTemp.write(f"{el},{ordbok[el]}\n")
    månedTemp.close()



def repVarmebølge(dagligTemp):
    print(dagligTemp)

    for el in dagligTemp:
        print("funker")
        biter = el.split(",")
        print(biter)
        if float(biter[2]) > 25:
            print(biter)



hoved()

#tehtävä 5
print("Anna leiviskät.")
leiviskät = float(input())
print("Anna naulat.")
naulat = float(input())
print("Anna luodit.")
luodit = float(input())
print("Massa nykymittojen mukaan:")

luoditgrammat = 13.3 * luodit
naulatgrammat = (32 * 13.3) * naulat
leiviskätgrammat = (20 * 32 * 13.3) * leiviskät
kilogrammat = (luoditgrammat + naulatgrammat + leiviskätgrammat) // 1000
grammat = (luoditgrammat + naulatgrammat + leiviskätgrammat) % 1000
print(str(f"{kilogrammat:.0f}") + " kilogrammaa ja " + str(f"{grammat:.2f}") + " grammaa.")
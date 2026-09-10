gallonit = input("Anna gallonit: ")

def gallonit_litroiksi(gallonit):
    return gallonit * 3.785

litroiksi = gallonit_litroiksi(float(gallonit))
print(f"{gallonit} gallonia on {litroiksi:.2f} litraa.")
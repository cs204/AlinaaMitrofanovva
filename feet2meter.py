def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    v = v[0:-2]
    v = float(v)
    return v*0.3048

main()






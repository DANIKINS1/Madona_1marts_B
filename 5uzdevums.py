def write_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content + '\n')
        return True
    except IOError as e:
        print(f"Kļūda: {e}")
        return False

def main():
    filename = "lietotajs.txt"

    while True:
        try:
            username = input("Lūdzu, ievadiet savu vārdu (vai 'exit', lai izietu): ")
            if username.lower() == 'exit':
                break
            if write_to_file(filename, username):
                print("Vārds veiksmīgi ierakstīts failā.")
        except KeyboardInterrupt:
            print("\nProgramma pārtraukta ar Ctrl+C.")
            break

if __name__ == "__main__":
    main()
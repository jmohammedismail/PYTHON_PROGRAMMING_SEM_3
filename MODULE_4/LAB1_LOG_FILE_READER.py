# MODULE 4 - LAB 1
# Log File Reader Program
# Reads log.txt, displays it line by line, counts ERROR messages,
# and handles the case where the file does not exist.

def read_log_file():
    try:
        with open("log.txt", "r", encoding="utf-8") as file:
            error_count = 0

            print("\n----- LOG FILE CONTENTS -----")
            for line in file:
                line = line.rstrip("\n")
                print(line)

                if "ERROR" in line.upper():
                    error_count += 1

            print("\n----- ERROR SUMMARY -----")
            print("Total ERROR messages:", error_count)

    except FileNotFoundError:
        print("Error: log.txt does not exist.")
    except OSError as error:
        print("Error while reading the log file:", error)


if __name__ == "__main__":
    read_log_file()

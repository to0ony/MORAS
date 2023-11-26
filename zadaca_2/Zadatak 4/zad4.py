with open("zadatak4.asm", "w") as file:
    # Postavljanje lijeve vertikale
    memory_address = 16384
    for i in range(128):
        file.write(f"@{memory_address}\n")
        file.write("M = 1\n\n")
        memory_address += 32

    # Postavljanje gornje horizontalne
    memory_address = 16384
    for i in range(128//16):
        file.write(f"@{memory_address}\n")
        file.write("M = -1\n\n")
        memory_address += 1

    # file.write("@32768 \n")
    # file.write("D = A; \n")
    # file.write("D = D + 1; \n")
    # file.write("D = -D; \n")
    

    # Postavljanje desne vertikale
    memory_address = 16384 + 8
    for i in range(128):
        file.write(f"@{memory_address}\n")
        file.write("M = 1\n\n")  
        memory_address += 32

    # Postavljanje donje horizontalne
    memory_address = 16384 + 32 * (128 - 1)
    for i in range(128//16):
        file.write(f"@{memory_address}\n")
        file.write("M = -1\n\n")  
        memory_address += 1
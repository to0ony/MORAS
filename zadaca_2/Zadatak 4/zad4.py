start_address = 16384

with open("zadatak4.asm", "w") as file:
    # Postavljanje lijeve vertikale
    memory_address = start_address
    for i in range(128):
        file.write(f"@{memory_address}\n")
        file.write("M = 1\n\n")
        memory_address += 32

    # Postavljanje gornje horizontalne
    memory_address = start_address
    for i in range(128//16):
        file.write(f"@{memory_address}\n")
        file.write("M = -1\n\n")
        memory_address += 1

    file.write("@32767 \n")
    file.write("D = A; \n")
    file.write("D = D + 1; \n")
    file.write("D = -D; \n")
    

    # Postavljanje desne vertikale
    memory_address = start_address + 39
    for i in range(126):
        file.write(f"@{memory_address}\n")
        file.write("M = D\n\n")  
        memory_address += 32

    # Postavljanje donje horizontalne
    memory_address = start_address + 32 * (128 - 1)
    for i in range(128//16):
        file.write(f"@{memory_address}\n")
        file.write("M = -1\n\n")  
        memory_address += 1

    # Postavljanje glavne dijagonale
    memory_address = start_address + 32 * 16 + 1
    j = 1
    for i in range(96):
        if j == 32768:
            file.write("@32767 \n")
            file.write("D = A; \n")
            file.write("D = D + 1; \n")
            file.write("D = -D; \n")
            j = 1
        else:
            file.write(f"@{j}\n")
            file.write("D = A\n")
            j *= 2

        file.write(f"@{memory_address}\n")
        file.write("M = D\n\n")
        memory_address += 32

        if(j == 1): memory_address += 1

    # Postavljanje sporedne dijagonale
    memory_address = start_address + 32 * 16 + 6
    j = 32768
    for i in range(96):
        if j == 32768:
            file.write("@32767 \n")
            file.write("D = A; \n")
            file.write("D = D + 1; \n")
            file.write("D = -D; \n")
        else:
            file.write(f"@{j}\n")
            file.write("D = A\n")
        
        j //= 2
        file.write(f"@{memory_address}\n")
        file.write("M = D\n\n")
        memory_address += 32

        if(j == 0): 
            memory_address -= 1
            j = 32768

    file.write("(END)\n")
    file.write("@END\n")
    file.write("0; JMP\n")
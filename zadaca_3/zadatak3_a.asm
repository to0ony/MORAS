@0
D = M
$MV(D, R2) // R2 = R0 (baza)

@1
D = M
$MV(D, R3) // R3 = R1 (eksponent)

@1
D = A
$MV(D, R4) // R4 = 1

@END
D; JEQ

(LOOP)
  $SUM(R2, R4, R4) // R4 = R2 + R4

  $SUM(R3, @NEG_ONE, R3) // R3 = R3 - 1

  @LOOP
  D; JGT

(END)
@END
0; JMP

(NEG_ONE)
@-1
D = A
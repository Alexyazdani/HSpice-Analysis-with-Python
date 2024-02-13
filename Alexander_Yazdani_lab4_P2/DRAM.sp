
** Simple DRAM cell and sweep

.include CMOSN.inc
.include dram_sweep_data.txt

.PARAM W_VAL = 120e-9
.PARAM C_VAL = 1fF

** Circuit Netlist

** Supply
VSUP X 0 0.8
VG   Y 0 0

** Transistor
M1 X Y Z Z   CMOSN L=45e-9 W=W_VAL

** Capacitor
C1 Z 0 C_VAL

** Initial Conditions
.IC V(Z)   = 0.8


** Analysis Setup
.TRAN 0.1n 200u SWEEP data = mydata


** Control Information
.OPTION POST BRIEF NOMOD PROBE MEASOUT

** Print and Measurement
**.PRINT V(Z)
.MEASURE TRAN RTL TRIG AT=0 TARG V(Z) VAL=0.6 FALL=1
.MEASURE TRAN AVG_CUR AVG I(C1) FROM 0 to 'RTL'
.MEASURE TRAN AVG_PWR AVG P(C1) FROM 0 to 'RTL'

.END

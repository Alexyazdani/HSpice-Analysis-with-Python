"""
Alex Yazdani
EE 477L
Lab 4 Part 2
"""

filename = "dram_sweep_result.txt"
RTL = []
Iavg = []
Pavg = []

def main():
    setup_file = open("dram_sweep_data.txt", 'r')
    result_file = open(filename, 'w')
    datafile = open("dram_sweep.lis", 'r')

    for line in datafile:
        if "rtl" in line:
            new_rtl = line.split("=")[1].split()[0].replace(" ", "")
            while len(new_rtl) < 9:
                new_rtl += " "
            RTL.append(new_rtl)
        elif "avg_cur" in line:
            new_cur = line.split("=")[1].split()[0].replace(" ", "")
            while len(new_cur) < 9:
                new_cur += " "
            Iavg.append(new_cur)
        elif "avg_pwr" in line:
            new_pwr = line.split("=")[1].split()[0].replace(" ", "")
            while len(new_pwr) < 9:
                new_pwr += " "
            Pavg.append(new_pwr)

    result_file.write("TEMP      W         C         RTL          Iavg          Pavg\n")
    for i, line in enumerate(setup_file):
        if i < 2:
            continue
        new_line = line.lstrip().replace("\n", "") + "     " + RTL[i-2] + "    " + Iavg[i-2] + "    " + Pavg[i-2] + "\n"
        result_file.write(new_line)




if __name__ == "__main__":
    main()

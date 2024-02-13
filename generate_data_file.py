"""
Alex Yazdani
EE 477L
Lab 4 Part 2

Code from lab demonstration used for reference.
"""

file_name = "dram_sweep_data.txt"

def main():
    t_values = [25, 85]  
    w_values = [120, 180, 240, 300]
    c_values = [0.01] + [8**(0.1 * i) for i in range(1, 11)]

    file = open(file_name, 'w')
    file.write(".DATA     mydata\n")
    file.write("+      TEMP     W_VAL      C_VAL\n")

    for temp in t_values:
        for w in w_values:
            for c in c_values:
                line = f"       {temp}       {w}n       {c:.2f}f\n"
                file.write(line)

    file.close()

if __name__ == "__main__":
    main()

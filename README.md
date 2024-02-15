Alex Yazdani
EE477L
Lab 4
Fall 2023

This project demonstrates how to use python to analyze HSpice simulation data.

The Hspice script used is DRAM.sp. The variables C_VAL and W_VAL were created. This allows the script to sweep over a range of values.
These are specified by dram_sweep_data.txt, which is included in a statement at the beginning of the script. In the .TRAN line, “SWEEP data = mydata” is appended, which lets the script know what data to sweep.

The first script, generate_data_file.py, generates the .txt file containing the values for Hspice to sweep. The .py file starts by setting up lists containing the variable combinations necessary. It then begins writing to a .txt file, considering every variable combination through nested for loops. The file is then closed.
Once the Hspice simulation is complete and a .lis file has been generated, the next python script, construct_results_file.py, can be run. This script examines the .lis file line by line, searching for a match for the strings “rtl”, “avg_cur”, and “avg_pwr”. It will then use .split() to pull out the proper values. Because some values have a different number of significant figures, these extracted strings were padded with spaces to make them fall within the same column when a monospaced font is used. A new file, dram_sweep_result.txt, is constructed using the .txt file generated from the first python file, as well as the extracted data from the .lis file.
Instead of rounding the data values, it will keep as many significant figures as Hspice reports.

Nothing is necessary to run the first script. For the second script, the .lis file and the .txt file generated from the previous script must be present in the same directory. They must be named dram_sweep.lis and dram_sweep_data.txt respectively.


import re
import sys
from collections import defaultdict
from prettytable import PrettyTable

def count_registers(file_path, registers_to_track):
    register_counts = defaultdict(int)
    
    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.split()
            if len(tokens) < 2:
                continue
            
            # Extract registers used in the instruction
            used_registers = re.findall(r'\b\w+\b', line)
            
            for reg in used_registers:
                if reg in registers_to_track:
                    register_counts[reg] += 1
    
    return register_counts

# Generate the register set
a_registers = {f"a{i}" for i in range(8)}
s_registers = {f"s{i}" for i in range(12)}
t_registers = {f"t{i}" for i in range(7)}
n_registers = {f"n{i}" for i in range(97)}
registers_to_track = a_registers | s_registers | t_registers | n_registers

# Get file name from command line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <assembly_file>")
    sys.exit(1)

file_path = sys.argv[1]
counts = count_registers(file_path, registers_to_track)

# Sorting function to ensure correct order
def register_sort_key(reg):
    match = re.match(r'([a-z]+)(\d+)', reg)
    if match:
        return match.group(1), int(match.group(2))
    return reg, 0  # Default fallback

# Create and display the table
table = PrettyTable(["Register", "Count"])
for reg, count in sorted(counts.items(), key=lambda x: register_sort_key(x[0])):
    table.add_row([reg, count])

# Add a row for the total number of unique registers used
total_unique = len(counts)
table.add_row(["Total Unique Registers", total_unique])

print(table)

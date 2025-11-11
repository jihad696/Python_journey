import os

# ================= Part 1: Create Folder & Files =================

base_folder = os.path.join(
    os.path.expanduser("~"), r"OneDrive\Desktop\elzero_pyhton\65-68"
)
python_path = os.path.join(base_folder, "Python_two")
os.makedirs(python_path, exist_ok=True)

assign_file_path = os.path.join(python_path, "assign.txt")

with open(assign_file_path, "w") as f:
    f.write("Hello_from_assign")

with open(assign_file_path, "r") as f:
    print(f.read())

folder = r"C:\Users\Gehad\OneDrive\Desktop\elzero_pyhton\65-68\Desktop\Python"

for i in range(1, 51):
    if i == 25:
        special_path = os.path.join(folder, "special-text.txt")
        with open(special_path, "w"):
            pass
        print("special file is created")
    else:
        file_path = os.path.join(folder, f"txt{i}.txt")
        with open(file_path, "w") as f:
            f.write(f"Elzero Web School => {i}")

print(os.getcwd())
print(os.path.dirname(os.path.abspath("assign.py")))
print(os.path.basename(__file__))

all_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
print("Number of files in folder:", len(all_files))

# ================= Part 2: Append Text & File Stats =================

txt1_path = folder
with open(os.path.join(txt1_path, "txt1.txt"), "a") as file:
    file.write("\nAppended => Elzero Web School" * 50)

with open(os.path.join(txt1_path, "txt1.txt"), "r") as file:
    text = file.read()
    print(len(text.splitlines()))
    words = text.split()
    print(len(words))
    print(len(text))
    print(text.count("l"))

# ================= Part 3: Delete Last 10 Files =================

for i in range(41, 51):
    file_path = os.path.join(folder, f"txt{i}.txt")
    if os.path.exists(file_path):
        os.remove(file_path)

# Verify last file
remaining_files = sorted([f for f in os.listdir(folder) if f.endswith(".txt")])
print("Last file remaining:", remaining_files[-1])

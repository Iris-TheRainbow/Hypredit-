import os, glob
import sys

home = os.path.expanduser("~")
confpath = home +"/.config/hypredit"
conffile = confpath + "/hypredit.conf"

editor = ""
hyprconf = ""
if os.path.exists(conffile):
    with open(conffile, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.startswith("editor = "):
                editor = line.split(" ")[-1]
            if line.startswith("hyprconf = "):
                hyprconf = line.split(" ")[-1]
if editor == "": editor = "nano"
if hyprconf == "": hyprconf = home +"/.config/hypr"

files = os.listdir(hyprconf)
confs = []
for file in files:
    if file.endswith(".conf"):
        confs.append(file)
print(confs)

for i in range(len(confs)):
    string = "(" + str(i + 1) + "): " + confs[i]
    confs[i] = (i + 1, confs[i])
    print(string)

while True:
    file = input("Select a hypr conf file: ")
    target = ""
    brake = False
    for conf in confs:
        if int(conf[0]) == int(file):
            target = conf[1]
            break
        elif conf[1] == file:
            target = conf[1]
            break
        elif file == 0:
            brake = True
    if target == "": continue

    if brake:
        break

    os.system(editor + " " + hyprconf + "/" + target)
    break

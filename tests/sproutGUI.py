from appJar import gui
import qr_camera as camera
import sprout


def full_clear():
    app.clearAllTextAreas()


def clear_keys():
    app.clearTextArea("k1")
    app.clearTextArea("k2")
    app.clearTextArea("k3")


def split():
    clear_keys()
    raw_seed = app.getTextArea("main")
    split_seed = sprout.split_seed(raw_seed)

    # Data format is [shard1, shard2, shard3]
    # Each Shard is [wordlist, indexes, qr]

    # Data wrangling
    shards =[]
    i  = 0
    while i < 3:
        s = ' '.join(split_seed[i][0]) + "\n" + "\n" + split_seed[i][2]
        shards.append(s)
        i+=1

    # Update the GUI
    app.setTextArea("k1", shards[0])
    app.setTextArea("k2", shards[1])
    app.setTextArea("k3", shards[2])


def rejoin():
    # step one? what keys to we have?
    # text areas are empty, not none

    # Get the text areas
    k1 = app.getTextArea("k1")
    k2 = app.getTextArea("k2")
    k3 = app.getTextArea("k3")

    seed = ""
    if k1 == "" and k2 != "" and k3 != "":
        k2 = k2.split(" ")
        k3 = k3.split(" ")
        w = "twothree"
        seed = sprout.recover_seed(k2, k3, w)
    elif k2 == "" and k1 != "" and k3 != "":
        k1 = k1.split(" ")
        k3 = k3.split(" ")
        w = "onethree"
        seed = sprout.recover_seed(k1, k3, w)
    elif k3 == "" and k2 != "" and k1 != "":
        k1 = k1.split(" ")
        k2 = k2.split(" ")
        w = "onetwo"
        seed = sprout.recover_seed(k1, k2, w)
    else:
        app.warningBox("Error", "Invalid Key!")

    app.clearTextArea("main")
    app.setTextArea("main", seed)


def scan():
    qr = camera.qr_reader()
    if qr[0] == "1":
        app.setTextArea("k1", qr[1])
    elif qr[0] == "2":
        app.setTextArea("k2", qr[1])
    elif qr[0] == "3":
        app.setTextArea("k3", qr[1])
    else:
        app.warningBox("Invalid", "You've got an invalid key there, pal!")

# old colors: bg = gray || label, bg = purple, fg = gray
with gui("sproutGUI", "800x650", bg='#494850', font={'size': 18}) as app:
    app.label("sproutGUI", bg='#978897', fg='#2C2C34', row=0, colspan=4)
    app.label("Seed Phrase", row=1, colspan=4)
    app.addTextArea("main", row=2, colspan=4, rowspan=1)
    app.label("Key 1", row=3, column=0, colspan=1)
    app.addTextArea("k1", row=4, column=0, colspan=1)
    app.label("Key 2", row=3, column=1, colspan=1)
    app.addTextArea("k2", row=4, column=1, colspan=1, rowspan=0)
    app.label("Key 3", row=3, column=2, colspan=1)
    app.addTextArea("k3", row=4, column=2, colspan=1, rowspan=0)
    # app.buttons(["Submit", "Cancel"], [press, app.stop], colspan=4)
    app.buttons(["Split", "Join", "Scan", "Clear", "Quit"], [split, rejoin, scan, full_clear, app.stop], colspan=4)

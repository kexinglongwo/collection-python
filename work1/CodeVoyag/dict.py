old_dict = {
    101: "a",
    102: "b",
    103: "c",
    104: "d",
    105: "e",

}
new_dict = {id: old_dict[id] for id in old_dict if id % 2 != 0}
print(new_dict)
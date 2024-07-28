def list2string(changelist):
    if type(changelist) == list:
        return " ".join(map(str, changelist))
    else:
        return changelist

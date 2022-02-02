time = int(input("Time in seconds:"))
hh = int(time / 3600)
mm = int((time - 3600 * hh) / 60)
ss = time - hh * 3600 - mm * 60
if hh < 10:
    hh = str(0) + str(hh)
if mm < 10:
    mm = str(0) + str(mm)
if ss < 10:
    ss = str(0) + str(ss)
print(f"Time in format hh:mm:ss {hh}:{mm}:{ss}")



def rvrs_str(inpt_str):
  rvrs_str = ""
  for i in range(len(inpt_str) - 1, -1, -1):
    rvrs_str += inpt_str[i]
  return rvrs_str


inpt_str = input("Enter your str - ")


rslt = rvrs_str(inpt_str)

print(f"reversed str - {rslt}")



#str_get = list(input("Gimmi - "))

def len_len(str):
  len = 0 
  while True:
    try:
      str[len]
      len += 1
    except IndexError:
      break
  return len


def rvrs_str(inpt_str):
  rvrs_str = ""
  for i in range(len(inpt_str) - 1, -1, -1):
    rvrs_str += inpt_str[i]
  return rvrs_str


inpt_str = list(input("Enter your str - "))


rslt = rvrs_str(inpt_str)

print(f"reversed str - {rslt}")

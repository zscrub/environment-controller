from time import sleep

menu_options = {
        "Temp": {"SetTemp": 0, "SetFormat": "F"}, 
        "Humidity": 0.8,
        "Light": 0, 
        "Fan": 0
    }

# redundant
# p = 0
# l = list(menu_options.keys())
# M = len(l)-1

def menu_index():
    swrite("^", line=1, pos=8)
    swrite(">", 2, 3)
    swrite("v", 4, 8)



# print(menu_options)

# print(f"{l[p]}\n{l[p+1]}", end = "\r")

# while True: 
#     sleep(0.1)

#     if keyboard.is_pressed('w') and p>0: 
#         p-=1
#         # print(p)
#         try:
#             print(f"  > {l[p]}\n{l[p+1]}", end = "\r")
#         except IndexError:
#             print(f"    {l[p-1]}\n> {l[p]}", end = "\r")
            
#     if keyboard.is_pressed('s') and p<M: 
#         p+=1
#         # print(p)
#         try:
#             print(f"  > {l[p]}\n{l[p+1]}", end = "\r")
#         except IndexError:
#             print(f"    {l[p-1]}\n> {l[p]}", end = "\r")
            
from pwn import *

# 0x555555555b6e
key = ""
#testcase = "abcdefghijklmnopqrstuvwxyz"
testcase = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#0 2 52 53 54
#26 19 19 0 2
context.log_level = "critical"
'''
p = process(["gdb", "test"])
p.recvuntil("gef➤ ")
p.sendline("run")
p.recvuntil("Enter the password: ")
p.sendline("123")


a = p.recv()
a = a.decode("utf-8")
'''


found = 0
#print("Brute forcing...")
while(1):
	if found == 0:
		for l1 in range (0, len(testcase)):
			if found == 0:
				for l2 in range (0, len(testcase)):
					if found == 0:
						for l3 in range (0, len(testcase)):
							if found == 0:
								for l4 in range (0, len(testcase)):
									if found == 0:
										for l5 in range (0, len(testcase)):
											key = testcase[l1]+testcase[l2]+testcase[l3]+testcase[l4]+testcase[l5]
											p = process("./test")
											p.recvuntil("Enter the password: ")
											print("Trying: "+ key + ": ", end = "")
											p.sendline(key)

											a = p.recv()
											a = a.decode("utf-8")
											print(a)

											if("Wrong" not in a):
												print("Found: " + key)
												found = 1

												p.close()
												break

											p.close()

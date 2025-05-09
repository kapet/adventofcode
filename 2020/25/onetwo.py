
def transform(subject, loopsize):
    value = 1
    for i in range(loopsize):
        value = (value * subject) % 20201227
    return value

if False:
    pubkey1 = 17807724
    pubkey2 = 5764801
else:
    pubkey1 = 19241437
    pubkey2 = 17346587

value = 1
loops = 0
while value != pubkey1:
    value = (value * 7) % 20201227
    loops += 1
print('one', transform(pubkey2, loops))


import slides
from time import sleep

for slide in slides.slides:
    print('\033c')
    print("\u001b[34;1m")
    print(slide)
    sleep(1)
    print("\u001b[27A")

print('\033c')
print("THE END")
sleep(2)
print('\033c')
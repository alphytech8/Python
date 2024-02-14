while True:
    try:
        s1 = int(input("Enter marks for subject 1:"))
        s2 = int(input("Enter marks for subject 2:"))
        s3 = int(input("Enter marks for subject 3:"))
        if s1 > 100 or s2 > 100 or s3 > 100:
            print("Please enter marks below 100 for all subjects.")
            continue
        avg = (s1 + s2 + s3) / 3
        print("Average score:", avg)
        if avg >= 70 and avg <= 100:
            print("Your grade is A")
        elif avg >= 60 and avg <= 69:
            print("Your grade is B")
        elif avg >= 50 and avg <= 59:
            print("Your grade is C")
        elif avg >= 40 and avg <= 49:
            print("Your grade is D")
        elif avg >= 0 and avg <= 39:
            print("You have failed")
        else:
            print("Please enter valid integer marks between 0 and 100 for all subjects.")
    except ValueError:
        print("Please enter valid integer marks for all subjects.")

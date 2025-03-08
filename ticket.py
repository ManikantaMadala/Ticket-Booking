import qrcode
import os
import platform

def generate_qr_code(data, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

def show_image(filename='qrcode.png'):
    if platform.system() == "Darwin":       # macOS
        os.system(f"open {filename}")
    elif platform.system() == "Windows":    # Windows
        os.system(f"start {filename}")
    else:                                   # Linux
        os.system(f"xdg-open {filename}")

def movie():
    print("We have 3 Movies. Please Enter:\n")
    print("1 for Saripodha Saniraram\n2 for G.O.A.T\n3 for Raayan\n")
    
    while True:
        try:
            m = int(input("Enter Your Choice: "))
            if m == 1:
                M = "Saripodha Saniraram"
                break
            elif m == 2:
                M = "G.O.A.T"
                break
            elif m == 3:
                M = "Raayan"
                break
            else:
                print("Please Enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Select Any Theater (Type integer):")
    print("1 for Imax\n2 for Prasad\n")

    while True:
        try:
            the = int(input("Enter Your Choice: "))
            if the == 1:
                Theater = "Imax"
                s = 20
                break
            elif the == 2:
                Theater = "Prasad"
                s = 40
                break
            else:
                print("Please Enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    Time = ['8:00 AM', '12:00 PM', '5:00 PM']
    print(f"Theater: {Theater}\nMovie: {M}\nTime Movie is Available: {Time}\n")

    while True:
        try:
            ti = int(input("Which time you want to book (Type number only):\n1 for 8:00 AM\n2 for 12:00 PM\n3 for 5:00 PM\n"))
            if ti == 1:
                tim = '8:00 AM'
                break
            elif ti == 2:
                tim = '12:00 PM'
                break
            elif ti == 3:
                tim = '5:00 PM'
                break
            else:
                print("Invalid Time Choice.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nAvailable Seats: {s}\nHow Many Seats Do You Want to Buy?")
    
    while True:
        try:
            seat = int(input("Enter your choice: "))
            if seat <= s:
                break
            else:
                print("SORRY, Seats are not Enough!\nBOOKING FAILED\nExiting...")
                return
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\n\nTheater: {Theater}\nMovie: {M}\nTime: {tim}\nNumber of Seats: {seat}\n")

    while True:
        try:
            Conform = int(input("Confirm Above Data:\nType 1 for Yes\nType 2 for No\n"))
            if Conform == 1:
                print(f"Your Ticket is booked\nMake sure you reach {Theater} 10 mins before {tim}")
                break
            elif Conform == 2:
                print("Ticket Not Confirmed...")
                main()
                return
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def series():
    print("We have 4 Series. Please Enter:\n")
    print("1 for Gyarah Gyarah\n2 for Lucifer\n3 for Taaga Khabbar\n4 for One Piece (Anime)\n")

    while True:
        try:
            ser = int(input("Enter Your Choice: "))
            if ser == 1 or ser == 3:
                print("Series: Gyarah Gyarah and Taaga Khabbar are available on Hotstar")
                break
            elif ser == 2 or ser == 4:
                print("Series: Lucifer and One Piece are available on Netflix")
                break
            else:
                print("Please Enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print(".....BOOK YOUR TICKETS.....")
    print("Please Enter\n1 for Movies\n2 for Series\n")
    
    while True:
        try:
            t = int(input("Enter Your Choice: "))
            if t == 1:
                movie()
                break
            elif t == 2:
                series()
                break
            else:
                print("Please Enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(".....Thank you.....")
    
    # Generate QR code
    qr_data = "Thank you for booking! Visit our website: https://in.bookmyshow.com/"
    generate_qr_code(qr_data)

    # Show QR code image
    show_image()

main()


user = "Dipesh"
o_p = "DipeshDagar@123"


def pass_checker(n_p):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    if len(n_p) < 8:
        print("❌ Weak Password (minimum 8 characters required)")
        return False

    for ch in n_p:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        print("❌ Password must include Upper, Lower, Digit & Special char")
        return False


# -------- MAIN LOOP --------
while True:
    u = input("\nUser: ")
    p = input("Pass: ")

    if user == u and o_p == p:
        print("\nOptions:")
        print("1. Change Password")
        print("2. Logout")

        x = int(input("Enter Your Option: "))

        if x == 1:
            n_p = input("New Password: ")

            if n_p == o_p:
                print("❌ New password cannot be same as old password")

            elif pass_checker(n_p):
                y = input("Confirm Password: ")
                if n_p == y:
                    o_p = n_p
                    print("✅ Password changed successfully")
                else:
                    print("❌ Password mismatch")

        elif x == 2:
            print("🔒 Logged out successfully")

        else:
            print("❌ Invalid option")

    else:
        print("❌ Invalid username or password")

    again = input("\nDo you want to login again? (y/n): ").lower()
    if again != "y":
        print("👋 Program Ended")
        break

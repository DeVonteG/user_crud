import requests

URL= "http://127.0.0.1:5000/users"


def update_user(id, first_name, last_name, hobbies):
    user= {
        "first_name": first_name,
        "last_name": last_name,
        "hobbies": hobbies
    }
    url= URL+"/"+id
    response = requests.put(url, json=user)
    if  response.status_code == 204:
        print (
            "Successfully updated record; Got %s"
        )
    else:
        print(
            "Something went wrong while updating record"
        )

if __name__ =="__main__":
    uid= input("Type in the user's id: ")
    fname = input("Type in the user's first name: ")
    lname = input("Type in the user's last name: ")
    hobbies = input("Type in the user's hobbies: ")
    update_user(uid, fname, lname, hobbies)
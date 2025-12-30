import requests

def fetch_data_from_api():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response= requests.get(url)
    # print(response.status_code)
    # print(response.text)
    # print(response.json())

    data= response.json()
    if data["success"] and "data" in data:
        userdata= data["data"]
        username= userdata["login"]["username"]
        country=userdata["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch data")

def main():
    try:
        username, country= fetch_data_from_api()
        print(f"Username= {username} Country= {country}")
    
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

from datetime import date, datetime,timedelta

def get_birthdays_per_week(users: list()):
    if len(users) > 0:
        output_result = {"Monday":[], 
        "Tuesday":[],
        "Wednesday":[],
        "Thursday":[],
        "Friday":[],}
        start_date = date.today() 
        end_date = start_date + timedelta(days=6)  
        for user in users:
            if end_date.year > start_date.year and user['birthday'].month == 1: 
                user_birthday = datetime(year=end_date.year,month=user['birthday'].month,day=user['birthday'].day).date()    
            else:
                user_birthday = datetime(year=start_date.year,month=user['birthday'].month,day=user['birthday'].day).date()
            if start_date <= user_birthday <=  end_date:
                if user_birthday.strftime('%A') in output_result:
                    output_result[user_birthday.strftime('%A')].append(user['name'])
                else:
                    output_result['Monday'].append(user['name'])    
        delete_key = [key for key,value in output_result.items() if not value]
        for key in delete_key:
            del output_result[key]
        return output_result
    else:
        return{}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

raw_phones = [
 {"phone_code": "P301", "brand": "apple", "price": 25000000, "status": "available"},
 {"phone_code": " p101 ", "brand": "samsung", "price": 12000000, "status": "available"},
 {"phone_code": "Po02", "brand": "xiaomi", "price": 8000000, "status": "sold"},
 {"phone_code": "P102", "brand": "samsung", "price": 9500000, "status": "reserved"},
 {"phone_code": "P302", "brand": "apple", "price": 28000000, "status": "available"}
]

def  clean_and_validate_phone(raw_phones):
    validate_phone = raw_phones.copy()
    for r_p in validate_phone :
        r_p['phone_code'] = r_p['phone_code'].strip().upper()
        if not r_p['phone_code'].startswith('P') or not r_p['phone_code'][1].isdigit() :
            validate_phone.remove(r_p) 
    return validate_phone

check =clean_and_validate_phone(raw_phones)
print(check)
    
    
def search_phones(raw_phones, value_price: float,status: str = None):
    result =[]
    for r_p in raw_phones :
        if status is None :
            if r_p['price'] <= value_price :
                result.append(r_p)
        else :
            if r_p['price'] <= value_price and r_p['status'] :
                result.append(r_p)
    return result
result = search_phones(raw_phones,9000000,'sold')   
print(result)  

def  sort_phones_by_price_desc(raw_phones):
    phones = raw_phones.copy()
    i =0 
    for phone in phones:
        if phone[i]['price'] > phone[i +1]['price']:
            phone[i], phone[i] = phone[i +1],phone[i +1]
        i+= i
    return phones

result_sort = sort_phones_by_price_desc(raw_phones)
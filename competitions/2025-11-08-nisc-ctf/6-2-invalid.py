from enum import Enum
from typing import List, Dict
from datetime import datetime

import re
import csv

user_roles : Dict[int, str] = {}
user_names : Dict[int, str] = {}

invalid : List[List[str]] = [["姓名", "违规类型"]]

class InvalidType(Enum) :
    INFO = "信息违规"
    OPERATIONS = "操作违规"

TABLES_CSR = ["user_management", "order_management"]
TABLES_FS  = ["order_management"]
TABLES_PM  = ["product_management"]
TABLES_SA  = ["system_logs"]

def check_name_valid(name : str) -> bool :
    return re.fullmatch(r"[\u4e00-\u9fa5]{2,4}", name) is not None

def check_phone_valid(phone : str) -> bool :
    if phone[0] != "1" :
        return False
    elif re.fullmatch(r"[3-9]{1}", phone[1]) is None :
        return False
    return re.fullmatch(r"[0-9]{11}", phone) is not None

def check_id_valid(id : str) -> bool :
    if re.fullmatch(r"\d{17}[0-9Xx]$", id) is None :
        return False
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    table  = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    sum = 0
    for i in range(0, 17) :
        sum += int(id[i]) * weight[i]
    if table[sum % 11].lower() != id[-1].lower() :
        return False
    return True

def check_bank_id_valid(bank_id : str) -> bool :
    if re.fullmatch(r"\d{16,19}", bank_id) is None :
        return False
    index = 1
    sum = 0
    for i in range(len(bank_id) - 1, -1, -1) :
        if index % 2 == 0 :
            if int(bank_id[i]) * 2 > 9 :
                sum += int(bank_id[i]) * 2 - 9
            else :
                sum += int(bank_id[i]) * 2
        else :
            sum += int(bank_id[i])
        index += 1
    return sum % 10 == 0

def check_date_valid(date : str, id : str) -> bool :
    try :
        date_object  = datetime.strptime(date, "%Y/%m/%d")
        start_object = datetime.strptime("2015/1/1", "%Y/%m/%d")
        end_object   = datetime.strptime("2025/10/31", "%Y/%m/%d")
        if not start_object <= date_object <= end_object :
            return False
        id_date = id[6:10] + "/" + id[10:12] + "/" + id[12:14]
        id_date_object = datetime.strptime(id_date, "%Y/%m/%d")
        if not id_date_object <= date_object :
            return False
        return True

    except ValueError :
        return False

def check_users_valid() -> None :
    with open("./data.sql", "r", encoding = "utf-8") as sql :
        for line in sql.readlines() :
            if "INSERT INTO `users`" in line :
                info_raw = line.replace("INSERT INTO `users` VALUES (", "").replace(");", "")
                info : List[str] = list(map(
                    lambda s : s.replace("\'", "").replace("\n", "").replace(" ", ""),
                    info_raw.split(","))
                )
                user_roles[int(info[0])] = info[-1]
                user_names[int(info[0])] = info[1]
                if not check_name_valid(info[1]) :
                    invalid.append([info[1], InvalidType.INFO.value])
                    continue
                if not check_phone_valid(info[2]) :
                    invalid.append([info[1], InvalidType.INFO.value])
                    continue
                if not check_id_valid(info[3]) :
                    invalid.append([info[1], InvalidType.INFO.value])
                    continue
                if not check_bank_id_valid(info[4]) :
                    invalid.append([info[1], InvalidType.INFO.value])
                    continue
                if not check_date_valid(info[5], info[3]) :
                    invalid.append([info[1], InvalidType.INFO.value])
                    continue

def check_operations_valid() -> None :
    with open("./data.sql", "r", encoding = "utf-8") as sql :
        for line in sql.readlines() :
            if "INSERT INTO `operations`" in line :
                info_raw = line.replace("INSERT INTO `operations` VALUES (", "").replace(");", "")
                info : List[str] = list(map(
                    lambda s : s.replace("\'", "").replace("\n", "").replace(" ", ""),
                    info_raw.split(",")
                ))
                print(info)
                try :
                    if user_roles[int(info[1])] == "客服" and info[3] not in TABLES_CSR :
                        invalid.append([user_names[int(info[1])], InvalidType.OPERATIONS.value])
                    if user_roles[int(info[1])] == "财务" and info[3] not in TABLES_FS :
                        invalid.append([user_names[int(info[1])], InvalidType.OPERATIONS.value])
                    if user_roles[int(info[1])] == "商品经理" and info[3] not in TABLES_PM :
                        invalid.append([user_names[int(info[1])], InvalidType.OPERATIONS.value])
                    if user_roles[int(info[1])] == "系统审计员" and info[3] not in TABLES_SA :
                        invalid.append([user_names[int(info[1])], InvalidType.OPERATIONS.value])
                except KeyError :
                    continue

check_users_valid()
check_operations_valid()
invalid_filtered = [list(x) for x in set(tuple(x) for x in invalid)]

with open("./output-invalid.csv", "w", encoding = "utf-8") as file :
    writer = csv.writer(file)
    writer.writerows(invalid_filtered)

# flag is DASCTF{50503382802106599405693745879513}

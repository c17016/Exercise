# 専門学校ITカレッジ沖縄　ゲームクリエイター科
# 長嶺　由也
def check(any_num, start_num, end_num):
    if start_num == end_num:
        if start_num == any_num:            
            return "含む"
        else:          
            return "含まない"

    elif start_num > end_num:
        if start_num <= any_num <= 23 or 0 <= any_num < end_num:            
            return "含む"
        else:            
            return "含まない"
            
    else:
        if start_num <= any_num < end_num:           
            return "含む"
        else:           
            return "含まない"

if  __name__ == "__main__":    
    while True:
        print("0 ~ 23 の範囲から時刻を入力して下さい。\nある時刻：", end = "")
        any_num = int(input())
        
        if 0 <= any_num <= 23:
            break 
        else:
            continue

    while True:
        print("開始時刻と終了時刻を入力して下さい。\n開始時刻：", end = "")
        # 開始時刻
        start_num = int(input())        
        print("終了時刻：", end = "")
        # 終了時刻
        end_num = int(input())

        if 0 <= start_num <= 23 and 0 <= end_num <= 23:
            break
        else:
            continue

    print(check(any_num, start_num, end_num))    
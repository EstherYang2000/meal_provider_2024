import json


def modify_menu_item(restaurant_id, restaurant_file, json_data, mapping_data):
    # 讀取 restaurant file
    with open(restaurant_file, "r") as f:
        restaurant_data = json.load(f)
    # 根據 restaurant_id 取得對應的 restaurant name
    restaurant_name = ""
    for restaurant in restaurant_data:
        if restaurant["restaurant_id"] == restaurant_id:
            restaurant_name = restaurant["name"]
            break
    print(restaurant_name)
    if restaurant_name is None:
        print("Error: Restaurant ID not found.")
        return
    menu_value_list = mapping_data[restaurant_name]
    print(menu_value_list)
    # 根據 restaurant name 取得對應的 JSON key
    for index, item in enumerate(json_data):
        if item["restaurant_id"] == restaurant_id:
            index_10 = index % 10
            item["item_name"] = menu_value_list[index_10]
    print(json_data)
    return json_data


mapping_data = {
    "八方雲集": [
        "滷肉飯",
        "蚵仔煎",
        "牛肉麵",
        "大腸麵線",
        "鹹酥雞",
        "豆花",
        "豬血糕",
        "臭豆腐",
        "蔥油餅",
        "燒餅油條",
        "肉圓",
        "碗粿",
        "甜不辣",
        "刈包",
        "米糕",
        "麻辣臭豆腐",
        "筒仔米糕",
        "鹽水雞",
        "芋頭鴨",
        "鳳梨酥",
    ],
    "正忠排骨飯": [
        "排骨飯",
        "雞腿飯",
        "控肉飯",
        "酸菜白肉鍋",
        "豬腳麵線",
        "花生湯",
        "蚵仔煎",
        "油條豆漿",
        "燒賣",
        "蒸餃",
        "筍干炒肉絲",
        "魚丸湯",
        "米粉湯",
        "燙青菜",
        "麻辣鍋",
        "紅豆湯",
        "牛肉湯餃",
        "涼拌小黃瓜",
        "豬肝湯",
        "花生糕",
    ],
    "永和豆漿": [
        "鹹豆漿",
        "甜豆漿",
        "油條",
        "蔥花餅",
        "蘿蔔糕",
        "燒餅",
        "飯糰",
        "豆花",
        "韭菜盒子",
        "芝麻球",
        "蛋餅",
        "饅頭",
        "湯圓",
        "包子",
        "豆漿冰",
        "鍋貼",
        "薄餅",
        "豆皮",
        "小籠包",
        "炒米粉",
    ],
    "雙月食品社": [
        "肉燥飯",
        "蒸餃",
        "麻婆豆腐",
        "蛋撻",
        "炒飯",
        "煎餃",
        "臭豆腐",
        "筍干牛肉",
        "三杯雞",
        "豆花",
        "脆皮雞腿",
        "火鍋",
        "海鮮湯",
        "牛肉麵",
        "魚丸湯",
        "排骨飯",
        "炸鱔魚",
        "糖葫蘆",
        "地瓜球",
        "花生冰",
    ],
    "鼎泰豐": [
        "小籠包",
        "蝦餃",
        "煎堆",
        "牛肉捲餅",
        "紅油炒手",
        "綠豆湯",
        "豆沙包",
        "燒賣",
        "鹽酥雞",
        "豆花",
        "炒米粉",
        "炒麵",
        "炸豆腐",
        "粉絲煲",
        "蒸蛋",
        "牛肉面",
        "湯包",
        "蘿蔔糕",
        "芋圓",
        "豆漿",
    ],
    "段純貞牛肉麵餐廳": [
        "牛肉麵",
        "酸菜牛肉麵",
        "炸醬麵",
        "牛肉湯餃",
        "牛肉捲餅",
        "涼拌牛肉",
        "牛肉炒飯",
        "燙牛肉",
        "牛肉串",
        "牛肉鍋貼",
        "麻辣牛肉",
        "酸辣湯",
        "牛肉粉絲湯",
        "紅燒牛肉",
        "麻辣熱炒",
        "牛腩煲",
        "牛肉丸子湯",
        "牛肉燉豆腐",
        "牛肉燉白菜",
        "牛肉酥",
    ],
    "四海遊龍": [
        "魚翅湯",
        "海參",
        "燒白",
        "蝦仁炒飯",
        "烤魚",
        "鮑魚",
        "龍蝦湯",
        "魚丸湯",
        "海鮮炒麵",
        "海鮮粥",
        "貝殼湯",
        "魚片粥",
        "鹽燒海鮮",
        "蒜蓉蒸蝦",
        "海參炒肉",
        "墨魚炒飯",
        "烤魷魚",
        "海鮮豆腐",
        "海鮮春卷",
        "海鮮火鍋",
    ],
    "壽司郎": [
        "壽司拼盤",
        "海膽壽司",
        "鮪魚壽司",
        "三文魚壽司",
        "蟹肉壽司",
        "章魚壽司",
        "鰻魚壽司",
        "烤魚壽司",
        "黃瓜卷",
        "花枝卷",
        "鮭魚皮壽司",
        "牛肉壽司",
        "煙燻鮭魚壽司",
        "飛魚卵壽司",
        "鰻魚腹壽司",
        "蝦卵壽司",
        "烤牛舌壽司",
        "炙燒鮭魚壽司",
        "牡蠣壽司",
        "魚籽壽司",
    ],
    "鳥貴族": [
        "燒鳥拼盤",
        "雞肉串",
        "雞翅串",
        "雞腿串",
        "雞心串",
        "雞肝串",
        "雞軟骨串",
        "雞皮串",
        "鴨肉串",
        "鴨舌串",
        "鴨肝串",
        "鴨腿串",
        "鴨翅串",
        "雞蛋燒",
        "豬肉串",
        "牛肉串",
        "牛舌串",
        "羊肉串",
        "魚肉串",
        "蔬菜串",
    ],
    "吉野家": [
        "牛丼",
        "雞肉丼",
        "豬排丼",
        "鮭魚丼",
        "蝦丼",
        "海鮮丼",
        "烤肉丼",
        "炒牛肉丼",
        "炒豬肉丼",
        "炒雞肉丼",
        "烤魚丼",
        "烤雞丼",
        "炸豬排丼",
        "炸雞丼",
        "炸蝦丼",
        "素食丼",
        "蔬菜丼",
        "章魚丼",
        "花枝丼",
        "牛肉湯丼",
    ],
    "燒肉Smile": [
        "燒肉拼盤",
        "豬肉燒肉",
        "牛肉燒肉",
        "雞肉燒肉",
        "鴨肉燒肉",
        "羊肉燒肉",
        "海鮮燒肉",
        "蔬菜燒肉",
        "烤豬排",
        "烤牛排",
        "烤雞排",
        "烤鴨排",
        "烤羊排",
        "烤魚",
        "烤蝦",
        "烤章魚",
        "烤蔬菜",
        "烤豆腐",
        "烤香腸",
        "烤花枝",
    ],
    "森森燒肉": [
        "燒肉拼盤",
        "豬肉燒肉",
        "牛肉燒肉",
        "雞肉燒肉",
        "鴨肉燒肉",
        "羊肉燒肉",
        "海鮮燒肉",
        "蔬菜燒肉",
        "烤豬排",
        "烤牛排",
        "烤雞排",
        "烤鴨排",
        "烤羊排",
        "烤魚",
        "烤蝦",
        "烤章魚",
        "烤蔬菜",
        "烤豆腐",
        "烤香腸",
        "烤花枝",
    ],
    "春水堂人文茶館": [
        "奶茶",
        "紅茶",
        "綠茶",
        "烏龍茶",
        "花茶",
        "果茶",
        "冷泡茶",
        "蜂蜜檸檬茶",
        "珍珠奶茶",
        "椰果奶茶",
        "芒果茶",
        "草莓茶",
        "蘋果茶",
        "桃子茶",
        "檸檬茶",
        "橙子茶",
        "葡萄茶",
        "奇異果茶",
        "梅子茶",
        "藍莓茶",
    ],
    "翰林茶館": [
        "奶茶",
        "紅茶",
        "綠茶",
        "烏龍茶",
        "花茶",
        "果茶",
        "冷泡茶",
        "蜂蜜檸檬茶",
        "珍珠奶茶",
        "椰果奶茶",
        "芒果茶",
        "草莓茶",
        "蘋果茶",
        "桃子茶",
        "檸檬茶",
        "橙子茶",
        "葡萄茶",
        "奇異果茶",
        "梅子茶",
        "藍莓茶",
    ],
    "天仁茶業": [
        "奶茶",
        "紅茶",
        "綠茶",
        "烏龍茶",
        "花茶",
        "果茶",
        "冷泡茶",
        "蜂蜜檸檬茶",
        "珍珠奶茶",
        "椰果奶茶",
        "芒果茶",
        "草莓茶",
        "蘋果茶",
        "桃子茶",
        "檸檬茶",
        "橙子茶",
        "葡萄茶",
        "奇異果茶",
        "梅子茶",
        "藍莓茶",
    ],
    "五十嵐": [
        "奶茶",
        "紅茶",
        "綠茶",
        "烏龍茶",
        "花茶",
        "果茶",
        "冷泡茶",
        "蜂蜜檸檬茶",
        "珍珠奶茶",
        "椰果奶茶",
        "芒果茶",
        "草莓茶",
        "蘋果茶",
        "桃子茶",
        "檸檬茶",
        "橙子茶",
        "葡萄茶",
        "奇異果茶",
        "梅子茶",
        "藍莓茶",
    ],
    "南海茶道": [
        "奶茶",
        "紅茶",
        "綠茶",
        "烏龍茶",
        "花茶",
        "果茶",
        "冷泡茶",
        "蜂蜜檸檬茶",
        "珍珠奶茶",
        "椰果奶茶",
        "芒果茶",
        "草莓茶",
        "蘋果茶",
        "桃子茶",
        "檸檬茶",
        "橙子茶",
        "葡萄茶",
        "奇異果茶",
        "梅子茶",
        "藍莓茶",
    ],
    "八曜和茶": [
        "奶茶",
        "紅茶",
        "綠茶",
        "烏龍茶",
        "花茶",
        "果茶",
        "冷泡茶",
        "蜂蜜檸檬茶",
        "珍珠奶茶",
        "椰果奶茶",
        "芒果茶",
        "草莓茶",
        "蘋果茶",
        "桃子茶",
        "檸檬茶",
        "橙子茶",
        "葡萄茶",
        "奇異果茶",
        "梅子茶",
        "藍莓茶",
    ],
    "大茗": [
        "奶茶",
        "紅茶",
        "綠茶",
        "烏龍茶",
        "花茶",
        "果茶",
        "冷泡茶",
        "蜂蜜檸檬茶",
        "珍珠奶茶",
        "椰果奶茶",
        "芒果茶",
        "草莓茶",
        "蘋果茶",
        "桃子茶",
        "檸檬茶",
        "橙子茶",
        "葡萄茶",
        "奇異果茶",
        "梅子茶",
        "藍莓茶",
    ],
    "Cold Stone": [
        "巧克力冰淇淋",
        "香草冰淇淋",
        "草莓冰淇淋",
        "抹茶冰淇淋",
        "芒果冰淇淋",
        "榴蓮冰淇淋",
        "紅豆冰淇淋",
        "奶酪冰淇淋",
        "薄荷巧克力冰淇淋",
        "焦糖海鹽冰淇淋",
        "檸檬薄荷冰淇淋",
        "香蕉巧克力冰淇淋",
        "椰子冰淇淋",
        "花生冰淇淋",
        "酒漬櫻桃冰淇淋",
        "覆盆子冰淇淋",
        "水melon冰淇淋",
        "橙子冰淇淋",
        "黑莓冰淇淋",
        "咖啡冰淇淋",
    ],
    "鮮芋仙": [
        "芋圓",
        "芋頭奶茶",
        "芋頭冰",
        "芋圓湯",
        "芋頭牛奶冰",
        "芋頭糕",
        "芋圓牛奶湯",
        "芋圓紅豆湯",
        "芋圓芒果湯",
        "芋頭粥",
        "芋頭包",
        "芋頭蒸糕",
        "芋圓綠豆湯",
        "芋圓椰奶湯",
        "芋頭燒",
        "芋圓粉圓冰",
        "芋圓珍珠奶茶",
        "芋頭酥",
        "芋頭泡芙",
        "芋圓黑糖冰",
    ],
    "糕糕在尚": [
        "蛋糕",
        "戚風蛋糕",
        "乳酪蛋糕",
        "瑪芬蛋糕",
        "布朗尼",
        "磅蛋糕",
        "戚風杯子蛋糕",
        "核桃蛋糕",
        "檸檬蛋糕",
        "椰子蛋糕",
        "提拉米蘇",
        "草莓蛋糕",
        "抹茶蛋糕",
        "巧克力蛋糕",
        "香蕉蛋糕",
        "蘋果蛋糕",
        "芒果蛋糕",
        "黑森林蛋糕",
        "橙子蛋糕",
        "香草蛋糕",
    ],
    "港城豆花": [
        "豆花",
        "芋圓豆花",
        "紅豆豆花",
        "綠豆豆花",
        "花生豆花",
        "珍珠豆花",
        "椰果豆花",
        "芒果豆花",
        "椰奶豆花",
        "抹茶豆花",
        "黑糖豆花",
        "鳳梨豆花",
        "巧克力豆花",
        "草莓豆花",
        "榴蓮豆花",
        "桂花豆花",
        "冬瓜豆花",
        "牛奶豆花",
        "芝麻豆花",
        "酒醉豆花",
    ],
    "美而美": [
        "蛋餅",
        "三明治",
        "燒餅油條",
        "豆漿",
        "漢堡",
        "煎餅果子",
        "蔥花餅",
        "肉鬆餅",
        "蛋撻",
        "紅豆餅",
        "燕麥粥",
        "玉米粥",
        "肉包",
        "蔬菜包",
        "糖餅",
        "奶茶",
        "鹹豆漿",
        "甜豆漿",
        "蘿蔔糕",
        "芋頭糕",
    ],
    "城市漢堡": [
        "漢堡",
        "雞肉漢堡",
        "豬肉漢堡",
        "牛肉漢堡",
        "蘑菇漢堡",
        "鮪魚漢堡",
        "素食漢堡",
        "三明治",
        "熱狗",
        "薯條",
        "洋蔥圈",
        "沙拉",
        "雞塊",
        "蘋果派",
        "可樂",
        "冰茶",
        "咖啡",
        "奶昔",
        "冰淇淋",
        "果汁",
    ],
    "早安美芝城": [
        "三明治",
        "蛋餅",
        "熱狗",
        "漢堡",
        "蛋撻",
        "燒餅油條",
        "豆漿",
        "紅茶",
        "綠茶",
        "咖啡",
        "牛奶",
        "玉米濃湯",
        "煎餅果子",
        "肉包",
        "蔬菜包",
        "饅頭",
        "糖餅",
        "奶茶",
        "鹹豆漿",
        "甜豆漿",
    ],
    "麥當勞": [
        "巨無霸",
        "雞塊",
        "薯條",
        "漢堡包",
        "蘋果派",
        "奶昔",
        "冰淇淋",
        "麥香魚",
        "麥香雞",
        "大麥克",
        "麥脆雞",
        "麥樂雞",
        "麥克雞塊",
        "咖啡",
        "紅茶",
        "綠茶",
        "可樂",
        "冰茶",
        "果汁",
        "雞肉卷",
    ],
    "肯德基": [
        "炸雞",
        "薯條",
        "漢堡",
        "雞腿堡",
        "熱狗",
        "三明治",
        "蛋撻",
        "沙拉",
        "玉米濃湯",
        "飯盒",
        "雞翅",
        "雞塊",
        "雞腿",
        "可樂",
        "咖啡",
        "紅茶",
        "綠茶",
        "奶茶",
        "奶昔",
        "冰淇淋",
    ],
    "丹丹漢堡": [
        "漢堡",
        "雞塊",
        "薯條",
        "雞腿堡",
        "熱狗",
        "三明治",
        "沙拉",
        "玉米濃湯",
        "飯盒",
        "雞翅",
        "雞塊",
        "雞腿",
        "可樂",
        "咖啡",
        "紅茶",
        "綠茶",
        "奶茶",
        "奶昔",
        "冰淇淋",
        "果汁",
    ],
    "Shake Shack": [
        "漢堡",
        "雞塊",
        "薯條",
        "雞腿堡",
        "熱狗",
        "三明治",
        "沙拉",
        "玉米濃湯",
        "飯盒",
        "雞翅",
        "雞塊",
        "雞腿",
        "可樂",
        "咖啡",
        "紅茶",
        "綠茶",
        "奶茶",
        "奶昔",
        "冰淇淋",
        "果汁",
    ],
    "Subway": [
        "三明治",
        "沙拉",
        "餅乾",
        "熱狗",
        "薯條",
        "漢堡",
        "雞塊",
        "可樂",
        "咖啡",
        "紅茶",
        "綠茶",
        "奶茶",
        "奶昔",
        "冰淇淋",
        "果汁",
        "雞腿堡",
        "飯盒",
        "雞翅",
        "雞腿",
        "三明治",
    ],
    "拉亞漢堡": [
        "漢堡",
        "雞塊",
        "薯條",
        "雞腿堡",
        "熱狗",
        "三明治",
        "沙拉",
        "玉米濃湯",
        "飯盒",
        "雞翅",
        "雞塊",
        "雞腿",
        "可樂",
        "咖啡",
        "紅茶",
        "綠茶",
        "奶茶",
        "奶昔",
        "冰淇淋",
        "果汁",
    ],
    "教父牛排": [
        "牛排",
        "豬排",
        "雞排",
        "鴨排",
        "羊排",
        "海鮮燒烤",
        "蔬菜燒烤",
        "薯條",
        "沙拉",
        "湯品",
        "麵包",
        "奶昔",
        "冰淇淋",
        "可樂",
        "咖啡",
        "紅茶",
        "綠茶",
        "奶茶",
        "果汁",
        "烤蔬菜",
    ],
    "西提牛排": [
        "牛排",
        "豬排",
        "雞排",
        "鴨排",
        "羊排",
        "海鮮燒烤",
        "蔬菜燒烤",
        "薯條",
        "沙拉",
        "湯品",
        "麵包",
        "奶昔",
        "冰淇淋",
        "可樂",
        "咖啡",
        "紅茶",
        "綠茶",
        "奶茶",
        "果汁",
        "烤蔬菜",
    ],
    "石二鍋": [
        "火鍋",
        "麻辣火鍋",
        "海鮮火鍋",
        "牛肉火鍋",
        "豬肉火鍋",
        "雞肉火鍋",
        "羊肉火鍋",
        "蔬菜火鍋",
        "湯底選擇",
        "餃子",
        "肉丸",
        "豆腐",
        "蔬菜盤",
        "海鮮盤",
        "牛肉盤",
        "豬肉盤",
        "雞肉盤",
        "羊肉盤",
        "米飯",
        "麵條",
    ],
    "涮乃葉": [
        "火鍋",
        "麻辣火鍋",
        "海鮮火鍋",
        "牛肉火鍋",
        "豬肉火鍋",
        "雞肉火鍋",
        "羊肉火鍋",
        "蔬菜火鍋",
        "湯底選擇",
        "餃子",
        "肉丸",
        "豆腐",
        "蔬菜盤",
        "海鮮盤",
        "牛肉盤",
        "豬肉盤",
        "雞肉盤",
        "羊肉盤",
        "米飯",
        "麵條",
    ],
    "Miss Energy 能量小姐": [
        "沙拉",
        "三明治",
        "蔬菜汁",
        "果汁",
        "能量棒",
        "蛋白質飲料",
        "低糖餐盒",
        "無麩質餐盒",
        "素食餐盒",
        "低卡餐盒",
        "豆腐沙拉",
        "雞胸肉沙拉",
        "烤魚沙拉",
        "烤雞沙拉",
        "烤豬肉沙拉",
        "烤牛肉沙拉",
        "蔬菜三明治",
        "雞肉三明治",
        "豬肉三明治",
        "牛肉三明治",
    ],
    "Poke Go 波奇走走": [
        "波奇沙拉",
        "鮭魚波奇",
        "雞肉波奇",
        "豬肉波奇",
        "牛肉波奇",
        "蔬菜波奇",
        "海鮮波奇",
        "烤魚波奇",
        "烤雞波奇",
        "烤豬肉波奇",
        "烤牛肉波奇",
        "水果波奇",
        "果汁",
        "蔬菜汁",
        "能量棒",
        "蛋白質飲料",
        "低糖餐盒",
        "無麩質餐盒",
        "素食餐盒",
        "低卡餐盒",
    ],
    "Lady M New York": [
        "千層蛋糕",
        "草莓千層蛋糕",
        "巧克力千層蛋糕",
        "檸檬千層蛋糕",
        "抹茶千層蛋糕",
        "芒果千層蛋糕",
        "提拉米蘇",
        "紅絲絨蛋糕",
        "檸檬蛋糕",
        "香蕉蛋糕",
        "芝麻蛋糕",
        "芋頭蛋糕",
        "巧克力蛋糕",
        "草莓蛋糕",
        "櫻桃蛋糕",
        "椰子蛋糕",
        "杏仁蛋糕",
        "核桃蛋糕",
        "咖啡蛋糕",
        "香草蛋糕",
    ],
    "Patisserie Parola": [
        "法式馬卡龍",
        "提拉米蘇",
        "檸檬塔",
        "草莓蛋糕",
        "巧克力蛋糕",
        "芝麻蛋糕",
        "芋頭蛋糕",
        "抹茶蛋糕",
        "藍莓蛋糕",
        "紅絲絨蛋糕",
        "椰子蛋糕",
        "杏仁蛋糕",
        "核桃蛋糕",
        "咖啡蛋糕",
        "香草蛋糕",
        "檸檬蛋糕",
        "櫻桃蛋糕",
        "芒果蛋糕",
        "香橙蛋糕",
        "巧克力慕斯蛋糕",
    ],
}
# Example usage:
restaurant_file = "database/data/restaurants.json"
menu_item = "database/data/final_corrected_completely_updated_menu_items.json"
with open(menu_item, "r") as f:
    menu_item_data = json.load(f)
modified_json_data = None
for i in range(6, 41):
    if i < 10:
        restaurant_id = f"restaurant00{i}"
    else:
        restaurant_id = f"restaurant0{i}"

    modified_json_data = modify_menu_item(
        restaurant_id, restaurant_file, menu_item_data, mapping_data
    )

output_file = f"database/data/modified_menu_items.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(modified_json_data, f, indent=4, ensure_ascii=False)
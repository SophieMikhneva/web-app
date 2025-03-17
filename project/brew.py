import requests # библиотека для API запросов
key = 'c219b14b-3858-49c3-b674-05efd8b6175b' #наш ключ с API Яндекс.Расписаний

#Создадим словарь со всеми городами России

url = f'https://api.rasp.yandex.net/v3.0/stations_list/?apikey={key}&lang=ru_RU&format=json' #Выдаёт все доступные станции
response = requests.get(url)
if response.status_code == 200:
    station = response.json()


def extract_russian_cities(data):
    russian_cities = {}

    # Перебираем все страны
    for country in data['countries']:
        if country['title'] == 'Россия':
            # Перебираем регионы России
            for region in country['regions']:
                # Перебираем населенные пункты в регионе
                for settlement in region['settlements']:
                    # Собираем информацию о городе
                    city_info = {
                        'title': settlement['title'],
                        'yandex_code': settlement['codes'].get('yandex_code', ''),
                        'stations': []
                    }

                    # Собираем информацию о станциях
                    for station in settlement['stations']:
                        station_info = {
                            'title': station['title'],
                            'yandex_code': station['codes'].get('yandex_code', ''),
                            'station_type': station['station_type'],
                            'transport_type': station['transport_type'],
                            'coordinates': {
                                'latitude': station['latitude'],
                                'longitude': station['longitude']
                            }
                        }
                        if 'direction' in station:
                            station_info['direction'] = station['direction']

                        city_info['stations'].append(station_info)

                    russian_cities[city_info['title']] = [city_info['yandex_code'], city_info['stations']]
            break  # Выходим после обработки России

    return russian_cities

# Пример использования
russian_cities = extract_russian_cities(station)
#Найдем большие города, через которые будет интересно делать пересадки
big_towns = {'Калининград': 'c22',
 'Мурманск': 'c23',
 'Петрозаводск': 'c18',
 'Санкт-Петербург': 'c2',
 'Псков': 'c25',
 'Великие Луки': 'c10928',
 'Великий Новгород': 'c24',
 'Тверь': 'c14',
 'Смоленск': 'c12',
 'Брянск': 'c191',
 'Калуга': 'c6',
 'Обнинск': 'c967',
 'Курск': 'c8',
 'Орёл': 'c10',
 'Тула': 'c15',
 'Москва': 'c213',
 'Долгопрудный': 'c214',
 'Дубна': 'c215',
 'Зеленоград': 'c216',
 'Пущино': 'c217',
 'Белгород': 'c4',
 'Липецк': 'c9',
 'Ярославль': 'c16',
 'Владимир': 'c192',
 'Александров': 'c10656',
 'Гусь-Хрустальный': 'c10661',
 'Муром': 'c10668',
 'Иваново': 'c5',
 'Рязань': 'c11',
 'Тамбов': 'c13',
 'Воронеж': 'c193',
 'Ростов-на-Дону': 'c39',
 'Шахты': 'c11053',
 'Таганрог': 'c971',
 'Новочеркасск': 'c238',
 'Волгодонск': 'c11036',
 'Краснодар': 'c35',
 'Анапа': 'c1107',
 'Новороссийск': 'c970',
 'Сочи': 'c239',
 'Туапсе': 'c1058',
 'Геленджик': 'c10990',
 'Армавир': 'c10987',
 'Ейск': 'c10993',
 'Майкоп': 'c1093',
 'Черкесск': 'c1104',
 'Нальчик': 'c30',
 'Владикавказ': 'c33',
 'Магас': 'c20181',
 'Грозный': 'c1106',
 'Махачкала': 'c28',
 'Ставрополь': 'c36',
 'Каменск-Шахтинский': 'c11043',
 'Пятигорск': 'c11067',
 'Минеральные Воды': 'c11063',
 'Ессентуки': 'c11057',
 'Кисловодск': 'c11062',
 'Невинномысск': 'c11064',
 'Элиста': 'c1094',
 'Астрахань': 'c37',
 'Волгоград': 'c38',
 'Саратов': 'c194',
 'Жигулевск': 'c11132',
 'Балаково': 'c11143',
 'Пенза': 'c49',
 'Саранск': 'c42',
 'Ульяновск': 'c195',
 'Самара': 'c51',
 'Тольятти': 'c240',
 'Сызрань': 'c11139',
 'Чебоксары': 'c45',
 'Йошкар-Ола': 'c41',
 'Нижний Новгород': 'c47',
 'Саров': 'c11083',
 'Киров': 'c46',
 'Кострома': 'c7',
 'Вологда': 'c21',
 'Архангельск': 'c20',
 'Северодвинск': 'c10849',
 'Сыктывкар': 'c19',
 'Ижевск': 'c44',
 'Казань': 'c43',
 'Набережные Челны': 'c236',
 'Нижнекамск': 'c11127',
 'Пермь': 'c50',
 'Уфа': 'c172',
 'Нефтекамск': 'c11114',
 'Салават': 'c11115',
 'Стерлитамак': 'c11116',
 'Оренбург': 'c48',
 'Дзержинск': 'c972',
 'Челябинск': 'c56',
 'Магнитогорск': 'c235',
 'Снежинск': 'c11218',
 'Курган': 'c53',
 'Екатеринбург': 'c54',
 'Каменск-Уральский': 'c11164',
 'Нижний Тагил': 'c11168',
 'Новоуральск': 'c11170',
 'Первоуральск': 'c11171',
 'Тюмень': 'c55',
 'Тобольск': 'c11175',
 'Ханты-Мансийск': 'c57',
 'Сургут': 'c973',
 'Нижневартовск': 'c1091',
 'Омск': 'c66',
 'Новосибирск': 'c65',
 'Бердск': 'c11314',
 'Томск': 'c67',
 'Салехард': 'c58',
 'Барнаул': 'c197',
 'Бийск': 'c975',
 'Рубцовск': 'c11251',
 'Горно-Алтайск': 'c11319',
 'Кемерово': 'c64',
 'Междуреченск': 'c11287',
 'Новокузнецк': 'c237',
 'Прокопьевск': 'c11291',
 'Абакан': 'c1095',
 'Кызыл': 'c11333',
 'Красноярск': 'c62',
 'Ачинск': 'c11302',
 'Норильск': 'c11311',
 'Железногорск': 'c20086',
 'Иркутск': 'c63',
 'Братск': 'c976',
 'Улан-Удэ': 'c198',
 'Чита': 'c68',
 'Якутск': 'c74',
 'Благовещенск': 'c77',
 'Биробиджан': 'c11393',
 'Владивосток': 'c75',
 'Находка': 'c974',
 'Уссурийск': 'c11426',
 'Анадырь': 'c11458',
 'Петропавловск-Камчатский': 'c78',
 'Магадан': 'c79',
 'Южно-Сахалинск': 'c80',
 'Хабаровск': 'c76',
 'Комсомольск-на-Амуре': 'c11453'}

#Функция для получения Яндекс-кода города
def get_code(town):
    return russian_cities[town][0]

#Функция для получения географического расположения города
def get_coordinates(town):
    for k in range(len(russian_cities[town][1])):
        if russian_cities[town][1][k]['coordinates']['latitude'] != '' and russian_cities[town][1][k]['coordinates'][
            'longitude'] != '':
            return russian_cities[town][1][k]['coordinates']

#Функция для получения примерного расстояния по прямой между городами 1 и 2
def get_distance(town_1, town_2):
    coordinates_town_1 = get_coordinates(town_1)
    coordinates_town_2 = get_coordinates(town_2)
    if coordinates_town_2['latitude'] and coordinates_town_1['latitude'] and coordinates_town_2['longitude'] and coordinates_town_1['longitude']:
        return 40075*((((coordinates_town_2['latitude']-coordinates_town_1['latitude'])**2)+((coordinates_town_2['longitude']-coordinates_town_1['longitude'])**2))**(1/2))/360
    else:
        return (town_2)

#Функция для получения списка ближайших городов
def get_nearby_town(from_town, to_town, distance, big_towns):
    four_nearby_dictanse = []
    i = 1.2
    while len(four_nearby_dictanse)<1:
        nearby = {}
        for town in big_towns:
            if type(get_distance(to_town, town))!=float:
                print (town)
            elif get_distance(from_town, town)+get_distance(to_town, town)<=i*distance and town!=to_town and get_distance(to_town, town)<=1.2*get_distance(to_town, from_town) and get_distance(from_town, town)<=1.2*get_distance(to_town, from_town):
                nearby[town]=get_distance(from_town, town)+get_distance(to_town, town)
        four_nearby_dictanse = sorted(nearby.items(), key=lambda item: item)
        i+=0.1
    four_nearby=[i[0] for i in four_nearby_dictanse]
    return four_nearby[:4]

#Функция для получения расписания прямых рейсов
def get_data_strait(from_town, to_town, time):
    code_from_town = get_code(from_town)
    code_to_town = get_code(to_town)
    url_strait = f"https://api.rasp.yandex.net/v3.0/search/?apikey=c219b14b-3858-49c3-b674-05efd8b6175b&format=json&from={code_from_town}&to={code_to_town}&lang=ru_RU&page=1&date={time}"
    response = requests.get(url_strait)

    if response.status_code == 200:
        data_strait = response.json()
        return data_strait
    else:
        return("Ошибка:", response.status_code)

#Функция для сортировки расписания прямых рейсов и вывода основных характеристик маршрута
def sort_routes(segments, sort_by='time', transport_priority=None, exclude_transport=None):
    if transport_priority is None:
        transport_priority = []
    if exclude_transport is None:
        exclude_transport = []

    # Фильтрация исключенных типов транспорта
    filtered_segments = [
        s for s in segments
        if s['thread']['transport_type'] not in exclude_transport
    ]

    # Определение порядка приоритета транспорта
    transport_order = {transport: idx for idx, transport in enumerate(transport_priority)}
    default_priority = len(transport_priority)

    # Функция для получения ключа сортировки
    def get_sort_key(segment):
        transport_type = segment['thread']['transport_type']
        priority = transport_order.get(transport_type, default_priority)

        if sort_by == 'price':
            # Получение цены (если данные доступны)
            tickets_info = segment.get('tickets_info', {})
            price = tickets_info.get('price', float('inf')) if tickets_info else float('inf')
            return (priority, price)
        elif sort_by == 'time':
            # Сортировка по времени в пути (duration)
            return (priority, segment['duration'])
        else:
            raise ValueError("sort_by должен быть 'time' или 'price'")

    # Сортировка сегментов
    sorted_segments = sorted(filtered_segments, key=get_sort_key)

    # Формирование результата
    result = []
    for seg in sorted_segments:
        thread = seg['thread']
        from_station = seg['from']['title']
        to_station = seg['to']['title']
        tickets_info = seg.get('tickets_info', {})

        result.append({
            'departure_time': seg['departure'],
            'arrival_time': seg['arrival'],
            'duration': seg['duration'],
            # 'duration': f'{int(seg['duration'])//60//60//24} дней, {int(seg['duration'])//60//60%24} часов, {int(seg['duration'])//60%60%24} минут',
            'price': tickets_info.get('price') if tickets_info else None,
            'from': from_station,
            'to': to_station,
            'name': thread['title'],
            'transport_type': thread['transport_type']
        })

    return result


#Функция для получения расписания стыковочных рейсов, если отсутствуют прямые

def get_data_transfer(from_town, to_town, time):
    code_from_town = get_code(from_town)
    code_to_town = get_code(to_town)
    data_strait = get_data_strait(from_town, to_town, time)
    url_transfer = f"https://api.rasp.yandex.net/v3.0/search/?apikey=c219b14b-3858-49c3-b674-05efd8b6175b&format=json&from={code_from_town}&to={code_to_town}&lang=ru_RU&page=1&date={time}&transfers=True"
    if data_strait['pagination']['total']==0:
        response = requests.get(url_transfer)
        if response.status_code == 200:
            data_transfer = response.json()
            return data_transfer
        else:
            return("Ошибка:", response.status_code)


#Пример работы всей этой ерунды для прямого рейса
from_town = 'Симферополь'
to_town = 'Москва'
time = '2025-03-20'
#transport_priority=None
#exclude_transport=None

data = get_data_strait(from_town, to_town, time)
sort_routes(data['segments'], sort_by='time')

'''[{'departure_time': '2025-03-20T18:05:00+03:00',
  'arrival_time': '2025-03-21T23:50:00+03:00',
  'duration': 107100.0,
  'price': None,
  'from': 'Симферополь-Пасс.',
  'to': 'Москва (Казанский вокзал)',
  'name': 'Симферополь — Москва',
  'transport_type': 'train'},
 {'departure_time': '2025-03-20T19:50:00+03:00',
  'arrival_time': '2025-03-22T06:10:00+03:00',
  'duration': 123600.0,
  'price': None,
  'from': 'Симферополь-Пасс.',
  'to': 'Москва (Казанский вокзал)',
  'name': 'Симферополь — Москва',
  'transport_type': 'train'},
 {'departure_time': '2025-03-20T23:10:00+03:00',
  'arrival_time': '2025-03-22T10:00:00+03:00',
  'duration': 125400.0,
  'price': None,
  'from': 'Симферополь-Пасс.',
  'to': 'Москва (Казанский вокзал)',
  'name': 'Севастополь — Москва',
  'transport_type': 'train'},
 {'departure_time': '2025-03-20T22:20:00+03:00',
  'arrival_time': '2025-03-22T12:09:00+03:00',
  'duration': 136140.0,
  'price': None,
  'from': 'Симферополь-Пасс.',
  'to': 'Москва (Павелецкий вокзал)',
  'name': 'Симферополь — Москва',
  'transport_type': 'train'},
 {'departure_time': '2025-03-20T21:10:00+03:00',
  'arrival_time': '2025-03-22T13:22:00+03:00',
  'duration': 144720.0,
  'price': None,
  'from': 'Симферополь-Пасс.',
  'to': 'Москва (Павелецкий вокзал)',
  'name': 'Симферополь — Москва',
  'transport_type': 'train'}]'''
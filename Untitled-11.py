import telebot
from telebot import types

bot = telebot.TeleBot('6182703487:AAFRmRE3OpLZq82XdazUXrJ8PkQlhZGAN9Y');
@bot.message_handler(commands=['start'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    item1 = types.KeyboardButton('Информация')

    markup.add(item1) 

    bot.send_message(message.chat.id,'Приветствую , {0.first_name}!\nЕсли хотите узнать побольше про данного бота, жмите на кнопку "Информация"!'.format(message.from_user), reply_markup=markup)


    

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Диеты')
            item2 = types.KeyboardButton('Калоризатор')
            
            markup.add(item1,item2)

            bot.send_message(message.chat.id, 'Данный бот даст общую информацию про различные диеты и их составление, а также помогает высчитать калорийность любого продукта!\nВыберите интересующий Вас пункт, основываясь на кнопки ниже.',reply_markup=markup)
            
        elif message.text == 'Калоризатор':
            markup=types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Сайт для самостоятельного подсчёта калорий', url='https://doctorushakov.com/calculator'))
            bot.send_message(message.chat.id, 'Что такое калории?\n\n«В школьном учебнике по физике без труда найдется определение, что калория — это количество тепловой энергии, которое позволяет нагреть один грамм воды на один градус Цельсия при стандартном атмосферном давлении. Название этой единицы измерения пошло от латинского calor — «тепло». Но энергетическая ценность пищи измеряется обычно в более крупных единицах — килокалориях, в 1 ккал — 1000 калорий, и речь идет в данном случае уже о килограмме воды. То есть калории — это единицы энергии, заключенной в пище, которые наш организм может или использовать сразу, или отложить про запас».\n\nКнопка под сообщением приведёт Вас на сайт, с помощью которого Вы сами сможете подсчитать норму калорий с учётом суточной активности, физической нагрузки и состояния здоровья.', reply_markup=markup)


        elif message.text == 'Диеты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Сбалансированная диета')
            item2 = types.KeyboardButton('Экспресс (голодная) диета')
            item3 = types.KeyboardButton('Селективная (односторонняя) диета')
            item4 = types.KeyboardButton('Констрастная (монодиета)')
            item5 = types.KeyboardButton('Натуропатическая (естественная) диета')
            item6 = types.KeyboardButton('Искусственная диета')
            item7 = types.KeyboardButton('Назад')
    

            markup.add(item1,item2,item3,item4,item5,item6,item7)

            bot.send_message(message.chat.id, 'Что такое диета?\n\nДиета - это Строгое и сознательно ограничение количества энергии, потребляемой с пищей (калораж). Например, это может быть соблюдение какой-либо известной диеты или просто подсчет калорий и установление жестких рамок.\nДиеты привычны и популярны. Считается, что примерно половина женщин нормального веса пытались придерживаться диеты. Одно из исследований показало, что на диете сидят почти 70% 15-летних девушек и 8% из них придерживаются крайне строгой диеты. В результате другого исследования было установлено, что примерно 70% женщин и 45% мужчин, сидящих на диете, не имеют лишнего веса, и им не нужно придерживаться никаких диет.\n Главное помните, что какой бы тип диеты вы не выбрали, мы рекомендуем терять лишний вес, не теряя головы на плечах! Не спешите доверять авторитетам и заявлениям звёзд, взвешивайте все «за» и «против», читайте отзывы, обязательно консультируйтесь с врачом – и тогда вы наверняка останетесь довольны результатами!\n\nНиже приведены 6 самых популярных и обобщённых диет, с которыми вы можете ознакомиться, перейдя по кнопкам.',reply_markup=markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item8 = types.KeyboardButton('Диеты')
            item9 = types.KeyboardButton('Калоризатор')
            
            markup.add(item8,item9)
            bot.send_message(message.chat.id,'Возвращаю Вас обратно в меню.', reply_markup=markup)


        elif message.text == 'Сбалансированная диета':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back2 = types.KeyboardButton('Назад')
            markup.add(back2)
            bot.send_message(message.chat.id,'Такой тип питания еще называют рациональным, то есть, разумным. Он относительно легко совмещается с привычным образом жизни. Точнее, подразумевается, что вы можете сделать привычным для себя новый, научно обоснованный рацион, которого и будете придерживаться в дальнейшем.\nСбалансированная диета может быть низкокалорийной (800-1400 ккал в день) и нормальной калорийности. Она обязательно содержит сбалансированный набор жиров, белков, углеводов, витаминов, минералов и других пищевых элементов – особенно незаменимых. При этом учитывается ваш пол, возраст, профессия, наследственность и т.д.',reply_markup=markup)


        elif message.text == 'Экспресс (голодная) диета':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back3 = types.KeyboardButton('Назад')
            markup.add(back3)
            bot.send_message(message.chat.id,'Это несбалансированные низкокалорийные диеты, которые рассчитаны на 1-3 недели. Они обычно содержат только самый минимум питательных веществ.\nОграничения призваны перевести работу вашей пищеварительной системы на «резервное питание» – то есть, прежде всего, помочь быстро избавиться от жировых запасов.', reply_markup=markup)

        elif message.text == 'Селективная (односторонняя) диета':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Назад')
            markup.add(back4)
            bot.send_message(message.chat.id,'К данной группе относятся диеты низкоуглеводные, обезжиренные, белковые, овощные и т.п. Принцип прост – из всего спектра вкусной и здоровой пищи вы выбираете лишь ту, которая подходит по какому-то признаку.\nНапример, не содержит определенных соединений. Или содержит их в максимальном количестве (как в случае с белками). Но, конечно, такой «урезанный паек» также не следует растягивать надолго.',reply_markup=markup)

        elif message.text == 'Констрастная (монодиета)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back5 = types.KeyboardButton('Назад')
            markup.add(back5)
            bot.send_message(message.chat.id,'Это очень интересный вариант диеты для похудения. От вас не потребуется особых усилий. Придерживаться такой системы питания нужно не меньше месяца. Для того чтобы похудеть, нужно чередовать строгое питание (1 неделя) и более свободное (1 неделя). Дело в том, что в обычных диетах организм сначала стремительно сбрасывает вес, а потом потеря лишних килограммов приостанавливается. Это связано с тем, что организм попросту привыкает.\nПри контрастной диете можно постараться обмануть ваш организм . Первую неделю вы худеете, а вторую – закрепляете результат без особых усилий. Затем, вновь нужно повторить данную схему. Это очень удобная диета для тех, кто не может выдерживать слишком строгие ограничения в еде, но очень хочет похудеть.', reply_markup=markup)                          

        elif message.text == 'Натуропатическая (естественная) диета':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back6 = types.KeyboardButton('Назад')
            markup.add(back6)
            bot.send_message(message.chat.id,'В зависимости от ваших индивидуальных целей, вкусов, убеждений или вероисповедания вы можете сделать ставку на раздельное питание, вегетарианство, сыроедение, соки, частичный или даже полный отказ от пищи.\nВ конце концов, разок в неделю можно и поголодать: многочисленные авторы уверяют, что это весьма полезно. Естественно, никто не собирается лишать вас удовольствия, только имейте в виду: чистая вода человеку жизненно необходима. Не отказывайтесь от нее – особенно, если голодаете. Ведь именно вода помогает вымывать шлаки из организма!', reply_markup=markup)

        elif message.text == 'Искусственная диета':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back7 = types.KeyboardButton('Назад')
            markup.add(back7)
            bot.send_message(message.chat.id,'Искусственные диеты выстраиваются на применении пищевых заменителей, концентратов, питательных смесей, биологически активных добавок (БАД) и т.п. Минимум усилий – максимум эффекта.\nНо поскольку искусственные продукты сильно разнятся по качеству, происхождению и воздействию, вы, во-первых, должны быть твердо уверены в том, что делаете, а во-вторых, безопаснее проводить такие эксперименты строго под наблюдением врача.',reply_markup=markup)

bot.polling(non_stop=True)




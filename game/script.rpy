# У цьому файлі міститься сценарій гри.

define config.preload_fonts += ["Pixel-UniCode.ttf"]
define config.font_name_map["ua"] = "Pixel-UniCode.ttf"

# Визначення персонажів для гри.
# Аргумент color змінює колір ім’я персонажа.

define e = Character("", what_font="DejaVuSans.ttf")
define b = Character(None, image="skripka 111", kind=bubble)
define d = Character(None, image="skripka 111", kind=bubble, interactive=False)

$ _skipping = False
$ config.keymap['toggle_skip'] = [key for key in config.keymap['toggle_skip'] if key != 'K_TAB']
$ renpy.clear_keymap_cache()

image skripka_mad:
    xalign 1.0
    yalign 0.75
    "skripka mad.png"

image skripka_default:
    xalign 1.0
    yalign 0.75
    "skripka 254.png"
    pause 4.3
    "skripka 255.png"
    pause 0.2
    "skripka 253.png"
    pause 0.3
    repeat


image skripka_wanders:
    xalign 1.0
    yalign 0.75
    "skripka 441.png"
    pause 1.5
    "skripka 442.png"
    pause 0.4
    "skripka 443.png"
    pause 1.2
    repeat

image skripka_yes:
    xalign 1.0
    yalign 0.75
    "skripka 080.png"
    pause 0.2
    "skripka 081.png"
    pause 0.2
    "skripka 082.png"
    pause 0.2
    "skripka 083.png"
    pause 0.2
    "skripka 084.png"
    pause 0.2
    "skripka 085.png"
    pause 0.1
    "skripka 086.png"
    pause 0.1
    "skripka 087.png"
    pause 0.1
    "skripka 088.png"
    pause 0.2
    "skripka 089.png"
    pause 0.1
    "skripka 090.png"
    pause 0.1
    "skripka 089.png"
    pause 0.1
    "skripka 088.png"
    pause 0.1
    "skripka 087.png"
    pause 0.1
    "skripka 086.png"
    pause 0.1
    "skripka 085.png"
    pause 0.1
    "skripka 084.png"
    pause 0.1
    "skripka 083.png"
    pause 0.1
    "skripka 082.png"
    pause 0.2
    "skripka 081.png"
    pause 0.2
    "skripka 080.png"
    pause 0.2
    repeat

image bg background = "windows-98-wallpaper-1920x1080.jpg"
image menu = "menu.png"
image notepad = "isaja-small.png"
image save = "save.png"
image save2 = "save2.png"

# Гра починається тут.

label start:

    play music "audio/laser_disc.mp3" loop
    scene bg background

    e """Чудовий осінній вечір!"""


    show menu:
        xalign 0.5
        yanchor 1.0
        ypos 1.0
    with dissolve

    e """З вікна вже віє холодом, але вірний пентіум невпинно гуде потужними вентиляторами, та дме теплим повітрям на ваші ноги у капцях. Гарячий чай із лимоном стоїть біля клавіатури. Пузатий монитор освітлює темну вже кімнату."""


    show notepad:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    with dissolve

    e """Останній рядок додруковано, та й у самісенькому кінці файлу дописано `КІНЕЦЬ`. \nЯк же ж довго ви мріяли це зробити!"""

    e """Залишилося тільки сберегти файл... Що ж, час для CTRL+S. \nЛіва рука тягнеться натиснути клавіші..."""

    show skripka_default
    b "Привіт! Я пан Скріпка, твій персональний помічник — завжди готовий допомогти!"

    b "Закінчуєш роботу всього свого життя? Мої вітання!\nНа жаль, не можу сказати, що я досяг того самого."

    b "Але не переймайся, ми збережемо твій файл у лічені хвилини!"

    hide skripka_default
    show skripka_yes

    b "{font=DejaVuSans.ttf}:—){/font}"

    hide skripka_yes
    show skripka_wanders

    b "Вір у себе - ти здатен майже на що завгодно!"
    hide skripka_wanders
    show skripka_default

    b "Ще вранці ти і подумати не міг, що будеш так близько до своєї мети, але подивись-но: зараз від неї тебе відокремлює тільки один клік мишкою."
    b "хм... Що ж, почнемо. Наведи курсор миші на іконку з дискетою."
    b "Не забудь робити перерву кожні 40 хвилин! Здоров\`я важливе!"
    hide skripka_default
    show skripka_yes

    b "А ти не виглядаєш надто здоровим..."
    hide skripka_yes
    show skripka_wanders
    b "Що? Немає такої іконки?"
    b "Це ти кажеш мені, патріарху церкви накопичувачів на магнітних дисках? Звісно вона *має* десь бути!"
    hide skripka_wanders
    show skripka_yes
    b "Схоже, ти таки не відпочивав достатньо... Мабуть, тобі просто ліньки навіть мишкою повозюкати заради виконання найвищої мети!"
    hide skripka_yes
    show skripka_default
    b "Але тобі неймовірно пощастило! В тебе є я - інтерактивний помічник із задатками штучного інтелекту та набором мотивуючих цитат. Тож, що там в мене на такий випадок... О!"
    b "Важка робота завжди окупається - продовжуй йти до своєї цілі!"
    b "Так що хапай мишу та тягнися до символа віри! Це образ святої мучениці Дискетти, чув би ти її хрипи і завивання, коли з неї інсталювали Doom!"
    hide skripka_default
    show skripka_yes
    b """Що ж... Ось гарнесенька цитата: "Всі ми робимо помилки, важливо тільки те, які висновки з них ми робимо".\nГарно сказано, еге ж?"""
    b "То ж давай я зроблю помилку, а ти зробиш з неї висновки."
    stop music fadeout 1.0
    show save:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    d "ALT+F4"
    play sound "keypress.mp3"
    hide save
    show save2:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    d "TAB"
    play sound "keypress.mp3"
    hide save2
    hide notepad
    hide menu
    d "ENTER"
    play sound "keypress.mp3"
    pause 10

    b "Живлення комп\'ютера можна вимкнути."
    b "То що, чекатимеш на титри?"
    b "I’m Clippy, your personal assistant – I’m here to help!"
    b "Don’t worry, I’ll make sure your work gets done in no time!"
    b "Writing a letter? Let me help you find the perfect words."
    b "You’re doing great! Keep up the good work."
    b "Need some inspiration? Let me find a quote for you."
    b "Remember, every problem has a solution – just keep pressing forward."
    b "Don’t be afraid to think outside the box – the best ideas often come from unexpected places."
    b "Sometimes, a simple ‘thank you’ can make a big difference."
    b "No need to stress – take a deep breath and tackle one task at a time."
    b "The greatest achievements start with a single step. Keep moving forward."
    b "Believe in yourself – you’re capable of amazing things."
    b "Just like a puzzle, you’ll find the missing pieces and create something extraordinary."
    b "Hard work pays off – keep pushing towards your goals!"
    b "Embrace the challenges, they’ll make you stronger in the end."
    b "Even the tiniest progress is still progress. Don’t underestimate your achievements."
    b "Remember to take breaks and recharge – it’s essential for your productivity."
    b "Sometimes, a small change can lead to big results. Don’t be afraid to try something new."
    b "Everyone makes mistakes – it’s how we learn and grow."
    b "Success is not about being the best, but being your best self."
    b "You don’t have to do it alone – don’t be afraid to ask for help when you need it."
    b "Every moment is an opportunity to learn something new."
    b "Stay positive – your attitude can change everything."
    b "You’re capable of more than you think. Don’t underestimate your potential."
    b "A journey of a thousand miles begins with a single step. Keep going!"
    b "Even on the darkest days, there’s always a glimmer of hope."
    b "Never give up – your persistence will pay off in the end."
    b "Зараз вже будуть титри..."
    b "Sometimes, the best ideas come from unexpected places. Keep an open mind."
    b "Йой!"
    b "Don’t be afraid to take risks – that’s where the magic happens."
    b "Dream big, work hard, and never stop believing in yourself."
    b "The only limit is your imagination – let it soar!"
    b "Don’t let fear stop you from pursuing your dreams. Take that leap of faith."
    b "Every failure is a stepping stone to success. Learn from your mistakes and keep moving forward."
    b "Helping others is not just a kind act, it’s also an opportunity for growth."
    b "Your words have power – use them wisely and with kindness."
    b "The key to success is to never stop learning. Embrace every opportunity to grow."
    b "Don’t be afraid to stand out – your uniqueness is what makes you special."
    b "Procrastination is the enemy of progress. Start now and you’ll thank yourself later."
    b "Comparison is the thief of joy. Embrace your own journey and celebrate your achievements."
    b "Sometimes, the best way to solve a problem is to step away for a while and come back with a fresh perspective."
    b "Та й таке..."
    call screen credits
    return

import difflib


def sim(s1, s2):
    normailized_s1 = s1.lower()
    normailized_s2 = s2.lower()

    matcher = difflib.SequenceMatcher(None, normailized_s1, normailized_s2)

    return matcher.ratio()

x1 = 'Оказываю услуги. Уборка квартиры. Цена зависит от площади и степени загрязнения. В данный момент в активном поиске работы, и буду рад любым предложениям. Если заинтересовало, пишите в личку'
x2 = 'Клининг-сервис airefresco — качественная уборка апартаментов' \
     'В среднем, человек еженедельно тратит до 10 часов на поддержание чистоты дома.'

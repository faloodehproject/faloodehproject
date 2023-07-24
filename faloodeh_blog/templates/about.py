from Faloodeh.Faloodeh_UI import html5 , css3

html = html5()
html.h2(inner='سلام من امیر محمد دهقان هستم ', style=css3(font_size='40px'))
html.p(
    inner='''
    من تقریبا 3 ساله هست از سال 99 برنامه نویسی رو شروع کردم و 
    اولین زبانی که یادگرفتم زبان پایتون بود و باعث شد به برنامه نویسی علاقه مند بشم و ادامه بدم
    بعد از اون با زبان های زیادی مثل java , Dart , javascript , C++ و چهار چوب هاشون مثل flutter , django , flask , beeware , bootstrap5 tailwind و کلی 
    دیگه که اسمشون تو ذهنم نیست ولی از بین اینهمه راه و زبان و چهارچوب  زبان پایتون چهارچوب جنگو و حوضه وب رو به عنوان تخصصم انتخاب کردم البته بماند که فول استک هستم 
    الان و بعد از اون تصمیم گرفتم برای خودم یه چهارچوب فول استک وب بنویسم با پایتون شاید اگه زبان php بود کارم خیلی راحت تر بود ولی از اون جایی که من کار های راحت رو
    دوست ندارم رفتم سمت ساخت چهارچوب وب با پایتون خب اول اینکه هیچ اسناد و متن فارسی که چه عرض کنم انگلیسیش هم نبود
    فقط مقداری مطالب سطح خیلی پایین و انتزایی وخوب هیچ حد وسطی نبود پس تصمیم گرفتم این حد وسط رو خودم بسازم
    و خب حاصل 6 ماه تلاشم شد این عزیز و اسمشم فالوده گذاشتم و اولین از نوع خودش در ایران هست.
    ''',
    style=css3(font_size='35px')
    )
if __name__ == '__main__':
    print(html)


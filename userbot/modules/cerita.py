from userbot import CMD_HELP, bot
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinickcerita":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita Dulu BossKu` ", 
            " .type Sejak aku putus dari kekasihku, aku menjadi sangat depresi. Aku merasa hidupku tak ada gunanya lagi. Bagaimana tidak? hubungan yang telah kubina selama 6 tahun harus kandas begitu saja. Aku telah menjalani hubungan yang panjang dan terlalu jauh bersamanya.
            Setelah putus darinya aku tak mau lagi mengenal cowok dan tak mau membina hubungan lagi, aku sudah trauma dan merasa tak pantas lagi merasakan cinta. Aku menjalani hari - hariku seperti air yang mengalir yang hanya mengikuti arus dan tak tahu akan ke mana bermuara. Yang jelas aku sangat hancur ketika kekasihku tak lagi mempertahankan hubungan kami dan meninggalkan diriku begitu saja. Tak ada yang bisa aku salahkan, karena semua memang salahku telah melakukannya dengan dia dengan alasan cinta, itulah sebabnya aku tak mau lagi merasakan cinta dengan cowok lain. Aku takut hal yang sama akan terulang.
            Aku bekerja di sebuah yayasan sosial, di sana aku hanya mempunyai seorang teman cowok bernama Vyan. Dia adalah satu - satunya cowok yang dekat dengan aku karena dia adalah anaknya teman papaku. Dia orang yang sangat baik, taat beribadah, dan dia tak pernah mengenal pacaran sehingga dia tak akan mengerti rasa sakit yang aku alami.
            Sebenarnya orangtuaku berusaha mendekatkan aku dengan Vyan tapi aku tak akan pernah mau menjalin hubungan asmara dengan dia, karena dia terlalu suci buat diriku yang hina ini. Vyan selalu berusaha mengingatkan aku pada Allah karena sejak frustasi aku tak lagi menjalankan salat, tak lagi mengingat Sang Pencipta.
            Vyan tak pernah lelah menjadi alarm ketika waktunya salat. Namun aku tetap menganggap dia hanya seorang teman dan tak lebih. Tak akan mungkin aku memiliki perasaan padanya. Pada tanggal 19 Maret tepatnya di hari ulang tahunku, Vyan memberiku surprise yang tak terduga, dengan memberikan sebuah cincin dan dia mengatakan ingin melamarku. Tak perlu berpikir panjang aku langsung menolaknya. Aku berjanji tak akan menerimanya. Karena aku tak pantas untuk mendampingi hidup seorang Vyan yang aku anggap cowok paling suci yang pernah aku temui.
            Vyan tak marah padaku karena aku menolaknya, hanya dia selalu bertanya apa alasanku tak mau menerimanya. Walau begitu orangtuaku sangat marah padaku karena memang sebenarnya aku dijodohkan dengan Vyan. Aku pun tak berani mengungkapkan kepada semuanya mengenai alasanku mengapa menolak Vyan. Aku takut akan murkanya orangtuaku dan aku juga tak mau dibenci oleh Vyan karena keadaanku yang telah ternodai.
            Sebenarnya alasanku menolak Vyan bukan karena aku tak ada rasa kepadanya tetapi karena aku sudah tak suci lagi. Aku telah memberikan kehormatanku sebagai wanita kepada mantan kekasihku. Aku sangat menyesal melakukannya, aku tak dapat lagi berkata - kata jika mengingat hal itu. Aku tak ingin ada orang yang tahu sehingga sejak aku putus dari mantan kekasihku aku tak mau lagi mengenal cowok. Perasaan berdosa dan menyesal selalu menghantuiku dan perasaan takut untuk menikah juga selalu membayangiku. Aku tak pantas lagi dicintai apalagi dicintai seorang Vyan.
            Namun orangtua dan juga Vyan selalu mendesak aku dan ingin tahu jawabanku tentang alasan aku menolaknya. Tetapi aku tak berani mengatakannya. Semakin sakit aku diam, semakin terluka jika aku bungkam. Akhirnya sore itu aku mengajak Vyan untuk ketemuan di taman, aku akan menjelaskan semuanya kepada Vyan tentang diriku yang ternoda ini.
            Sebelum aku menjelaskan tentang diriku, Vyan memberiku sebuah kain. Kemudian aku diminta untuk mengatakan yang sejujurnya. Dengan kata yang terbata - bata aku mulai membuka mulut bahwa, Sebenarnya aku sudah ti..dak.. pe..., kemudian Vyan memotong perkataanku lalu menjawab, Aku sudah tahu semuanya, aku tahu kamu telah ternoda tapi aku mau menerima asalkan kamu mau memakai kain itu, dan kita mulai hidup yang baru dalam ikatan yang halal.
            Alangkah terkejutnya aku mendengar semua itu. Aku tak menyangka Vyan ternyata sudah mengetahuinya. Setelah aku membuka kain itu adalah sebuah hijab. Masya Allah aku begitu beruntung. Vyan mengatakan bahwa cinta itu indah dan tak memandang status apapun. Aku merasa bahwa cintanya Vyan bukanlah cinta biasa, dan aku adalah noda yang ia jadikan mutiara. Pada akhirnya aku menikah dengan Vyan dan kini hidup bahagia bersama seorang jagoan serta calon adiknya yang masih berusia 6 bulan dalam kandungan.
            ",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])

CMD_HELP.update({
    "Cerita":
    "`.sinick1`\
    \nUsage: cerita dulu bro."
})






define ale = Character("Alex", color="#51c2ef")
define luc = Character("Lucy", color="#ecbaef")
define mil = Character("Milena", color="#f4e68b")
define mae = Character("Maela", color="#ccff66")
define ann = Character("Anna", color="#b19eff")
define lau = Character("Laura", color="#cdffc1")
define ana = Character("Anastacia", color="#ffa991")
define kyr = Character("Kyra", color="#ff6363")
define mir = Character("Miranda", color="#bcff75")
define lis = Character("Lisa", color="#ff75f7")
define kir = Character("Kirk", color="#bcffbc")
define aya = Character("Aya", color="#b0aaff")
define nik = Character("Nikky", color="#b0aaff")
define ruz = Character("Ruzena", color="#f2f298")
define lar = Character("Lara", color="#ffa184")
define edd = Character("Eddy", color="#ccffff")
define don = Character("Donna", color="#f2cfa7")
define fen = Character("Fenella", color="#fffaaa")
define flo = Character("Floyd", color="#a2dcef")
define gia = Character("Gianna", color="#dff9bd")
define mar = Character("Mario", color="#fdfffc")
define lui = Character("Luigi", color="#66ff66")
define mom = Character("Alexandra", color="#fff054")
define sab = Character("Sabrina", color="#a0ffec")
define bor = Character("Bornay", color="#a0ffec")
define brb = Character("Barbara", color="#ff9854")
define stranger = Character("Stranger", color="#fdfffc")
define unk = Character("???", color="#ff9854")
define tat = Character("Tatiana", color="#d6ffda")
define sam = Character("Samantha", color="#ccfffa")
define kro = Character("Krondor", color="#c1c1c1")
define sar = Character("Sarah", color="#66ffcc")
define adr = Character("Adrianna", color="#cc6699")
define sao = Character("Saori", color="#6666ff")
define gin = Character("Ginna", color="#ff66ff")
define tha = Character("Thays", color="#ff9900")
define lin = Character("Linda", color="#ffff66")
define ama = Character("Amanda", color="#ccff66")
define mark = Character("Mark", color="#ccccff")
define nin = Character("Nina", color="#d1edf9")
define boris = Character("Boris", color="#a0ffec")
define sor = Character("Sora", color="#ffff66")
define ste = Character("Stella", color="#dbc276")
define suk = Character("Suki", color="#ccff66")
define minj = Character("Minji", color="#ff9626")
define mire = Character("Mireia", color="#59d66e")
define bob = Character("Bob", color="#a0ffec")
define ala = Character("Alanna", color="#ffff66")
define mary = Character("Mary", color="#dbc276")
define daf = Character("Dafne", color="#ffaddb")
define dug = Character("Dugald", color="a0ffec")
define pyo = Character("Pyotr", color="#f46542")
define hei = Character("Heike", color="#c7d4ea")
define bil = Character("Bill", color="#c7d4ea")
define ade = Character("Adele", color="#b7ffcd")
define mia = Character("Mia", color="#ff77fa")
define vic = Character("Victoria", color="#d6ba6f")
define adria = Character("Adria", color="#ddf6ff")
define aur = Character("Aurora", color="#ff9966")
define shi = Character("Shibuya", color="#82E0AA")
define marian = Character("Marian", color="#e0dd7f")
define mon = Character("Monica", color="#d7e590")
define ver = Character("Verdi", color="#e3ff96")
define emm = Character("Emma", color="#f7cba8")
define tif = Character("Tiffany", color="#d9ffb3")
define dad = Character("Miranda's Dad", color="#ccffe6")
define val = Character("Valentina", color="#efa5c3")
define dad2 = Character("Anastacia's Dad", color="#ccffe6")
define sco = Character("Scotty", color="#ccffe6")
define uya = Character("Uyara", color="#bf4040")
define bos = Character("Boss", color="#ccff33")
define lun = Character("Luna", color="#e6b3ff")
define era = Character ("Erasmus",color="#ccffe6")
define lyse = Character ("Lysette",color="#ffff99")
define mabe = Character ("Mabelle",color="#ff80bf")
define cammy = Character ("Cammy",color="#ffff99")
define kar = Character ("Karoline",color="#ffcc99")
define eli = Character ("Elise",color="#ffff1a")
define tho = Character("Thomas", color="#f46542")
define jos = Character ("Josephina",color="#ffff1a")
define tas = Character ("Tasha",color="#ffff1a")
define han = Character("Dr. Hans", color="#f46542")
define bia = Character("Bianca", color="#ffff66")
define edw = Character("Edwards", color="#ccff33")
define hin = Character("Hina", color="#ffff66")
define fran = Character("Fran", color="#dbc276")



define flash = Fade(0.1, 0.0, 0.5, color="#fff")


default heart_house = False
default heart_park = False
default heart_gym = False
default heart_girls = False
default heart_beach = False
default heart_school = False
default heart_square = False
default heart_library = False
default heart_bank = False
default heart_pub = False
default heart_dt = False



init python:
    renpy.music.register_channel("sound2", "sfx", loop=False)
    renpy.music.register_channel("sound3", "sfx", loop=False)






define config.autosave_on_choice = False




screen street_imagemap():
    imagemap:
        ground "map_street_ground"
        hover "map_street_hover"

        hotspot (90, 110, 300, 50) action Jump("map_house")
        hotspot (90, 190, 300, 50) action Jump("map_library")
        hotspot (90, 270, 300, 50) action Jump("map_gym")
        hotspot (90, 350, 300, 50) action Jump("map_pub")
        hotspot (90, 430, 300, 50) action Jump("map_market")
        hotspot (90, 510, 300, 50) action Jump("map_bank")
        hotspot (450, 110, 300, 50) action Jump("map_park")
        hotspot (450, 190, 300, 50) action Jump("map_square")
        hotspot (450, 270, 300, 50) action Jump("map_school")
        hotspot (450, 350, 300, 50) action Jump("map_beach")
        hotspot (450, 430, 300, 50) action Jump("map_girls")
        hotspot (906, 30, 65, 65) action Jump("status_screen")
        hotspot (906, 100, 65, 65) action Jump("atlas_mode")
        hotspot (836, 30, 65, 65) action Jump("chara_screen_1")

screen atlas_imagemap():
    imagemap:
        ground "map_atlas_ground"
        hover "map_atlas_hover"

        if heart_house:
            add "heart_map.png" xpos 100 ypos 200

        if heart_park:
            add "heart_map.png" xpos 200 ypos 300

        if heart_gym:
            add "heart_map.png" xpos 400 ypos 175

        if heart_girls:
            add "heart_map.png" xpos 150 ypos 375

        if heart_beach:
            add "heart_map.png" xpos 800 ypos 500

        if heart_school:
            add "heart_map.png" xpos 700 ypos 200

        if heart_square:
            add "heart_map.png" xpos 700 ypos 400

        if heart_library:
            add "heart_map.png" xpos 800 ypos 200

        if heart_bank:
            add "heart_map.png" xpos 500 ypos 100

        if heart_pub:
            add "heart_map.png" xpos 400 ypos 400

        if heart_dt:
            add "heart_map.png" xpos 600 ypos 100

        hotspot (100, 200, 100, 100) action Jump("map_house")
        hotspot (800, 200, 100, 100) action Jump("map_library")
        hotspot (400, 300, 100, 100) action Jump("map_gym")
        hotspot (400, 400, 100, 100) action Jump("map_pub")
        hotspot (600, 400, 100, 100) action Jump("map_market")
        hotspot (500, 100, 100, 100) action Jump("map_bank")
        hotspot (200, 300, 100, 100) action Jump("map_park")
        hotspot (700, 400, 100, 100) action Jump("map_square")
        hotspot (700, 200, 100, 100) action Jump("map_school")
        hotspot (800, 500, 100, 100) action Jump("map_beach")
        hotspot (100, 500, 200, 100) action Jump("map_girls")
        hotspot (400, 600, 100, 100) action Jump("status_screen")

        hotspot (500, 600, 100, 100) action Jump("chara_screen_1")
        hotspot (600, 100, 100, 100) action Jump("map_downtown")
        hotspot (900, 0, 100, 100) action Jump("patreon_screen")
        hotspot (600, 600, 100, 100) action QuickSave()
        hotspot (300, 600, 100, 100) action Jump("inventory_screen")



screen chara_screen_1():
    imagemap:
        ground "z_chara_screen_1_ground"
        hover "z_chara_screen_1_hover"

        hotspot (450, 550, 100, 100) action Jump("atlas_mode")
        hotspot (325, 550, 100, 100) action Jump("chara_screen_2")
        hotspot (575, 550, 100, 100) action Jump("chara_screen_2")

        hotspot (75, 50, 100, 100) action Jump("chara_kyra")
        hotspot (200, 50, 100, 100) action Jump("chara_anastacia")
        hotspot (325, 50, 100, 100) action Jump("chara_aya")
        hotspot (450, 50, 100, 100) action Jump("chara_lisa")
        hotspot (575, 50, 100, 100) action Jump("chara_miranda")
        hotspot (700, 50, 100, 100) action Jump("chara_milena")
        hotspot (825, 50, 100, 100) action Jump("chara_lucy")

        hotspot (75, 175, 100, 100) action Jump("chara_lara")
        hotspot (200, 175, 100, 100) action Jump("chara_laura")
        hotspot (325, 175, 100, 100) action Jump("chara_anna")
        hotspot (450, 175, 100, 100) action Jump("chara_fenella")
        hotspot (575, 175, 100, 100) action Jump("chara_donna")
        hotspot (700, 175, 100, 100) action Jump("chara_gianna")
        hotspot (825, 175, 100, 100) action Jump("chara_stella")

        hotspot (75, 300, 100, 100) action Jump("chara_tatiana")
        hotspot (200, 300, 100, 100) action Jump("chara_samantha")
        hotspot (325, 300, 100, 100) action Jump("chara_sabrina")
        hotspot (450, 300, 100, 100) action Jump("chara_barbara")
        hotspot (575, 300, 100, 100) action Jump("chara_sarah")
        hotspot (700, 300, 100, 100) action Jump("chara_adrianna")
        hotspot (825, 300, 100, 100) action Jump("chara_sora")

        hotspot (75, 425, 100, 100) action Jump("chara_minji")
        hotspot (200, 425, 100, 100) action Jump("chara_mireia")
        hotspot (325, 425, 100, 100) action Jump("chara_alexandra")
        hotspot (450, 425, 100, 100) action Jump("chara_amanda")
        hotspot (575, 425, 100, 100) action Jump("chara_saori")
        hotspot (700, 425, 100, 100) action Jump("chara_linda")
        hotspot (825, 425, 100, 100) action Jump("chara_ruzena")

screen chara_screen_2():
    imagemap:
        ground "z_chara_screen_2_ground"
        hover "z_chara_screen_2_hover"

        hotspot (450, 550, 100, 100) action Jump("atlas_mode")
        hotspot (325, 550, 100, 100) action Jump("chara_screen_1")
        hotspot (575, 550, 100, 100) action Jump("chara_screen_1")

        hotspot (75, 50, 100, 100) action Jump("chara_nina")
        hotspot (200, 50, 100, 100) action Jump("chara_mary")
        hotspot (325, 50, 100, 100) action Jump("chara_alanna")
        hotspot (450, 50, 100, 100) action Jump("chara_maela")
        hotspot (575, 50, 100, 100) action Jump("chara_adria")
        hotspot (700, 50, 100, 100) action Jump("chara_aurora")
        hotspot (825, 50, 100, 100) action Jump("chara_adele")

        hotspot (75, 175, 100, 100) action Jump("chara_mia")
        hotspot (200, 175, 100, 100) action Jump("chara_victoria")
        hotspot (325, 175, 100, 100) action Jump("chara_shibuya")
        hotspot (450, 175, 100, 100) action Jump("chara_marian")
        hotspot (575, 175, 100, 100) action Jump("chara_monica")
        hotspot (700, 175, 100, 100) action Jump("chara_tiffany")
        hotspot (825, 175, 100, 100) action Jump("chara_verdi")

        hotspot (75, 300, 100, 100) action Jump("chara_emma")
        hotspot (200, 300, 100, 100) action Jump("chara_valentina")
        hotspot (325, 300, 100, 100) action Jump("chara_suki")
        hotspot (450, 300, 100, 100) action Jump("chara_twins")

















default alex_status_str = 0
default alex_status_int = 0
default alex_status_app = 0




default persistent.watermark = False
default persistent.vanilla_mode = True

default persistent.extra_001_locked = True

default persistent.end_lucy = False
default persistent.end_aya = False
default persistent.end_milena = False
default persistent.end_anna = False
default persistent.end_kyra = False
default persisten.end_lara = False
default persistent.end_lisa = False
default persistent.end_anastacia = False
default persistent.end_verdi = False
default persistent.end_ruzena = False
default persistent.end_laura = False
default persistent.end_tatiana = False
default persistent.end_kirk = False
default persistent.end_victoria = False
default persistent.end_mia = False
default persistent.end_tiffany = False
default persistent.end_mireia = False
default persistent.end_sarah = False
default persistent.verdi_house_ok = False
default persistent.verdi_replay_p1 = False
default persistent.verdi_replay_p2 = False
default persistent.lottery_replay = False

default persistent.sw_event_babes_beach_sharing_01 = False
default persistent.sw_event_babes_beach_sharing_02 = False
default persistent.sw_event_babes_beach_sharing_03 = False
default persistent.sw_event_babes_beach_solo_01 = False
default persistent.sw_event_babes_beach_solo_02 = False

default money = 250
default data = 1
default game_mode = 1
default map_mode = 1
default sort10 = renpy.random.randint(1,10)
default pub_moneycount = 0
default tipsort = 0
default lottery_day = 0

default harem_day = 0

default prob_anastacia = renpy.random.randint(1, 10)
default prob_aya = renpy.random.randint(1, 10)
default prob_lucy = renpy.random.randint(1, 10)
default prob_kyra = renpy.random.randint(1, 10)
default prob_tatiana = renpy.random.randint(1, 10)
default prob_lisa = renpy.random.randint(1, 10)
default prob_lara = renpy.random.randint(1, 10)
default prob_sabrina = renpy.random.randint(1, 10)
default prob_amanda = renpy.random.randint(1, 10)
default prob_miranda = renpy.random.randint(1, 10)
default prob_alexandra = renpy.random.randint(1, 10)
default prob_sarah = renpy.random.randint(1, 10)
default prob_alanna = renpy.random.randint(1, 10)
default prob_adele = renpy.random.randint(1, 10)
default prob_verdi = renpy.random.randint(1, 10)
default prob_tifa = renpy.random.randint(1, 10)
default prob_suki = renpy.random.randint(1, 10)
default prob_laura = renpy.random.randint(1, 10)


default invest = 0
default juros = 0
default money_before = 0
default library_count = 0
default gym_count = 0
default event_count = 0
default general_count = 0
default random_number = 0
default data_sarah_school_3 = 0
default anastacia_harem = 0
default date_points = 0
default date_ok = True
default date_kiss = False
default date_sex = False
default date_random = 0
default work_check = False
default nuclear_moneycount = 0
default nuclear_workcount = 0

default custom_pos = Position(xalign=0, yalign=0)

default kyra_sp1_trigger = 0

default lucy_sp2_trigger = 0

default lisa_sp1_trigger = 0

default saori_and_linda_trigger = 0

default tatiana_special_4_trigger = 0

default trigger_drone_emails = 0

default trigger_miranda_after_blowjob = 0

default minji_spank = 0
default minji_talk_count = 0

default sw_cena_noite = True



default talk_anastacia = False
default talk_kyra = False
default talk_aya = False
default talk_mirlisa = False
default random_event_switch = True
default switch_lottery = False
default switch_lottery_result = False
default switch_lottery_ban = False
default lottery_level_2 = False
default bank_talk = False
default ruz_talk = False
default ask_email_alexandra = False
default laura_school_3some = False
default mario_dronecam = False
default adele_fala_inicial = False
default adele_fala_continua = False
default stella_handjob = False
default comment_magazine = False
default mia_fala_inicial = False
default work_unlocked = False
default fala_victoria_inicial = False

default lara_level_1 = False
default event_lara_level_2 = False
default event_call_alexandra = False
default event_call_alexandra_2 = False
default event_photo_beach = False
default event_special_photo_alexandra_lucy = False
default event_call_alexandra_3 = False
default event_lara_magazine_1 = False
default event_lara_magazine_2 = False
default event_lara_dance = False
default sw_lara_dance_alex = False
default sw_lara_dance_kirk = False
default sw_lara_dance_3some = False
default sw_lara_dance_fuck_kirk = False
default sw_lara_dance_fuck_alex = False
default sw_lara_dance_vanilla_scene = False
default sw_lara_dance_01 = False
default sw_lara_dance_02 = False

default talk_lucy_1 = False
default event_lucy_1 = False
default event_lucy_2 = False
default event_lucy_3 = False
default event_lucy_4 = False
default event_lucy_sp_1 = False
default event_lucy_sp_2 = False
default event_lucy_sp_3 = False
default event_lucy_house = False
default event_lucy_ending = False
default event_smoke = False
default event_anna_ending = False
default date_lucy_alt = False
default date_milena_alt = False
default persistent.lucy_quick_sex = False
default event_lucy_sharing = False

default event_milena_house_1 = False
default event_milena_house_2 = False

default event_anastacia_1 = False
default event_anastacia_2 = False
default event_anastacia_special_1 = False
default event_anastacia_level_3 = False
default conversa_escolhe_anastacia = False
default event_anastacia_04 = False
default sw_anastacia_sex = False
default sw_fenella_sex = False
default event_anastacia_house_1 = False
default event_anastacia_house_2 = False
default sw_event_anastacia_house_2_01 = False
default sw_event_anastacia_house_2_02 = False
default sw_event_anastacia_house_2_03 = False
default sw_event_anastacia_house_2_04 = False
default sw_event_anastacia_house_2_05 = False
default sw_event_anastacia_house_2_06 = False
default sw_event_anastacia_house_2_07 = False
default sw_event_anastacia_house_2_drink = 0
default sw_event_anastacia_house_2_talk_count = 0
default sw_anastacia_end_talk_1 = False
default sw_anastacia_end_talk_2 = False
default sw_anastacia_end_talk_3 = False
default sw_anastacia_end_ana_bed = False
default sw_anastacia_end_fen_bed = False
default sw_anastacia_end_don_bed = False
default sw_anastacia_end_cum_ana = False
default sw_anastacia_end_cum_fen = False
default sw_anastacia_end_cum_don = False
default event_anastacia_ending = False

default event_kyra_1 = False
default event_kyra_sp_1 = False
default event_kyra_2 = False
default event_kyra_level_3 = False
default event_stella_market = False
default event_stella_visit_2 = False
default event_stella_visit_wine = False
default event_kyra_bukkake = False
default event_kyra_level_4 = False
default event_kyra_house_1 = False
default event_kyra_house_2 = False
default stella_option_1 = False
default stella_option_2 = False
default event_stella_market_2 = False
default event_date_gianna = False
default sw_date_gianna_1 = False
default sw_date_gianna_talk = 0
default sw_date_gianna_2 = False

default event_aya_1 = False
default event_aya_2 = False
default event_aya_special_1 = False
default event_aya_level_3 = False
default event_aya_level_4 = False
default event_aya_house = False
default event_aya_house_2 = False
default event_aya_end = False

default event_tatiana_sp_1 = False
default event_tatiana_sp_2 = False
default event_tatiana_sp_3 = False
default event_tatiana_1 = False
default event_tatiana_2 = False
default event_tatiana_3 = False
default event_tatiana_special_4 = False
default event_tatiana_remake_01 = False
default event_tatiana_remake_02 = False
default event_tatiana_remake_03 = False
default event_tatiana_remake_04 = False
default event_tatiana_remake_05 = False
default event_tatiana_remake_06 = False
default sw_tatiana_ending_01 = False
default event_tatiana_ending = False

default event_sarah_school = False
default event_saori_and_sarah = False
default event_sarah_school_2 = False
default event_sarah_school_3 = False
default event_call_sarah = False
default event_mixed_bath = False
default event_mireia_minji_1 = False
default event_call_minji = False
default sw_minji_talk_1 = False
default event_sarah_sex = False
default event_sarah_house = False
default sw_sarah_house_01 = False
default event_sarah_phone = False
default sw_sarah_phone_01 = False
default sw_sarah_phone_02 = False
default sw_sarah_phone_03 = False
default sw_sarah_phone_random = renpy.random.randint(1, 10)
default sw_sarah_phone_04 = 0
default event_sarah_friends_beach = False
default sw_sarah_friends_beach_01 = False
default sw_sarah_friends_beach_02 = False
default event_sarah_friends_beach_repeat = False
default sw_sarah_friends_beach_repeat_01 = False
default sw_sarah_friends_beach_repeat_02 = False
default sw_sarah_friends_beach_repeat_03 = False
default sw_sarah_friends_beach_repeat_04 = False
default event_mireia_mini_ending = False
default event_sarah_sharing = False
default sw_sarah_sharing_01 = 0
default event_sarah_ending = False

default event_laura_house_1 = False
default event_laura_house_2 = False
default event_laura_house_3 = False
default event_call_linda = False
default event_saori_and_linda = False
default event_laura_school = False
default sw_event_laura_2_01 = False
default sw_event_laura_2_02 = False
default sw_event_laura_2_03 = False
default sw_event_laura_2_04 = False
default sw_event_laura_house_3_cum_lisa = False
default sw_event_laura_house_3_cum_marian = False
default sw_event_laura_house_3_cum_laura = False
default sw_laura_house_3_1 = False
default sw_laura_house_3_2 = False
default sw_laura_house_3_3 = False
default sw_laura_house_3_4 = False
default sw_laura_house_3_5 = False
default sw_laura_house_3_6 = False
default sw_laura_house_3_7 = False
default sw_laura_house_3_8 = False
default sw_laura_house_3_9 = False
default event_linda_house_01 = False
default event_linda_house_02 = False
default event_orgy = False
default event_laura_ending = False

default event_call_maid = False

default event_lisa_1 = False
default event_lisa_special_1 = False
default talk_lisa_1 = False
default event_lisa_special_2 = False
default lisa_dont_explain = False
default event_marian_01 = False
default event_lisa_level_2 = False
default sw_lisa_lucy = False
default sw_monica_studio = False
default sw_alanna_studio = False
default event_lisa_level_3 = False
default event_lisa_level_4 = False
default event_lisa_special_3 = False
default event_lisa_phone = False
default event_lisa_phone_talk_count = 0
default event_lisa_phone_sex_count = 0
default event_lisa_phone_sex_random = renpy.random.randint(1, 4)
default event_lisa_phone_sex_same = 0

default event_gym_girl = False
default event_amanda_2 = False
default event_amanda_3 = False

default event_mary_1 = False
default event_mary_2 = False
default sw_mary_2_01 = False
default sw_mary_2_02 = False
default sw_mary_2_03 = False

default event_alanna_01 = False
default event_alanna_02 = False
default sw_alanna_sex = False

default sw_monica_sex = False
default event_monica_01 = False

default event_miranda_level_1 = False
default event_miranda_special_1 = False
default event_miranda_level_2 = False
default event_miranda_special_2 = False
default event_miranda_level_3 = False
default event_aurora_club = False
default event_adria_1 = False
default miranda_pedido = False
default miranda_pedido_2 = False
default adria_pergunta = False
default adria_talk_1 = False
default adria_talk_2 = False
default adria_fala_livros = False
default give_book_1 = False
default give_book_2 = False
default adria_pede_anitta = False
default event_adele_anitta = False
default event_aurora_1 = False
default aurora_opcao_1 = False
default aurora_opcao_2 = False
default aurora_opcao_3 = False
default aurora_opcao_count = 0
default event_miranda_special_3 = False
default sw_adele_ask = False
default event_miranda_special_4 = False
default event_adria_2 = False
default event_miranda_special_5 = False
default event_miranda_level_4 = False
default event_miranda_house = False
default event_miranda_house_opt_miranda_1 = False
default event_miranda_house_opt_miranda_2 = False
default event_miranda_house_opt_miranda_blank_1 = False
default event_miranda_house_opt_miranda_blank_2 = False
default event_miranda_house_opt_aurora_1 = False
default event_miranda_house_opt_aurora_2 = False
default event_miranda_house_opt_aurora_blank_1 = False
default event_miranda_house_opt_aurora_blank_2 = False
default event_miranda_house_opt_adria_1 = False
default event_miranda_house_opt_adria_2 = False
default event_miranda_house_opt_adria_blank_1 = False
default event_miranda_house_opt_adria_blank_2 = False
default event_miranda_house_mouth_fuck = 0
default event_miranda_house_random_3 = 0
default event_miranda_special_6 = False
default event_miranda_phone = False
default event_miranda_phone_2 = False
default sw_game_lucy_hp = 3
default sw_game_miranda_hp = 3
default sw_game_tatiana_hp = 3
default sw_game_milena_hp = 3
default sw_game_alex_hp = 3
default sw_game_person_a = 0
default sw_game_person_b = 0
default sw_game_01 = False
default sw_game_02 = False
default sw_game_03 = False
default sw_game_04 = False
default sw_game_05 = False
default sw_game_06 = False
default sw_game_07 = False
default sw_game_08 = False
default sw_game_09 = False
default sw_game_10 = False
default sw_game_alex_lost = False
default sw_game_miranda_lost = False
default sw_game_milena_lost = False
default sw_game_tatiana_lost = False
default sw_game_lucy_lost = False

default event_tiffany_01 = False
default event_tiffany_02 = False
default sw_event_tifa_02_1 = False
default sw_event_tifa_02_2 = False
default sw_event_tifa_02_3 = False
default event_tiffany_mini_ending = False
default sw_tiffany_mini_ending_01 = False
default sw_tiffany_mini_ending_02 = False
default sw_tiffany_mini_ending_03 = False
default sw_tiffany_mini_ending_04 = False

default event_twins_01 = False

default event_adele_1 = False
default event_adele_sex = False
default adele_sex_mast = False
default adele_sex_oral = False
default adele_sex_penetration = False
default adele_sex_girl = False
default adele_sex_boy = False
default sw_adele_sex_first = False
default sw_adele_001 = False
default sw_adele_002 = False

default event_ruzena_1 = False
default event_ruzena_2 = False
default event_ruzena_3 = False
default event_ruzena_4 = False
default event_shibuya_1 = False
default event_shibuya_2 = False
default event_shibuya_3 = False
default event_shibuya_4 = False
default sw_shibuya_4_1 = False
default event_shibuya_5 = False
default event_ruzena_5 = False
default event_ruzena_end = False
default sw_ruzena_end_1 = False
default sw_ruzena_end_2 = False

default event_victoria_massage = False
default event_victoria_sex = False
default sw_victoria_speak = False
default event_victoria_sex_again = False
default event_victoria_mini_ending = False

default event_nuclear_intro = False
default event_verdi_level_1 = False
default event_verdi_level_2 = False
default event_verdi_level_3 = False
default event_verdi_house = False
default sw_verdi_house_first = False
default sw_verdi_house_alexandra = False
default sw_verdi_sex_1 = False
default sw_verdi_sex_2 = False
default sw_verdi_sex_3 = False
default sw_verdi_house_sex_count = 0
default sw_verdi_house_hardcore = False
default event_verdi_level_5 = False
default sw_verdi_alt_hc = False
default sw_verdi_extra_fv = False
default sw_verdi_extra_fa = False
default event_verdi_ending = False

default event_emma_01 = False
default event_emma_02 = False
default event_emma_03 = False
default event_emma_04_solo = False
default event_emma_04_sharing = False

default event_suki_01 = False
default sw_suki_01_1 = False
default event_suki_02 = False
default sw_suki_02_1 = False
default sw_suki_02_2 = False
default event_suki_03 = False
default event_suki_03_alone = False
default event_suki_03_floyd = False

default event_nikky_1 = False
default sw_lottery_end = False

default event_mia_01 = False
default event_mia_02 = False
default sw_mia_02_count = 0
default event_mia_03 = False
default event_mia_mini_ending = False

default event_kirk_ending = False
default sw_kirk_ending_01 = False
default sw_kirk_ending_02 = False
default sw_kirk_ending_03 = False
default sw_kirk_ending_04 = False
default event_sexclub = False

default event_babes_beach_sharing = False
default heart_beach_lara_sh = False
default heart_beach_miranda_sh = False
default heart_beach_mothers_sh = False

default heart_beach_lara_solo = False
default heart_beach_miranda_solo = False

default harem_end_recruit_kyra = False
default harem_end_recruit_maids = False
default harem_end_recruit_miranda = False

default harem_start = False
default harem_end_train_kyra = False
default harem_end_fun_kyra = False
default train_kyra_conv_1 = False
default train_kyra_conv_2 = False
default train_kyra_conv_3 = False
default train_kyra_conv_4 = False
default train_kyra_conv_5 = False
default train_kyra_conv_6 = False
default train_kyra_conv_7 = False
default train_kyra_post_conv_1 = False
default train_kyra_post_conv_2 = False
default train_kyra_post_conv_3 = False
default train_kyra_post_conv_4 = False
default train_kyra_post_conv_5 = False
default train_kyra_post_conv_6 = False
default train_kyra_comp_1 = False
default train_kyra_comp_2 = False
default train_kyra_comp_3 = False
default train_kyra_comp_4 = False
default train_kyra_comp_5 = False
default train_kyra_comp_6 = False

default harem_end_special_miranda = False




default item_enciclopedia = False
default item_gymbook = False
default item_workbook = False
default item_waiterclothes = False
default item_waitergloves = False
default item_luckamulet = False
default item_watch = False
default item_glasses = False
default item_boots = False
default item_shirt = False
default item_pants = False
default item_jacket = False



default item_library_card = False
default item_gym_card = False

default item_cheap_wine = False
default item_expensive_wine = False
default item_vodka = False
default item_beerpack = False
default item_whiskey = False
default item_aphrodisiac = False

default item_magazine_lara = False

default item_book_1 = False
default item_book_2 = False
default item_book_3 = False



image a001a = Movie(play="animations/a001a.avi", pos=(0,0), anchor=(0,0))
image a001b = Movie(play="animations/a001b.avi", pos=(0,0), anchor=(0,0))
image a001c = Movie(play="animations/a001c.avi", pos=(0,0), anchor=(0,0))
image a002a = Movie(play="animations/a002a.avi", pos=(0,0), anchor=(0,0))
image a003a = Movie(play="animations/a003a.avi", pos=(0,0), anchor=(0,0))
image a004a = Movie(play="animations/a004a.avi", pos=(0,0), anchor=(0,0))
image a004b = Movie(play="animations/a004b.avi", pos=(0,0), anchor=(0,0))
image a004c = Movie(play="animations/a004c.avi", pos=(0,0), anchor=(0,0))
image a004d = Movie(play="animations/a004d.avi", pos=(0,0), anchor=(0,0))
image a004e = Movie(play="animations/a004e.avi", pos=(0,0), anchor=(0,0))
image 17_01_din = Movie(play="animations/17_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 17_02_din = Movie(play="animations/17_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 17_03_din = Movie(play="animations/17_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_01_din = Movie(play="animations/37_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_02_din = Movie(play="animations/37_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_03_din = Movie(play="animations/37_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_04_din = Movie(play="animations/37_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_05_din = Movie(play="animations/37_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_06_din = Movie(play="animations/37_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_07_din = Movie(play="animations/37_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_08_din = Movie(play="animations/37_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 37_09_din = Movie(play="animations/37_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_10_din = Movie(play="animations/37_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_11_din = Movie(play="animations/37_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_12_din = Movie(play="animations/37_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_13_din = Movie(play="animations/37_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 37_14_din = Movie(play="animations/37_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 42_01_din = Movie(play="animations/42_01_din.avi", pos=(0,0), anchor=(0,0))
image 42_02_din = Movie(play="animations/42_02_din.avi", pos=(0,0), anchor=(0,0))
image 42_03_din = Movie(play="animations/42_03_din.avi", pos=(0,0), anchor=(0,0))
image 42_04_din = Movie(play="animations/42_04_din.avi", pos=(0,0), anchor=(0,0))
image 42_05_din = Movie(play="animations/42_05_din.avi", pos=(0,0), anchor=(0,0))
image 44_01_din = Movie(play="animations/44_01_din.avi", pos=(0,0), anchor=(0,0))
image 46_05_din = Movie(play="animations/46_05_din.avi", pos=(0,0), anchor=(0,0))
image 46_06_din = Movie(play="animations/46_06_din.avi", pos=(0,0), anchor=(0,0))
image 48_01_din = Movie(play="animations/48_01_din.avi", pos=(0,0), anchor=(0,0))
image 48_02_din = Movie(play="animations/48_02_din.avi", pos=(0,0), anchor=(0,0))
image 56_01_din = Movie(play="animations/56_01_din.avi", pos=(0,0), anchor=(0,0))
image 57_01_din = Movie(play="animations/57_01_din.avi", pos=(0,0), anchor=(0,0))
image 59_05_din = Movie(play="animations/59_05_din.avi", pos=(0,0), anchor=(0,0))
image 59_06_din = Movie(play="animations/59_06_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_01_din = Movie(play="animations/d_lucy_01_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_02_din = Movie(play="animations/d_lucy_02_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_03_din = Movie(play="animations/d_lucy_03_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_04_din = Movie(play="animations/d_lucy_04_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_05_din = Movie(play="animations/d_lucy_05_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_06_din = Movie(play="animations/d_lucy_06_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_07_din = Movie(play="animations/d_lucy_07_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_08_din = Movie(play="animations/d_lucy_08_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_09_din = Movie(play="animations/d_lucy_09_din.avi", pos=(0,0), anchor=(0,0))
image d_lucy_10_din = Movie(play="animations/d_lucy_10_din.avi", pos=(0,0), anchor=(0,0))
image 63_01_din = Movie(play="animations/63_01_din.avi", pos=(0,0), anchor=(0,0))
image 63_02_din = Movie(play="animations/63_02_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_01_din = Movie(play="animations/d_milena_01_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_02_din = Movie(play="animations/d_milena_02_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_03_din = Movie(play="animations/d_milena_03_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_04_din = Movie(play="animations/d_milena_04_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_05_din = Movie(play="animations/d_milena_05_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_06_din = Movie(play="animations/d_milena_06_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_07_din = Movie(play="animations/d_milena_07_din.avi", pos=(0,0), anchor=(0,0))
image d_milena_08_din = Movie(play="animations/d_milena_08_din.avi", pos=(0,0), anchor=(0,0))
image 73_01_din = Movie(play="animations/73_01_din.avi", pos=(0,0), anchor=(0,0))
image 77_01_din = Movie(play="animations/77_01_din.avi", pos=(0,0), anchor=(0,0))
image 77_02_din = Movie(play="animations/77_02_din.avi", pos=(0,0), anchor=(0,0))
image 79_01_din = Movie(play="animations/79_01_din.avi", pos=(0,0), anchor=(0,0))
image 79_02_din = Movie(play="animations/79_02_din.avi", pos=(0,0), anchor=(0,0))
image 79_03_din = Movie(play="animations/79_03_din.avi", pos=(0,0), anchor=(0,0))
image 79_04_din = Movie(play="animations/79_04_din.avi", pos=(0,0), anchor=(0,0))
image 79_05_din = Movie(play="animations/79_05_din.avi", pos=(0,0), anchor=(0,0))
image 79_06_din = Movie(play="animations/79_06_din.avi", pos=(0,0), anchor=(0,0))
image 82_01_din = Movie(play="animations/82_01_din.avi", pos=(0,0), anchor=(0,0))
image 82_02_din = Movie(play="animations/82_02_din.avi", pos=(0,0), anchor=(0,0))
image 82_03_din = Movie(play="animations/82_03_din.avi", pos=(0,0), anchor=(0,0))
image 82_04_din = Movie(play="animations/82_04_din.avi", pos=(0,0), anchor=(0,0))
image 87_01_din = Movie(play="animations/87_01_din.avi", pos=(0,0), anchor=(0,0))
image 87_02_din = Movie(play="animations/87_02_din.avi", pos=(0,0), anchor=(0,0))
image 83_01_din = Movie(play="animations/83_01_din.avi", pos=(0,0), anchor=(0,0))
image 83_02_din = Movie(play="animations/83_02_din.avi", pos=(0,0), anchor=(0,0))
image 83_03_din = Movie(play="animations/83_03_din.avi", pos=(0,0), anchor=(0,0))
image 83_04_din = Movie(play="animations/83_04_din.avi", pos=(0,0), anchor=(0,0))
image 83_05_din = Movie(play="animations/83_05_din.avi", pos=(0,0), anchor=(0,0))
image 83_06_din = Movie(play="animations/83_06_din.avi", pos=(0,0), anchor=(0,0))
image 90_05_din = Movie(play="animations/90_05_din.avi", pos=(0,0), anchor=(0,0))
image 91_01_din = Movie(play="animations/91_01_din.avi", pos=(0,0), anchor=(0,0))
image 91_02_din = Movie(play="animations/91_02_din.avi", pos=(0,0), anchor=(0,0))
image 92_01_din = Movie(play="animations/92_01_din.avi", pos=(0,0), anchor=(0,0))
image 92_02_din = Movie(play="animations/92_02_din.avi", pos=(0,0), anchor=(0,0))
image 92_03_din = Movie(play="animations/92_03_din.avi", pos=(0,0), anchor=(0,0))
image 92_07_din = Movie(play="animations/92_07_din.avi", pos=(0,0), anchor=(0,0))
image 92_08_din = Movie(play="animations/92_08_din.avi", pos=(0,0), anchor=(0,0))
image 93_01_din = Movie(play="animations/93_01_din.avi", pos=(0,0), anchor=(0,0))
image 94_01_din = Movie(play="animations/94_01_din.avi", pos=(0,0), anchor=(0,0))
image 94_02_din = Movie(play="animations/94_02_din.avi", pos=(0,0), anchor=(0,0))
image 94_03_din = Movie(play="animations/94_03_din.avi", pos=(0,0), anchor=(0,0))
image 94_04_din = Movie(play="animations/94_04_din.avi", pos=(0,0), anchor=(0,0))
image 94_05_din = Movie(play="animations/94_05_din.avi", pos=(0,0), anchor=(0,0))
image 94_06_din = Movie(play="animations/94_06_din.avi", pos=(0,0), anchor=(0,0))
image 94_07_din = Movie(play="animations/94_07_din.avi", pos=(0,0), anchor=(0,0))
image 94_08_din = Movie(play="animations/94_08_din.avi", pos=(0,0), anchor=(0,0))
image 95_02_din = Movie(play="animations/95_02_din.avi", pos=(0,0), anchor=(0,0))
image 96_06_din = Movie(play="animations/96_06_din.avi", pos=(0,0), anchor=(0,0))
image 97_01_din = Movie(play="animations/97_01_din.avi", pos=(0,0), anchor=(0,0))
image 102_01_din = Movie(play="animations/102_01_din.avi", pos=(0,0), anchor=(0,0))
image 102_02_din = Movie(play="animations/102_02_din.avi", pos=(0,0), anchor=(0,0))
image 102_03_din = Movie(play="animations/102_03_din.avi", pos=(0,0), anchor=(0,0))
image 102_04_din = Movie(play="animations/102_04_din.avi", pos=(0,0), anchor=(0,0))
image 104_01_din = Movie(play="animations/104_01_din.avi", pos=(0,0), anchor=(0,0))
image 104_02_din = Movie(play="animations/104_02_din.avi", pos=(0,0), anchor=(0,0))
image 104_03_din = Movie(play="animations/104_03_din.avi", pos=(0,0), anchor=(0,0))
image 104_04_din = Movie(play="animations/104_04_din.avi", pos=(0,0), anchor=(0,0))
image 104_05_din = Movie(play="animations/104_05_din.avi", pos=(0,0), anchor=(0,0))
image 104_06_din = Movie(play="animations/104_06_din.avi", pos=(0,0), anchor=(0,0))
image 104_07_din = Movie(play="animations/104_07_din.avi", pos=(0,0), anchor=(0,0))
image 104_08_din = Movie(play="animations/104_08_din.avi", pos=(0,0), anchor=(0,0))
image 104_09_din = Movie(play="animations/104_09_din.avi", pos=(0,0), anchor=(0,0))
image 105_01_din = Movie(play="animations/105_01_din.avi", pos=(0,0), anchor=(0,0))
image 105_02_din = Movie(play="animations/105_02_din.avi", pos=(0,0), anchor=(0,0))
image 105_03_din = Movie(play="animations/105_03_din.avi", pos=(0,0), anchor=(0,0))
image 105_04_din = Movie(play="animations/105_04_din.avi", pos=(0,0), anchor=(0,0))
image 110_01_din = Movie(play="animations/110_01_din.webm", pos=(0,0), anchor=(0,0))
image 110_02_din = Movie(play="animations/110_02_din.webm", pos=(0,0), anchor=(0,0))
image 110_03_din = Movie(play="animations/110_03_din.webm", pos=(0,0), anchor=(0,0))
image 114_01_din = Movie(play="animations/114_01_din.webm", pos=(0,0), anchor=(0,0))
image 114_02_din = Movie(play="animations/114_02_din.webm", pos=(0,0), anchor=(0,0))
image 114_03_din = Movie(play="animations/114_03_din.webm", pos=(0,0), anchor=(0,0))
image 114_04_din = Movie(play="animations/114_04_din.webm", pos=(0,0), anchor=(0,0))
image 114_05_din = Movie(play="animations/114_05_din.webm", pos=(0,0), anchor=(0,0))
image 114_06_din = Movie(play="animations/114_06_din.webm", pos=(0,0), anchor=(0,0))
image 114_07_din = Movie(play="animations/114_07_din.webm", pos=(0,0), anchor=(0,0))
image 115_01_din = Movie(play="animations/115_01_din.webm", pos=(0,0), anchor=(0,0))
image 115_02_din = Movie(play="animations/115_02_din.webm", pos=(0,0), anchor=(0,0))
image 115_03_din = Movie(play="animations/115_03_din.webm", pos=(0,0), anchor=(0,0))
image 115_17_din = Movie(play="animations/115_17_din.webm", pos=(0,0), anchor=(0,0))
image 118_01_din = Movie(play="animations/118_01_din.webm", pos=(0,0), anchor=(0,0))
image 118_02_din = Movie(play="animations/118_02_din.webm", pos=(0,0), anchor=(0,0))
image 118_03_din = Movie(play="animations/118_03_din.webm", pos=(0,0), anchor=(0,0))
image 118_04_din = Movie(play="animations/118_04_din.webm", pos=(0,0), anchor=(0,0))
image 118_05_din = Movie(play="animations/118_05_din.webm", pos=(0,0), anchor=(0,0))
image 118_06_din = Movie(play="animations/118_06_din.webm", pos=(0,0), anchor=(0,0))
image 118_07_din = Movie(play="animations/118_07_din.webm", pos=(0,0), anchor=(0,0))
image 118_08_din = Movie(play="animations/118_08_din.webm", pos=(0,0), anchor=(0,0))
image 118_09_din = Movie(play="animations/118_09_din.webm", pos=(0,0), anchor=(0,0))
image 118_10_din = Movie(play="animations/118_10_din.webm", pos=(0,0), anchor=(0,0))
image 118_11_din = Movie(play="animations/118_11_din.webm", pos=(0,0), anchor=(0,0))
image 118_12_din = Movie(play="animations/118_12_din.webm", pos=(0,0), anchor=(0,0))
image 118_13_din = Movie(play="animations/118_13_din.webm", pos=(0,0), anchor=(0,0))
image 120_01_din = Movie(play="animations/120_01_din.webm", pos=(0,0), anchor=(0,0))
image 120_02_din = Movie(play="animations/120_02_din.webm", pos=(0,0), anchor=(0,0))
image 120_03_din = Movie(play="animations/120_03_din.webm", pos=(0,0), anchor=(0,0))
image 120_04_din = Movie(play="animations/120_04_din.webm", pos=(0,0), anchor=(0,0))
image 120_05_din = Movie(play="animations/120_05_din.webm", pos=(0,0), anchor=(0,0))
image 120_06_din = Movie(play="animations/120_06_din.webm", pos=(0,0), anchor=(0,0))
image 122_01_din = Movie(play="animations/122_01_din.webm", pos=(0,0), anchor=(0,0))
image 123_01_din = Movie(play="animations/123_01_din.webm", pos=(0,0), anchor=(0,0))
image 123_02_din = Movie(play="animations/123_02_din.webm", pos=(0,0), anchor=(0,0))
image 123_03_din = Movie(play="animations/123_03_din.webm", pos=(0,0), anchor=(0,0))
image 123_04_din = Movie(play="animations/123_04_din.webm", pos=(0,0), anchor=(0,0))
image 124_01_din = Movie(play="animations/124_01_din.webm", pos=(0,0), anchor=(0,0))
image 124_02_din = Movie(play="animations/124_02_din.webm", pos=(0,0), anchor=(0,0))
image 124_03_din = Movie(play="animations/124_03_din.webm", pos=(0,0), anchor=(0,0))
image 124_04_din = Movie(play="animations/124_04_din.webm", pos=(0,0), anchor=(0,0))
image 124_05_din = Movie(play="animations/124_05_din.webm", pos=(0,0), anchor=(0,0))
image 125_01_din = Movie(play="animations/125_01_din.webm", pos=(0,0), anchor=(0,0))
image 125_05_din = Movie(play="animations/125_05_din.webm", pos=(0,0), anchor=(0,0))
image 125_06_din = Movie(play="animations/125_06_din.webm", pos=(0,0), anchor=(0,0))
image 126_01_din = Movie(play="animations/126_01_din.webm", pos=(0,0), anchor=(0,0))
image 127_01_din = Movie(play="animations/127_01_din.webm", pos=(0,0), anchor=(0,0))
image 127_02_din = Movie(play="animations/127_02_din.webm", pos=(0,0), anchor=(0,0))
image 127_03_din = Movie(play="animations/127_03_din.webm", pos=(0,0), anchor=(0,0))
image 127_04_din = Movie(play="animations/127_04_din.webm", pos=(0,0), anchor=(0,0))
image 127_05_din = Movie(play="animations/127_05_din.webm", pos=(0,0), anchor=(0,0))
image 127_06_din = Movie(play="animations/127_06_din.webm", pos=(0,0), anchor=(0,0))
image 127_07_din = Movie(play="animations/127_07_din.webm", pos=(0,0), anchor=(0,0))
image 127_09_din = Movie(play="animations/127_09_din.webm", pos=(0,0), anchor=(0,0))
image 127_10_din = Movie(play="animations/127_10_din.webm", pos=(0,0), anchor=(0,0))
image 127_11_din = Movie(play="animations/127_11_din.webm", pos=(0,0), anchor=(0,0))
image 127_12_din = Movie(play="animations/127_12_din.webm", pos=(0,0), anchor=(0,0))
image 127_13_din = Movie(play="animations/127_13_din.webm", pos=(0,0), anchor=(0,0))
image 127_15_din = Movie(play="animations/127_15_din.webm", pos=(0,0), anchor=(0,0))
image 127_16_din = Movie(play="animations/127_16_din.webm", pos=(0,0), anchor=(0,0))
image 127_17_din = Movie(play="animations/127_17_din.webm", pos=(0,0), anchor=(0,0))
image 127_18_din = Movie(play="animations/127_18_din.webm", pos=(0,0), anchor=(0,0))
image 127_19_din = Movie(play="animations/127_19_din.webm", pos=(0,0), anchor=(0,0))
image 127_20_din = Movie(play="animations/127_20_din.webm", pos=(0,0), anchor=(0,0))
image 128_01_din = Movie(play="animations/128_01_din.webm", pos=(0,0), anchor=(0,0))
image 128_02_din = Movie(play="animations/128_02_din.webm", pos=(0,0), anchor=(0,0))
image 128_03_din = Movie(play="animations/128_03_din.webm", pos=(0,0), anchor=(0,0))
image 128_04_din = Movie(play="animations/128_04_din.webm", pos=(0,0), anchor=(0,0))
image 128_05_din = Movie(play="animations/128_05_din.webm", pos=(0,0), anchor=(0,0))
image 128_06_din = Movie(play="animations/128_06_din.webm", pos=(0,0), anchor=(0,0))
image 128_07_din = Movie(play="animations/128_07_din.webm", pos=(0,0), anchor=(0,0))
image 128_08_din = Movie(play="animations/128_08_din.webm", pos=(0,0), anchor=(0,0))
image 128_09_din = Movie(play="animations/128_09_din.webm", pos=(0,0), anchor=(0,0))
image 128_11_din = Movie(play="animations/128_11_din.webm", pos=(0,0), anchor=(0,0))
image 129_01_din = Movie(play="animations/129_01_din.webm", pos=(0,0), anchor=(0,0))
image 129_02_din = Movie(play="animations/129_02_din.webm", pos=(0,0), anchor=(0,0))
image 129_03_din = Movie(play="animations/129_03_din.webm", pos=(0,0), anchor=(0,0))
image 129_04_din = Movie(play="animations/129_04_din.webm", pos=(0,0), anchor=(0,0))
image 129_05_din = Movie(play="animations/129_05_din.webm", pos=(0,0), anchor=(0,0))
image 129_06_din = Movie(play="animations/129_06_din.webm", pos=(0,0), anchor=(0,0))
image 129_07_din = Movie(play="animations/129_07_din.webm", pos=(0,0), anchor=(0,0))
image 129_08_din = Movie(play="animations/129_08_din.webm", pos=(0,0), anchor=(0,0))
image 129_09_din = Movie(play="animations/129_09_din.webm", pos=(0,0), anchor=(0,0))
image 129_11_din = Movie(play="animations/129_11_din.webm", pos=(0,0), anchor=(0,0))
image 129_12_din = Movie(play="animations/129_12_din.webm", pos=(0,0), anchor=(0,0))
image 129_13_din = Movie(play="animations/129_13_din.webm", pos=(0,0), anchor=(0,0))
image 129_15_din = Movie(play="animations/129_15_din.webm", pos=(0,0), anchor=(0,0))
image 129_16_din = Movie(play="animations/129_16_din.webm", pos=(0,0), anchor=(0,0))
image 129_17_din = Movie(play="animations/129_17_din.webm", pos=(0,0), anchor=(0,0))
image 129_18_din = Movie(play="animations/129_18_din.webm", pos=(0,0), anchor=(0,0))
image 129_19_din = Movie(play="animations/129_19_din.webm", pos=(0,0), anchor=(0,0))
image 129_20_din = Movie(play="animations/129_20_din.webm", pos=(0,0), anchor=(0,0))
image 129_22_din = Movie(play="animations/129_22_din.webm", pos=(0,0), anchor=(0,0))
image 129_23_din = Movie(play="animations/129_23_din.webm", pos=(0,0), anchor=(0,0))
image 129_24_din = Movie(play="animations/129_24_din.webm", pos=(0,0), anchor=(0,0))
image 129_26_din = Movie(play="animations/129_26_din.webm", pos=(0,0), anchor=(0,0))
image 129_27_din = Movie(play="animations/129_27_din.webm", pos=(0,0), anchor=(0,0))
image 129_28_din = Movie(play="animations/129_28_din.webm", pos=(0,0), anchor=(0,0))
image 129_29_din = Movie(play="animations/129_29_din.webm", pos=(0,0), anchor=(0,0))
image 129_30_din = Movie(play="animations/129_30_din.webm", pos=(0,0), anchor=(0,0))
image 129_31_din = Movie(play="animations/129_31_din.webm", pos=(0,0), anchor=(0,0))
image 129_33_din = Movie(play="animations/129_33_din.webm", pos=(0,0), anchor=(0,0))
image 129_34_din = Movie(play="animations/129_34_din.webm", pos=(0,0), anchor=(0,0))
image 129_35_din = Movie(play="animations/129_35_din.webm", pos=(0,0), anchor=(0,0))
image 129_37_din = Movie(play="animations/129_37_din.webm", pos=(0,0), anchor=(0,0))
image 129_38_din = Movie(play="animations/129_38_din.webm", pos=(0,0), anchor=(0,0))
image 129_39_din = Movie(play="animations/129_39_din.webm", pos=(0,0), anchor=(0,0))
image 129_40_din = Movie(play="animations/129_40_din.webm", pos=(0,0), anchor=(0,0))
image 129_41_din = Movie(play="animations/129_41_din.webm", pos=(0,0), anchor=(0,0))
image 129_42_din = Movie(play="animations/129_42_din.webm", pos=(0,0), anchor=(0,0))
image 129_43_din = Movie(play="animations/129_43_din.webm", pos=(0,0), anchor=(0,0))
image 129_44_din = Movie(play="animations/129_44_din.webm", pos=(0,0), anchor=(0,0))
image 129_46_din = Movie(play="animations/129_46_din.webm", pos=(0,0), anchor=(0,0))
image 129_47_din = Movie(play="animations/129_47_din.webm", pos=(0,0), anchor=(0,0))
image 129_49_din = Movie(play="animations/129_49_din.webm", pos=(0,0), anchor=(0,0))
image 129_50_din = Movie(play="animations/129_50_din.webm", pos=(0,0), anchor=(0,0))
image 129_51_din = Movie(play="animations/129_51_din.webm", pos=(0,0), anchor=(0,0))
image 129_52_din = Movie(play="animations/129_52_din.webm", pos=(0,0), anchor=(0,0))
image 129_53_din = Movie(play="animations/129_53_din.webm", pos=(0,0), anchor=(0,0))
image 129_54_din = Movie(play="animations/129_54_din.webm", pos=(0,0), anchor=(0,0))
image 129_55_din = Movie(play="animations/129_55_din.webm", pos=(0,0), anchor=(0,0))
image 129_56_din = Movie(play="animations/129_56_din.webm", pos=(0,0), anchor=(0,0))
image 130_01_din = Movie(play="animations/130_01_din.webm", pos=(0,0), anchor=(0,0))
image 130_02_din = Movie(play="animations/130_02_din.webm", pos=(0,0), anchor=(0,0))
image 130_03_din = Movie(play="animations/130_03_din.webm", pos=(0,0), anchor=(0,0))
image 130_04_din = Movie(play="animations/130_04_din.webm", pos=(0,0), anchor=(0,0))
image 130_05_din = Movie(play="animations/130_05_din.webm", pos=(0,0), anchor=(0,0))
image 130_06_din = Movie(play="animations/130_06_din.webm", pos=(0,0), anchor=(0,0))
image 130_08_din = Movie(play="animations/130_08_din.webm", pos=(0,0), anchor=(0,0))
image 130_09_din = Movie(play="animations/130_09_din.webm", pos=(0,0), anchor=(0,0))
image 131_01_din = Movie(play="animations/131_01_din.webm", pos=(0,0), anchor=(0,0))
image 131_02_din = Movie(play="animations/131_02_din.webm", pos=(0,0), anchor=(0,0))
image 131_03_din = Movie(play="animations/131_03_din.webm", pos=(0,0), anchor=(0,0))
image 131_04_din = Movie(play="animations/131_04_din.webm", pos=(0,0), anchor=(0,0))
image 131_06_din = Movie(play="animations/131_06_din.webm", pos=(0,0), anchor=(0,0))
image 131_07_din = Movie(play="animations/131_07_din.webm", pos=(0,0), anchor=(0,0))
image 131_08_din = Movie(play="animations/131_08_din.webm", pos=(0,0), anchor=(0,0))
image 131_09_din = Movie(play="animations/131_09_din.webm", pos=(0,0), anchor=(0,0))
image 131_10_din = Movie(play="animations/131_10_din.webm", pos=(0,0), anchor=(0,0))
image 131_11_din = Movie(play="animations/131_11_din.webm", pos=(0,0), anchor=(0,0))
image 131_12_din = Movie(play="animations/131_12_din.webm", pos=(0,0), anchor=(0,0))
image 132_01_din = Movie(play="animations/132_01_din.webm", pos=(0,0), anchor=(0,0))
image 132_02_din = Movie(play="animations/132_02_din.webm", pos=(0,0), anchor=(0,0))
image 132_03_din = Movie(play="animations/132_03_din.webm", pos=(0,0), anchor=(0,0))
image 132_04_din = Movie(play="animations/132_04_din.webm", pos=(0,0), anchor=(0,0))
image 132_05_din = Movie(play="animations/132_05_din.webm", pos=(0,0), anchor=(0,0))
image 132_06_din = Movie(play="animations/132_06_din.webm", pos=(0,0), anchor=(0,0))
image 132_07_din = Movie(play="animations/132_07_din.webm", pos=(0,0), anchor=(0,0))
image 132_08_din = Movie(play="animations/132_08_din.webm", pos=(0,0), anchor=(0,0))
image 132_09_din = Movie(play="animations/132_09_din.webm", pos=(0,0), anchor=(0,0))
image 132_10_din = Movie(play="animations/132_10_din.webm", pos=(0,0), anchor=(0,0))
image 132_11_din = Movie(play="animations/132_11_din.webm", pos=(0,0), anchor=(0,0))
image 132_12_din = Movie(play="animations/132_12_din.webm", pos=(0,0), anchor=(0,0))
image 132_13_din = Movie(play="animations/132_13_din.webm", pos=(0,0), anchor=(0,0))
image 132_14_din = Movie(play="animations/132_14_din.webm", pos=(0,0), anchor=(0,0))
image 132_15_din = Movie(play="animations/132_15_din.webm", pos=(0,0), anchor=(0,0))
image 133_01_din = Movie(play="animations/133_01_din.webm", pos=(0,0), anchor=(0,0))
image 133_02_din = Movie(play="animations/133_02_din.webm", pos=(0,0), anchor=(0,0))
image 133_03_din = Movie(play="animations/133_03_din.webm", pos=(0,0), anchor=(0,0))
image 133_04_din = Movie(play="animations/133_04_din.webm", pos=(0,0), anchor=(0,0))
image 133_05_din = Movie(play="animations/133_05_din.webm", pos=(0,0), anchor=(0,0))
image 133_06_din = Movie(play="animations/133_06_din.webm", pos=(0,0), anchor=(0,0))
image 133_07_din = Movie(play="animations/133_07_din.webm", pos=(0,0), anchor=(0,0))
image 133_08_din = Movie(play="animations/133_08_din.webm", pos=(0,0), anchor=(0,0))
image 133_09_din = Movie(play="animations/133_09_din.webm", pos=(0,0), anchor=(0,0))
image 133_10_din = Movie(play="animations/133_10_din.webm", pos=(0,0), anchor=(0,0))
image 133_11_din = Movie(play="animations/133_11_din.webm", pos=(0,0), anchor=(0,0))
image 133_12_din = Movie(play="animations/133_12_din.webm", pos=(0,0), anchor=(0,0))
image 133_13_din = Movie(play="animations/133_13_din.webm", pos=(0,0), anchor=(0,0))
image 135_01_din = Movie(play="animations/135_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 135_02_din = Movie(play="animations/135_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 135_03_din = Movie(play="animations/135_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 135_04_din = Movie(play="animations/135_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 135_05_din = Movie(play="animations/135_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 135_06_din = Movie(play="animations/135_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_01_din = Movie(play="animations/136_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_02_din = Movie(play="animations/136_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_03_din = Movie(play="animations/136_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_04_din = Movie(play="animations/136_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_05_din = Movie(play="animations/136_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_06_din = Movie(play="animations/136_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 136_07_din = Movie(play="animations/136_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_08_din = Movie(play="animations/136_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_09_din = Movie(play="animations/136_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_10_din = Movie(play="animations/136_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 136_11_din = Movie(play="animations/136_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_12_din = Movie(play="animations/136_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_13_din = Movie(play="animations/136_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 136_14_din = Movie(play="animations/136_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 136_15_din = Movie(play="animations/136_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_01_din = Movie(play="animations/137_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_02_din = Movie(play="animations/137_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_03_din = Movie(play="animations/137_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_04_din = Movie(play="animations/137_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_05_din = Movie(play="animations/137_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_06_din = Movie(play="animations/137_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_07_din = Movie(play="animations/137_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 137_08_din = Movie(play="animations/137_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_09_din = Movie(play="animations/137_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 137_10_din = Movie(play="animations/137_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_01_din = Movie(play="animations/138_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_02_din = Movie(play="animations/138_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_03_din = Movie(play="animations/138_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_04_din = Movie(play="animations/138_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_05_din = Movie(play="animations/138_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 138_06_din = Movie(play="animations/138_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_07_din = Movie(play="animations/138_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_08_din = Movie(play="animations/138_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 138_09_din = Movie(play="animations/138_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 139_01_din = Movie(play="animations/139_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_02_din = Movie(play="animations/139_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_03_din = Movie(play="animations/139_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_04_din = Movie(play="animations/139_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_05_din = Movie(play="animations/139_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_06_din = Movie(play="animations/139_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_07_din = Movie(play="animations/139_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_08_din = Movie(play="animations/139_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_09_din = Movie(play="animations/139_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_10_din = Movie(play="animations/139_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_11_din = Movie(play="animations/139_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_12_din = Movie(play="animations/139_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 139_13_din = Movie(play="animations/139_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_14_din = Movie(play="animations/139_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_15_din = Movie(play="animations/139_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_16_din = Movie(play="animations/139_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_17_din = Movie(play="animations/139_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 139_18_din = Movie(play="animations/139_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_01_din = Movie(play="animations/141_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_02_din = Movie(play="animations/141_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_03_din = Movie(play="animations/141_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_04_din = Movie(play="animations/141_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_05_din = Movie(play="animations/141_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_06_din = Movie(play="animations/141_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 141_07_din = Movie(play="animations/141_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_08_din = Movie(play="animations/141_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_09_din = Movie(play="animations/141_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_10_din = Movie(play="animations/141_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 141_11_din = Movie(play="animations/141_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_12_din = Movie(play="animations/141_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_13_din = Movie(play="animations/141_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_14_din = Movie(play="animations/141_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 141_15_din = Movie(play="animations/141_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_16_din = Movie(play="animations/141_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_17_din = Movie(play="animations/141_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_18_din = Movie(play="animations/141_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_19_din = Movie(play="animations/141_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_20_din = Movie(play="animations/141_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_21_din = Movie(play="animations/141_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_22_din = Movie(play="animations/141_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_23_din = Movie(play="animations/141_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 141_24_din = Movie(play="animations/141_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 142_01_din = Movie(play="animations/142_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 142_02_din = Movie(play="animations/142_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 142_03_din = Movie(play="animations/142_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 142_04_din = Movie(play="animations/142_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 142_05_din = Movie(play="animations/142_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 142_06_din = Movie(play="animations/142_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_01_din = Movie(play="animations/143_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_02_din = Movie(play="animations/143_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_03_din = Movie(play="animations/143_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_04_din = Movie(play="animations/143_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_05_din = Movie(play="animations/143_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 143_06_din = Movie(play="animations/143_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_07_din = Movie(play="animations/143_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_08_din = Movie(play="animations/143_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_09_din = Movie(play="animations/143_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_10_din = Movie(play="animations/143_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_11_din = Movie(play="animations/143_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 143_12_din = Movie(play="animations/143_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 144_01_din = Movie(play="animations/144_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_02_din = Movie(play="animations/144_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_03_din = Movie(play="animations/144_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_04_din = Movie(play="animations/144_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 144_05_din = Movie(play="animations/144_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_06_din = Movie(play="animations/144_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_07_din = Movie(play="animations/144_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_08_din = Movie(play="animations/144_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_09_din = Movie(play="animations/144_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 144_10_din = Movie(play="animations/144_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_11_din = Movie(play="animations/144_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_12_din = Movie(play="animations/144_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_13_din = Movie(play="animations/144_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_14_din = Movie(play="animations/144_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_15_din = Movie(play="animations/144_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_16_din = Movie(play="animations/144_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_17_din = Movie(play="animations/144_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_18_din = Movie(play="animations/144_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_19_din = Movie(play="animations/144_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 144_20_din = Movie(play="animations/144_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 145_01_din = Movie(play="animations/145_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_02_din = Movie(play="animations/145_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_03_din = Movie(play="animations/145_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_04_din = Movie(play="animations/145_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_05_din = Movie(play="animations/145_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_06_din = Movie(play="animations/145_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_07_din = Movie(play="animations/145_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_08_din = Movie(play="animations/145_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 145_09_din = Movie(play="animations/145_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_10_din = Movie(play="animations/145_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_11_din = Movie(play="animations/145_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_12_din = Movie(play="animations/145_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_13_din = Movie(play="animations/145_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 145_14_din = Movie(play="animations/145_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 145_15_din = Movie(play="animations/145_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 146_01_din = Movie(play="animations/146_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 146_02_din = Movie(play="animations/146_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 146_03_din = Movie(play="animations/146_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 146_04_din = Movie(play="animations/146_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 146_05_din = Movie(play="animations/146_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 146_06_din = Movie(play="animations/146_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 147_01_din = Movie(play="animations/147_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 147_02_din = Movie(play="animations/147_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 147_03_din = Movie(play="animations/147_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 147_04_din = Movie(play="animations/147_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 147_05_din = Movie(play="animations/147_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 147_06_din = Movie(play="animations/147_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 148_01_din = Movie(play="animations/148_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_02_din = Movie(play="animations/148_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_03_din = Movie(play="animations/148_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_04_din = Movie(play="animations/148_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_05_din = Movie(play="animations/148_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_06_din = Movie(play="animations/148_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_07_din = Movie(play="animations/148_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_08_din = Movie(play="animations/148_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_09_din = Movie(play="animations/148_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_10_din = Movie(play="animations/148_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_11_din = Movie(play="animations/148_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 148_12_din = Movie(play="animations/148_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 148_13_din = Movie(play="animations/148_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_01_din = Movie(play="animations/150_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_02_din = Movie(play="animations/150_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_03_din = Movie(play="animations/150_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_04_din = Movie(play="animations/150_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_05_din = Movie(play="animations/150_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_06_din = Movie(play="animations/150_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_07_din = Movie(play="animations/150_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_08_din = Movie(play="animations/150_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_09_din = Movie(play="animations/150_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_10_din = Movie(play="animations/150_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_11_din = Movie(play="animations/150_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 150_12_din = Movie(play="animations/150_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 150_13_din = Movie(play="animations/150_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_01_din = Movie(play="animations/151_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_02_din = Movie(play="animations/151_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_03_din = Movie(play="animations/151_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_04_din = Movie(play="animations/151_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_05_din = Movie(play="animations/151_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_06_din = Movie(play="animations/151_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_07_din = Movie(play="animations/151_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 151_08_din = Movie(play="animations/151_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_09_din = Movie(play="animations/151_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_10_din = Movie(play="animations/151_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_11_din = Movie(play="animations/151_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 151_12_din = Movie(play="animations/151_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 151_13_din = Movie(play="animations/151_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 152_01_din = Movie(play="animations/152_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 152_02_din = Movie(play="animations/152_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 152_03_din = Movie(play="animations/152_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 152_04_din = Movie(play="animations/152_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 152_05_din = Movie(play="animations/152_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 152_06_din = Movie(play="animations/152_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 152_07_din = Movie(play="animations/152_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_01_din = Movie(play="animations/153_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_02_din = Movie(play="animations/153_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_03_din = Movie(play="animations/153_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 153_04_din = Movie(play="animations/153_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_05_din = Movie(play="animations/153_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_06_din = Movie(play="animations/153_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_07_din = Movie(play="animations/153_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_08_din = Movie(play="animations/153_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 153_09_din = Movie(play="animations/153_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_10_din = Movie(play="animations/153_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_11_din = Movie(play="animations/153_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_12_din = Movie(play="animations/153_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 153_13_din = Movie(play="animations/153_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_14_din = Movie(play="animations/153_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 153_15_din = Movie(play="animations/153_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_01_din = Movie(play="animations/154_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_02_din = Movie(play="animations/154_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_03_din = Movie(play="animations/154_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_04_din = Movie(play="animations/154_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_05_din = Movie(play="animations/154_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_06_din = Movie(play="animations/154_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_07_din = Movie(play="animations/154_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_08_din = Movie(play="animations/154_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_09_din = Movie(play="animations/154_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_10_din = Movie(play="animations/154_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_11_din = Movie(play="animations/154_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_12_din = Movie(play="animations/154_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_13_din = Movie(play="animations/154_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_14_din = Movie(play="animations/154_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 154_15_din = Movie(play="animations/154_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 154_16_din = Movie(play="animations/154_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_01_din = Movie(play="animations/155_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_02_din = Movie(play="animations/155_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_03_din = Movie(play="animations/155_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_04_din = Movie(play="animations/155_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_05_din = Movie(play="animations/155_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_06_din = Movie(play="animations/155_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_07_din = Movie(play="animations/155_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 155_08_din = Movie(play="animations/155_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_09_din = Movie(play="animations/155_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_10_din = Movie(play="animations/155_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 155_11_din = Movie(play="animations/155_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 156_01_din = Movie(play="animations/156_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_02_din = Movie(play="animations/156_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_03_din = Movie(play="animations/156_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_04_din = Movie(play="animations/156_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 156_05_din = Movie(play="animations/156_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_06_din = Movie(play="animations/156_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_07_din = Movie(play="animations/156_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 156_08_din = Movie(play="animations/156_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_09_din = Movie(play="animations/156_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_10_din = Movie(play="animations/156_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_11_din = Movie(play="animations/156_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_12_din = Movie(play="animations/156_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_13_din = Movie(play="animations/156_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_14_din = Movie(play="animations/156_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_15_din = Movie(play="animations/156_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_16_din = Movie(play="animations/156_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_17_din = Movie(play="animations/156_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 156_18_din = Movie(play="animations/156_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_19_din = Movie(play="animations/156_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_20_din = Movie(play="animations/156_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_21_din = Movie(play="animations/156_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_22_din = Movie(play="animations/156_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_23_din = Movie(play="animations/156_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_24_din = Movie(play="animations/156_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_25_din = Movie(play="animations/156_25_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_26_din = Movie(play="animations/156_26_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 156_27_din = Movie(play="animations/156_27_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 157_01_din = Movie(play="animations/157_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_02_din = Movie(play="animations/157_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_03_din = Movie(play="animations/157_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_04_din = Movie(play="animations/157_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_05_din = Movie(play="animations/157_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_06_din = Movie(play="animations/157_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_07_din = Movie(play="animations/157_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_08_din = Movie(play="animations/157_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_09_din = Movie(play="animations/157_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_10_din = Movie(play="animations/157_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_11_din = Movie(play="animations/157_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_12_din = Movie(play="animations/157_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_13_din = Movie(play="animations/157_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_14_din = Movie(play="animations/157_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_15_din = Movie(play="animations/157_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_16_din = Movie(play="animations/157_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_17_din = Movie(play="animations/157_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_18_din = Movie(play="animations/157_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_19_din = Movie(play="animations/157_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_20_din = Movie(play="animations/157_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 157_21_din = Movie(play="animations/157_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 158_01_din = Movie(play="animations/158_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_02_din = Movie(play="animations/158_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_03_din = Movie(play="animations/158_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_04_din = Movie(play="animations/158_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_05_din = Movie(play="animations/158_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_06_din = Movie(play="animations/158_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_07_din = Movie(play="animations/158_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_08_din = Movie(play="animations/158_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 158_09_din = Movie(play="animations/158_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_10_din = Movie(play="animations/158_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_11_din = Movie(play="animations/158_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_12_din = Movie(play="animations/158_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_13_din = Movie(play="animations/158_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 158_14_din = Movie(play="animations/158_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 158_15_din = Movie(play="animations/158_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_01_din = Movie(play="animations/159_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_02_din = Movie(play="animations/159_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_03_din = Movie(play="animations/159_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_04_din = Movie(play="animations/159_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_05_din = Movie(play="animations/159_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_06_din = Movie(play="animations/159_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_07_din = Movie(play="animations/159_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_08_din = Movie(play="animations/159_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 159_09_din = Movie(play="animations/159_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_10_din = Movie(play="animations/159_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_11_din = Movie(play="animations/159_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 159_12_din = Movie(play="animations/159_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_13_din = Movie(play="animations/159_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_14_din = Movie(play="animations/159_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_15_din = Movie(play="animations/159_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 159_16_din = Movie(play="animations/159_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_01_din = Movie(play="animations/160_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_02_din = Movie(play="animations/160_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_03_din = Movie(play="animations/160_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_04_din = Movie(play="animations/160_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_05_din = Movie(play="animations/160_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_06_din = Movie(play="animations/160_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_07_din = Movie(play="animations/160_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_08_din = Movie(play="animations/160_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_09_din = Movie(play="animations/160_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_10_din = Movie(play="animations/160_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 160_11_din = Movie(play="animations/160_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 161_01_din = Movie(play="animations/161_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_01_din = Movie(play="animations/162_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_02_din = Movie(play="animations/162_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_03_din = Movie(play="animations/162_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_04_din = Movie(play="animations/162_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_05_din = Movie(play="animations/162_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_06_din = Movie(play="animations/162_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_07_din = Movie(play="animations/162_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_08_din = Movie(play="animations/162_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_09_din = Movie(play="animations/162_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_10_din = Movie(play="animations/162_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_11_din = Movie(play="animations/162_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_12_din = Movie(play="animations/162_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_13_din = Movie(play="animations/162_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_14_din = Movie(play="animations/162_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_15_din = Movie(play="animations/162_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_16_din = Movie(play="animations/162_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_17_din = Movie(play="animations/162_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_18_din = Movie(play="animations/162_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_19_din = Movie(play="animations/162_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_20_din = Movie(play="animations/162_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_21_din = Movie(play="animations/162_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_22_din = Movie(play="animations/162_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_23_din = Movie(play="animations/162_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_24_din = Movie(play="animations/162_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_25_din = Movie(play="animations/162_25_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_26_din = Movie(play="animations/162_26_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_27_din = Movie(play="animations/162_27_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_28_din = Movie(play="animations/162_28_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_29_din = Movie(play="animations/162_29_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_30_din = Movie(play="animations/162_30_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_31_din = Movie(play="animations/162_31_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 162_32_din = Movie(play="animations/162_32_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_01_din = Movie(play="animations/163_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_02_din = Movie(play="animations/163_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_03_din = Movie(play="animations/163_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_04_din = Movie(play="animations/163_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_05_din = Movie(play="animations/163_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 163_06_din = Movie(play="animations/163_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_07_din = Movie(play="animations/163_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_08_din = Movie(play="animations/163_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_09_din = Movie(play="animations/163_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_10_din = Movie(play="animations/163_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_11_din = Movie(play="animations/163_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 163_12_din = Movie(play="animations/163_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 165_01_din = Movie(play="animations/165_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 165_02_din = Movie(play="animations/165_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 165_03_din = Movie(play="animations/165_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 165_04_din = Movie(play="animations/165_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 165_05_din = Movie(play="animations/165_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 165_06_din = Movie(play="animations/165_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 165_07_din = Movie(play="animations/165_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 165_08_din = Movie(play="animations/165_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 166_01_din = Movie(play="animations/166_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 166_02_din = Movie(play="animations/166_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 166_03_din = Movie(play="animations/166_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 167_01_din = Movie(play="animations/167_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_01_din = Movie(play="animations/168_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_02_din = Movie(play="animations/168_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_03_din = Movie(play="animations/168_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_04_din = Movie(play="animations/168_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_05_din = Movie(play="animations/168_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_06_din = Movie(play="animations/168_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_07_din = Movie(play="animations/168_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_08_din = Movie(play="animations/168_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_09_din = Movie(play="animations/168_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_10_din = Movie(play="animations/168_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 168_11_din = Movie(play="animations/168_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 168_12_din = Movie(play="animations/168_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 168_13_din = Movie(play="animations/168_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 169_01_din = Movie(play="animations/169_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_02_din = Movie(play="animations/169_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_03_din = Movie(play="animations/169_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_04_din = Movie(play="animations/169_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_05_din = Movie(play="animations/169_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_06_din = Movie(play="animations/169_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_07_din = Movie(play="animations/169_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_08_din = Movie(play="animations/169_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_09_din = Movie(play="animations/169_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 169_10_din = Movie(play="animations/169_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 170_01_din = Movie(play="animations/170_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 170_02_din = Movie(play="animations/170_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 170_03_din = Movie(play="animations/170_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 170_04_din = Movie(play="animations/170_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 170_05_din = Movie(play="animations/170_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 170_06_din = Movie(play="animations/170_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 170_07_din = Movie(play="animations/170_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 171_01_din = Movie(play="animations/171_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_02_din = Movie(play="animations/171_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_03_din = Movie(play="animations/171_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 171_04_din = Movie(play="animations/171_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_05_din = Movie(play="animations/171_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_06_din = Movie(play="animations/171_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 171_07_din = Movie(play="animations/171_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_08_din = Movie(play="animations/171_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_09_din = Movie(play="animations/171_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_10_din = Movie(play="animations/171_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_11_din = Movie(play="animations/171_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_12_din = Movie(play="animations/171_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_13_din = Movie(play="animations/171_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_14_din = Movie(play="animations/171_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_15_din = Movie(play="animations/171_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_16_din = Movie(play="animations/171_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_17_din = Movie(play="animations/171_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_18_din = Movie(play="animations/171_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_19_din = Movie(play="animations/171_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_20_din = Movie(play="animations/171_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_21_din = Movie(play="animations/171_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_22_din = Movie(play="animations/171_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_23_din = Movie(play="animations/171_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_24_din = Movie(play="animations/171_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_25_din = Movie(play="animations/171_25_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_26_din = Movie(play="animations/171_26_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_27_din = Movie(play="animations/171_27_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_28_din = Movie(play="animations/171_28_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_29_din = Movie(play="animations/171_29_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 171_30_din = Movie(play="animations/171_30_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_31_din = Movie(play="animations/171_31_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 171_32_din = Movie(play="animations/171_32_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_33_din = Movie(play="animations/171_33_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_34_din = Movie(play="animations/171_34_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 171_35_din = Movie(play="animations/171_35_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 171_36_din = Movie(play="animations/171_36_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_01_din = Movie(play="animations/172_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_02_din = Movie(play="animations/172_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_03_din = Movie(play="animations/172_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_04_din = Movie(play="animations/172_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_05_din = Movie(play="animations/172_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_06_din = Movie(play="animations/172_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 172_07_din = Movie(play="animations/172_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_08_din = Movie(play="animations/172_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_09_din = Movie(play="animations/172_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_10_din = Movie(play="animations/172_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_11_din = Movie(play="animations/172_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_12_din = Movie(play="animations/172_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_13_din = Movie(play="animations/172_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_14_din = Movie(play="animations/172_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_15_din = Movie(play="animations/172_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_16_din = Movie(play="animations/172_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_17_din = Movie(play="animations/172_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_18_din = Movie(play="animations/172_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 172_19_din = Movie(play="animations/172_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_20_din = Movie(play="animations/172_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_21_din = Movie(play="animations/172_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_22_din = Movie(play="animations/172_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 172_23_din = Movie(play="animations/172_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_01_din = Movie(play="animations/173_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_02_din = Movie(play="animations/173_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_03_din = Movie(play="animations/173_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_04_din = Movie(play="animations/173_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_05_din = Movie(play="animations/173_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_06_din = Movie(play="animations/173_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_07_din = Movie(play="animations/173_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 173_08_din = Movie(play="animations/173_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 174_01_din = Movie(play="animations/174_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_02_din = Movie(play="animations/174_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_03_din = Movie(play="animations/174_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_04_din = Movie(play="animations/174_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_05_din = Movie(play="animations/174_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_06_din = Movie(play="animations/174_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_07_din = Movie(play="animations/174_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_08_din = Movie(play="animations/174_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_09_din = Movie(play="animations/174_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 174_10_din = Movie(play="animations/174_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 174_11_din = Movie(play="animations/174_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 174_12_din = Movie(play="animations/174_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 174_13_din = Movie(play="animations/174_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_14_din = Movie(play="animations/174_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_15_din = Movie(play="animations/174_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_16_din = Movie(play="animations/174_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_17_din = Movie(play="animations/174_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_18_din = Movie(play="animations/174_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_19_din = Movie(play="animations/174_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_20_din = Movie(play="animations/174_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_21_din = Movie(play="animations/174_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_22_din = Movie(play="animations/174_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_23_din = Movie(play="animations/174_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_24_din = Movie(play="animations/174_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_25_din = Movie(play="animations/174_25_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_26_din = Movie(play="animations/174_26_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_27_din = Movie(play="animations/174_27_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_28_din = Movie(play="animations/174_28_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_29_din = Movie(play="animations/174_29_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_30_din = Movie(play="animations/174_30_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 174_31_din = Movie(play="animations/174_31_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 174_32_din = Movie(play="animations/174_32_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 175_01_din = Movie(play="animations/175_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_02_din = Movie(play="animations/175_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_03_din = Movie(play="animations/175_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_04_din = Movie(play="animations/175_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_05_din = Movie(play="animations/175_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_06_din = Movie(play="animations/175_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_07_din = Movie(play="animations/175_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_08_din = Movie(play="animations/175_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_09_din = Movie(play="animations/175_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_10_din = Movie(play="animations/175_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_11_din = Movie(play="animations/175_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_12_din = Movie(play="animations/175_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_13_din = Movie(play="animations/175_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_14_din = Movie(play="animations/175_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_15_din = Movie(play="animations/175_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_16_din = Movie(play="animations/175_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_17_din = Movie(play="animations/175_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 175_18_din = Movie(play="animations/175_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_19_din = Movie(play="animations/175_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_20_din = Movie(play="animations/175_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_21_din = Movie(play="animations/175_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 175_22_din = Movie(play="animations/175_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_23_din = Movie(play="animations/175_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_24_din = Movie(play="animations/175_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_25_din = Movie(play="animations/175_25_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_26_din = Movie(play="animations/175_26_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_27_din = Movie(play="animations/175_27_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_28_din = Movie(play="animations/175_28_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_29_din = Movie(play="animations/175_29_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_30_din = Movie(play="animations/175_30_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_31_din = Movie(play="animations/175_31_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_32_din = Movie(play="animations/175_32_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_33_din = Movie(play="animations/175_33_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_34_din = Movie(play="animations/175_34_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_35_din = Movie(play="animations/175_35_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_36_din = Movie(play="animations/175_36_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_37_din = Movie(play="animations/175_37_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 175_38_din = Movie(play="animations/175_38_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_39_din = Movie(play="animations/175_39_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_40_din = Movie(play="animations/175_40_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 175_41_din = Movie(play="animations/175_41_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_42_din = Movie(play="animations/175_42_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_43_din = Movie(play="animations/175_43_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_44_din = Movie(play="animations/175_44_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_45_din = Movie(play="animations/175_45_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_46_din = Movie(play="animations/175_46_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_47_din = Movie(play="animations/175_47_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_48_din = Movie(play="animations/175_48_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_49_din = Movie(play="animations/175_49_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_50_din = Movie(play="animations/175_50_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_51_din = Movie(play="animations/175_51_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_52_din = Movie(play="animations/175_52_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_53_din = Movie(play="animations/175_53_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_54_din = Movie(play="animations/175_54_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_55_din = Movie(play="animations/175_55_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_56_din = Movie(play="animations/175_56_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_57_din = Movie(play="animations/175_57_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_58_din = Movie(play="animations/175_58_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_59_din = Movie(play="animations/175_59_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_60_din = Movie(play="animations/175_60_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_61_din = Movie(play="animations/175_61_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_62_din = Movie(play="animations/175_62_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_63_din = Movie(play="animations/175_63_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_64_din = Movie(play="animations/175_64_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_65_din = Movie(play="animations/175_65_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_66_din = Movie(play="animations/175_66_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 175_67_din = Movie(play="animations/175_67_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 176_01_din = Movie(play="animations/176_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_02_din = Movie(play="animations/176_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_03_din = Movie(play="animations/176_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_04_din = Movie(play="animations/176_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_05_din = Movie(play="animations/176_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_06_din = Movie(play="animations/176_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_07_din = Movie(play="animations/176_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_08_din = Movie(play="animations/176_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 176_09_din = Movie(play="animations/176_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_10_din = Movie(play="animations/176_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_11_din = Movie(play="animations/176_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 176_12_din = Movie(play="animations/176_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_13_din = Movie(play="animations/176_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_14_din = Movie(play="animations/176_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 176_15_din = Movie(play="animations/176_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_16_din = Movie(play="animations/176_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_17_din = Movie(play="animations/176_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_18_din = Movie(play="animations/176_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_19_din = Movie(play="animations/176_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_20_din = Movie(play="animations/176_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 176_21_din = Movie(play="animations/176_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_22_din = Movie(play="animations/176_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_23_din = Movie(play="animations/176_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 176_24_din = Movie(play="animations/176_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_25_din = Movie(play="animations/176_25_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_26_din = Movie(play="animations/176_26_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_27_din = Movie(play="animations/176_27_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_28_din = Movie(play="animations/176_28_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_29_din = Movie(play="animations/176_29_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_30_din = Movie(play="animations/176_30_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_31_din = Movie(play="animations/176_31_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_32_din = Movie(play="animations/176_32_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_33_din = Movie(play="animations/176_33_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 176_34_din = Movie(play="animations/176_34_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 176_35_din = Movie(play="animations/176_35_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 176_36_din = Movie(play="animations/176_36_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 178_01_din = Movie(play="animations/178_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 178_02_din = Movie(play="animations/178_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 178_03_din = Movie(play="animations/178_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 178_04_din = Movie(play="animations/178_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 178_05_din = Movie(play="animations/178_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 178_06_din = Movie(play="animations/178_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 178_07_din = Movie(play="animations/178_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 178_08_din = Movie(play="animations/178_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 178_09_din = Movie(play="animations/178_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 178_10_din = Movie(play="animations/178_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 179_01_din = Movie(play="animations/179_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_02_din = Movie(play="animations/179_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_03_din = Movie(play="animations/179_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_04_din = Movie(play="animations/179_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_05_din = Movie(play="animations/179_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_06_din = Movie(play="animations/179_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 179_07_din = Movie(play="animations/179_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_08_din = Movie(play="animations/179_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_09_din = Movie(play="animations/179_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_10_din = Movie(play="animations/179_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_11_din = Movie(play="animations/179_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_12_din = Movie(play="animations/179_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 179_13_din = Movie(play="animations/179_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_14_din = Movie(play="animations/179_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_15_din = Movie(play="animations/179_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_16_din = Movie(play="animations/179_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_17_din = Movie(play="animations/179_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_18_din = Movie(play="animations/179_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_19_din = Movie(play="animations/179_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 179_20_din = Movie(play="animations/179_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 179_21_din = Movie(play="animations/179_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 180_01_din = Movie(play="animations/180_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 180_02_din = Movie(play="animations/180_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 181_01_din = Movie(play="animations/181_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_02_din = Movie(play="animations/181_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_03_din = Movie(play="animations/181_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_04_din = Movie(play="animations/181_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_05_din = Movie(play="animations/181_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_06_din = Movie(play="animations/181_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 181_07_din = Movie(play="animations/181_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_08_din = Movie(play="animations/181_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_09_din = Movie(play="animations/181_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_10_din = Movie(play="animations/181_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_11_din = Movie(play="animations/181_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_12_din = Movie(play="animations/181_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 181_13_din = Movie(play="animations/181_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_14_din = Movie(play="animations/181_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_15_din = Movie(play="animations/181_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_16_din = Movie(play="animations/181_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 181_17_din = Movie(play="animations/181_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)

image 182_01_din = Movie(play="animations/182_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 182_02_din = Movie(play="animations/182_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 182_03_din = Movie(play="animations/182_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 182_04_din = Movie(play="animations/182_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 182_05_din = Movie(play="animations/182_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 182_06_din = Movie(play="animations/182_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 183_01_din = Movie(play="animations/183_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 183_02_din = Movie(play="animations/183_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 183_03_din = Movie(play="animations/183_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 183_04_din = Movie(play="animations/183_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 183_05_din = Movie(play="animations/183_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 184_01_din = Movie(play="animations/184_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_02_din = Movie(play="animations/184_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_03_din = Movie(play="animations/184_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_04_din = Movie(play="animations/184_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_05_din = Movie(play="animations/184_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_06_din = Movie(play="animations/184_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_07_din = Movie(play="animations/184_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_08_din = Movie(play="animations/184_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_09_din = Movie(play="animations/184_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_10_din = Movie(play="animations/184_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 184_11_din = Movie(play="animations/184_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 184_12_din = Movie(play="animations/184_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 185_01_din = Movie(play="animations/185_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 185_02_din = Movie(play="animations/185_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 185_03_din = Movie(play="animations/185_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 185_04_din = Movie(play="animations/185_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 185_05_din = Movie(play="animations/185_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 185_06_din = Movie(play="animations/185_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 185_07_din = Movie(play="animations/185_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 185_08_din = Movie(play="animations/185_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)

image 186_01_din = Movie(play="animations/186_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_02_din = Movie(play="animations/186_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_03_din = Movie(play="animations/186_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_04_din = Movie(play="animations/186_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_05_din = Movie(play="animations/186_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_06_din = Movie(play="animations/186_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_07_din = Movie(play="animations/186_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_08_din = Movie(play="animations/186_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 186_09_din = Movie(play="animations/186_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 186_10_din = Movie(play="animations/186_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 186_11_din = Movie(play="animations/186_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 187_01_din = Movie(play="animations/187_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 188_01_din = Movie(play="animations/188_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 189_01_din = Movie(play="animations/189_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 189_02_din = Movie(play="animations/189_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 189_03_din = Movie(play="animations/189_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 189_04_din = Movie(play="animations/189_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 189_05_din = Movie(play="animations/189_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 189_06_din = Movie(play="animations/189_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 190_01_din = Movie(play="animations/190_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 190_02_din = Movie(play="animations/190_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 190_03_din = Movie(play="animations/190_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 192_01_din = Movie(play="animations/192_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 192_02_din = Movie(play="animations/192_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 193_01_din = Movie(play="animations/193_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 193_02_din = Movie(play="animations/193_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 193_03_din = Movie(play="animations/193_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 193_04_din = Movie(play="animations/193_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 193_05_din = Movie(play="animations/193_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 194_01_din = Movie(play="animations/194_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_02_din = Movie(play="animations/194_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_03_din = Movie(play="animations/194_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_04_din = Movie(play="animations/194_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_05_din = Movie(play="animations/194_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_06_din = Movie(play="animations/194_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_07_din = Movie(play="animations/194_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_08_din = Movie(play="animations/194_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 194_09_din = Movie(play="animations/194_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_10_din = Movie(play="animations/194_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_11_din = Movie(play="animations/194_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_12_din = Movie(play="animations/194_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_13_din = Movie(play="animations/194_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_14_din = Movie(play="animations/194_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_15_din = Movie(play="animations/194_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_16_din = Movie(play="animations/194_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_17_din = Movie(play="animations/194_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_18_din = Movie(play="animations/194_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 194_19_din = Movie(play="animations/194_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_20_din = Movie(play="animations/194_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 194_21_din = Movie(play="animations/194_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)

image 195_01_din = Movie(play="animations/195_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_02_din = Movie(play="animations/195_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_03_din = Movie(play="animations/195_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_04_din = Movie(play="animations/195_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_05_din = Movie(play="animations/195_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_06_din = Movie(play="animations/195_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_07_din = Movie(play="animations/195_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 195_08_din = Movie(play="animations/195_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_09_din = Movie(play="animations/195_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_10_din = Movie(play="animations/195_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_11_din = Movie(play="animations/195_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_12_din = Movie(play="animations/195_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_13_din = Movie(play="animations/195_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_14_din = Movie(play="animations/195_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_15_din = Movie(play="animations/195_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_16_din = Movie(play="animations/195_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_17_din = Movie(play="animations/195_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 195_18_din = Movie(play="animations/195_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_19_din = Movie(play="animations/195_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_20_din = Movie(play="animations/195_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_21_din = Movie(play="animations/195_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_22_din = Movie(play="animations/195_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_23_din = Movie(play="animations/195_23_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 195_24_din = Movie(play="animations/195_24_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_25_din = Movie(play="animations/195_25_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_26_din = Movie(play="animations/195_26_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 195_27_din = Movie(play="animations/195_27_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_28_din = Movie(play="animations/195_28_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_29_din = Movie(play="animations/195_29_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 195_30_din = Movie(play="animations/195_30_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 196_01_din = Movie(play="animations/196_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_02_din = Movie(play="animations/196_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_03_din = Movie(play="animations/196_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_04_din = Movie(play="animations/196_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_05_din = Movie(play="animations/196_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 196_06_din = Movie(play="animations/196_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_07_din = Movie(play="animations/196_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_08_din = Movie(play="animations/196_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_09_din = Movie(play="animations/196_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 196_10_din = Movie(play="animations/196_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 197_01_din = Movie(play="animations/197_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 197_02_din = Movie(play="animations/197_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 197_03_din = Movie(play="animations/197_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 197_04_din = Movie(play="animations/197_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 198_01_din = Movie(play="animations/0200/198_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_02_din = Movie(play="animations/0200/198_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_03_din = Movie(play="animations/0200/198_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_04_din = Movie(play="animations/0200/198_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_05_din = Movie(play="animations/0200/198_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_06_din = Movie(play="animations/0200/198_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_07_din = Movie(play="animations/0200/198_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_08_din = Movie(play="animations/0200/198_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_09_din = Movie(play="animations/0200/198_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_10_din = Movie(play="animations/0200/198_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_11_din = Movie(play="animations/0200/198_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 198_12_din = Movie(play="animations/0200/198_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 198_13_din = Movie(play="animations/0200/198_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 198_14_din = Movie(play="animations/0200/198_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 199_01_din = Movie(play="animations/0200/199_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_02_din = Movie(play="animations/0200/199_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_03_din = Movie(play="animations/0200/199_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_04_din = Movie(play="animations/0200/199_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_05_din = Movie(play="animations/0200/199_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_06_din = Movie(play="animations/0200/199_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_07_din = Movie(play="animations/0200/199_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_08_din = Movie(play="animations/0200/199_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_09_din = Movie(play="animations/0200/199_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_10_din = Movie(play="animations/0200/199_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_11_din = Movie(play="animations/0200/199_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 199_12_din = Movie(play="animations/0200/199_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 201_01_din = Movie(play="animations/0200/201_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_02_din = Movie(play="animations/0200/201_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_03_din = Movie(play="animations/0200/201_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_04_din = Movie(play="animations/0200/201_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_05_din = Movie(play="animations/0200/201_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_06_din = Movie(play="animations/0200/201_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_07_din = Movie(play="animations/0200/201_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_08_din = Movie(play="animations/0200/201_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_09_din = Movie(play="animations/0200/201_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_10_din = Movie(play="animations/0200/201_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_11_din = Movie(play="animations/0200/201_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_12_din = Movie(play="animations/0200/201_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_13_din = Movie(play="animations/0200/201_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 201_14_din = Movie(play="animations/0200/201_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 202_01_din = Movie(play="animations/0200/202_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_02_din = Movie(play="animations/0200/202_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_03_din = Movie(play="animations/0200/202_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_04_din = Movie(play="animations/0200/202_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_05_din = Movie(play="animations/0200/202_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_06_din = Movie(play="animations/0200/202_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_07_din = Movie(play="animations/0200/202_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_08_din = Movie(play="animations/0200/202_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_09_din = Movie(play="animations/0200/202_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_10_din = Movie(play="animations/0200/202_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_11_din = Movie(play="animations/0200/202_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_12_din = Movie(play="animations/0200/202_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_13_din = Movie(play="animations/0200/202_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 202_14_din = Movie(play="animations/0200/202_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_15_din = Movie(play="animations/0200/202_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_16_din = Movie(play="animations/0200/202_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_17_din = Movie(play="animations/0200/202_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_18_din = Movie(play="animations/0200/202_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_19_din = Movie(play="animations/0200/202_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_20_din = Movie(play="animations/0200/202_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_21_din = Movie(play="animations/0200/202_21_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 202_22_din = Movie(play="animations/0200/202_22_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 203_01_din = Movie(play="animations/0200/203_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 203_02_din = Movie(play="animations/0200/203_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 203_03_din = Movie(play="animations/0200/203_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 203_04_din = Movie(play="animations/0200/203_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 203_05_din = Movie(play="animations/0200/203_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 203_06_din = Movie(play="animations/0200/203_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 203_07_din = Movie(play="animations/0200/203_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 203_08_din = Movie(play="animations/0200/203_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)

image 204_01_din = Movie(play="animations/0200/204_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 204_02_din = Movie(play="animations/0200/204_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 204_03_din = Movie(play="animations/0200/204_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 204_04_din = Movie(play="animations/0200/204_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 204_05_din = Movie(play="animations/0200/204_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 205_01_din = Movie(play="animations/0200/205_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_02_din = Movie(play="animations/0200/205_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_03_din = Movie(play="animations/0200/205_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_04_din = Movie(play="animations/0200/205_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_05_din = Movie(play="animations/0200/205_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_06_din = Movie(play="animations/0200/205_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_07_din = Movie(play="animations/0200/205_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_08_din = Movie(play="animations/0200/205_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_09_din = Movie(play="animations/0200/205_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_10_din = Movie(play="animations/0200/205_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_11_din = Movie(play="animations/0200/205_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_12_din = Movie(play="animations/0200/205_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_13_din = Movie(play="animations/0200/205_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_14_din = Movie(play="animations/0200/205_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_15_din = Movie(play="animations/0200/205_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_16_din = Movie(play="animations/0200/205_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_17_din = Movie(play="animations/0200/205_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_18_din = Movie(play="animations/0200/205_18_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_19_din = Movie(play="animations/0200/205_19_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 205_20_din = Movie(play="animations/0200/205_20_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 206_01_din = Movie(play="animations/0200/206_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_02_din = Movie(play="animations/0200/206_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_03_din = Movie(play="animations/0200/206_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_04_din = Movie(play="animations/0200/206_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_05_din = Movie(play="animations/0200/206_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 206_06_din = Movie(play="animations/0200/206_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_07_din = Movie(play="animations/0200/206_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_08_din = Movie(play="animations/0200/206_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_09_din = Movie(play="animations/0200/206_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 206_10_din = Movie(play="animations/0200/206_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_11_din = Movie(play="animations/0200/206_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_12_din = Movie(play="animations/0200/206_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_13_din = Movie(play="animations/0200/206_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 206_14_din = Movie(play="animations/0200/206_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 207_01_din = Movie(play="animations/0200/207_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 207_02_din = Movie(play="animations/0200/207_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 207_03_din = Movie(play="animations/0200/207_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 207_04_din = Movie(play="animations/0200/207_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 207_05_din = Movie(play="animations/0200/207_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 207_06_din = Movie(play="animations/0200/207_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 207_07_din = Movie(play="animations/0200/207_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 207_08_din = Movie(play="animations/0200/207_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 207_09_din = Movie(play="animations/0200/207_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image 208_01_din = Movie(play="animations/0200/208_01_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_02_din = Movie(play="animations/0200/208_02_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_03_din = Movie(play="animations/0200/208_03_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_04_din = Movie(play="animations/0200/208_04_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_05_din = Movie(play="animations/0200/208_05_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_06_din = Movie(play="animations/0200/208_06_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 208_07_din = Movie(play="animations/0200/208_07_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_08_din = Movie(play="animations/0200/208_08_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_09_din = Movie(play="animations/0200/208_09_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 208_10_din = Movie(play="animations/0200/208_10_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_11_din = Movie(play="animations/0200/208_11_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_12_din = Movie(play="animations/0200/208_12_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_13_din = Movie(play="animations/0200/208_13_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_14_din = Movie(play="animations/0200/208_14_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_15_din = Movie(play="animations/0200/208_15_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))
image 208_16_din = Movie(play="animations/0200/208_16_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5), loop = False)
image 208_17_din = Movie(play="animations/0200/208_17_din.webm", pos=(0.5,0.5), anchor=(0.5,0.5))

image click:
    pause 1.2
    "click_here_small_2.png"
    pause 0.5
    "click_here_small_1.png"
    pause 0.5
    "click_here_small_2.png"
    pause 0.5
    "click_here_small_1.png"
    pause 0.5
    "click_here_small_2.png"
    pause 0.5
    "click_here_small_1.png"

transform click_pos:
    xpos 950
    ypos 50
    xanchor 0.5
    yanchor 0.5



image 17_18_anim:
    "17_18_1.webp" with Dissolve(.3)
    pause 1.0
    "17_18_2.webp" with Dissolve(.3)
    pause 1.0
    repeat

image aurora_anim_1:
    "78_36_01.webp" with Dissolve(0.05)
    pause 0.2
    "78_36_02.webp" with Dissolve(0.05)
    pause 0.2
    "78_36_03.webp" with Dissolve(0.05)
    pause 0.2
    "78_36_04.webp" with Dissolve(0.05)
    pause 0.2
    "78_36_03.webp" with Dissolve(0.05)
    pause 0.2
    "78_36_02.webp" with Dissolve(0.05)
    pause 0.2
    repeat

image aurora_anim_2:
    "78_39_01.webp" with Dissolve(0.05)
    pause 0.2
    "78_39_02.webp" with Dissolve(0.05)
    pause 0.2
    "78_39_03.webp" with Dissolve(0.05)
    pause 0.2
    "78_39_04.webp" with Dissolve(0.05)
    pause 0.2
    "78_39_05.webp" with Dissolve(0.05)
    pause 0.2
    "78_39_04.webp" with Dissolve(0.05)
    pause 0.2
    "78_39_03.webp" with Dissolve(0.05)
    pause 0.2
    "78_39_02.webp" with Dissolve(0.05)
    pause 0.2
    repeat

image adele_anim_1:
    "81_49.webp" with Dissolve(0.2)
    pause 0.4
    "81_50.webp" with Dissolve(0.2)
    pause 0.4
    repeat

image miranda_lick:
    "82_37.webp" with Dissolve(0.1)
    pause 0.25
    "82_38.webp" with Dissolve(0.1)
    pause 0.25
    "82_39.webp" with Dissolve(0.1)
    pause 0.25
    "82_38.webp" with Dissolve(0.1)
    pause 0.25
    repeat

image 90_25_anim:
    "90_25a.webp" with Dissolve(0.02)
    pause 0.2
    "90_25b.webp" with Dissolve(0.02)
    pause 0.2
    "90_25c.webp" with Dissolve(0.02)
    pause 0.2
    "90_25d.webp" with Dissolve(0.02)




    pause 0.2
    "90_25c.webp" with Dissolve(0.02)
    pause 0.2
    "90_25b.webp" with Dissolve(0.02)
    pause 0.2
    repeat

image 90_26_anim:
    "90_26a.webp" with Dissolve(0.05)
    pause 0.1
    "90_26b.webp" with Dissolve(0.05)
    pause 0.1
    "90_26c.webp" with Dissolve(0.05)
    pause 0.1
    "90_26d.webp" with Dissolve(0.05)
    pause 0.1
    "90_26e.webp" with Dissolve(0.05)
    pause 0.1
    "90_26d.webp" with Dissolve(0.05)
    pause 0.1
    "90_26c.webp" with Dissolve(0.05)
    pause 0.1
    "90_26b.webp" with Dissolve(0.05)
    pause 0.1
    repeat

image 93_53_anim:
    "93_53a.webp" with Dissolve(0.05)
    pause 0.1
    "93_53b.webp" with Dissolve(0.05)
    pause 0.1
    "93_53c.webp" with Dissolve(0.05)
    pause 0.1
    "93_53b.webp" with Dissolve(0.05)
    pause 0.1
    "93_53a.webp" with Dissolve(0.05)
    pause 0.1
    repeat

image 91_19_anim:
    "91_19a.webp" with Dissolve(.05)
    pause 0.1
    "91_19b.webp" with Dissolve(.05)
    pause 0.1
    "91_19c.webp" with Dissolve(.05)
    pause 0.1
    "91_19d.webp" with Dissolve(.05)
    pause 0.1
    "91_19e.webp" with Dissolve(.05)
    pause 0.1
    "91_19d.webp" with Dissolve(.05)
    pause 0.1
    "91_19c.webp" with Dissolve(.05)
    pause 0.1
    "91_19b.webp" with Dissolve(.05)
    pause 0.1
    repeat

image 122_51_anim:
    "122_51_1.webp" with Dissolve(.2)
    pause 1.0
    "122_51_2.webp" with Dissolve(.2)
    pause 1.5
    repeat

image 123_21_anim:
    "123_21.webp" with Dissolve(.2)
    pause 1.5
    "123_22.webp" with Dissolve(.2)
    pause 0.5
    "123_23.webp" with Dissolve(.2)
    pause 1.0
    "123_24.webp" with Dissolve(.3)
    pause 1.0
    "123_23.webp" with Dissolve(.3)
    pause 1.0
    "123_24.webp" with Dissolve(.3)
    pause 1.0
    "123_23.webp" with Dissolve(.3)
    pause 0.2
    "123_22.webp" with Dissolve(.2)
    pause 0.5
    repeat

image 123_32_anim:
    "123_32.webp" with Dissolve(.3)
    pause 0.5
    "123_33.webp" with Dissolve(.3)
    pause 0.5
    repeat

image 129_28_anim:
    "129_28.webp" with Dissolve(.05)
    pause 0.15
    "129_29.webp" with Dissolve(.05)
    pause 0.1
    "129_30.webp" with Dissolve(.05)
    pause 0.1
    "129_31.webp" with Dissolve(.05)
    pause 0.15
    "129_30.webp" with Dissolve(.05)
    pause 0.1
    "129_29.webp" with Dissolve(.05)
    pause 0.1
    repeat

image 129_122_anim_slow:
    "129_122_1.webp" with Dissolve(.1)
    pause 0.2
    "129_122_2.webp" with Dissolve(.1)
    pause 0.15
    "129_122_3.webp" with Dissolve(.1)
    pause 0.1
    "129_122_4.webp" with Dissolve(.1)
    pause 0.15
    "129_122_3.webp" with Dissolve(.1)
    pause 0.1
    "129_122_2.webp" with Dissolve(.1)
    pause 0.15
    repeat

image 129_122_anim_fast:
    "129_122_1.webp" with Dissolve(.1)
    pause 0.1
    "129_122_2.webp" with Dissolve(.1)
    pause 0.07
    "129_122_3.webp" with Dissolve(.1)
    pause 0.05
    "129_122_4.webp" with Dissolve(.1)
    pause 0.07
    "129_122_3.webp" with Dissolve(.1)
    pause 0.05
    "129_122_2.webp" with Dissolve(.1)
    pause 0.1
    repeat

image 129_165_anim:
    "129_165_1.webp" with Dissolve(.3)
    pause 0.8
    "129_165_2.webp" with Dissolve(.3)
    pause 0.8
    repeat

image 129_218_anim:
    "129_218.webp" with Dissolve(.3)
    pause 0.8
    "129_219.webp" with Dissolve(.3)
    pause 0.8
    repeat

image 131_21_anim:
    "131_21_1.webp" with Dissolve(.1)
    pause 0.2
    "131_21_2.webp" with Dissolve(.1)
    pause 0.15
    "131_21_3.webp" with Dissolve(.1)
    pause 0.1
    "131_21_4.webp" with Dissolve(.1)
    pause 0.15
    "131_21_5.webp" with Dissolve(.1)
    pause 0.2
    "131_21_4.webp" with Dissolve(.1)
    pause 0.15
    "131_21_3.webp" with Dissolve(.1)
    pause 0.1
    "131_21_2.webp" with Dissolve(.1)
    pause 0.15
    repeat

image 131_22_anim:
    "131_22_1.webp" with Dissolve(.7)
    pause 0.8
    "131_22_2.webp" with Dissolve(.7)
    pause 0.8
    repeat

image 135_13_anim:
    "135_13.webp" with Dissolve(.05)
    pause 0.3
    "135_14.webp" with Dissolve(.05)
    pause 0.3
    repeat

image 135_39_anim:
    "135_39.webp" with Dissolve(.3)
    pause 1.0
    "135_40.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 135_56_anim:
    "135_56.webp" with Dissolve(.3)
    pause 1.0
    "135_57.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 136_46_anim:
    "136_46.webp" with Dissolve(.3)
    pause 2.0
    "136_47.webp" with Dissolve(.3)
    pause 2.0
    repeat

image 137_22_anim:
    "137_22.webp" with Dissolve(.3)
    pause 1.5
    "137_23.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 138_06_anim:
    "138_06.webp" with Dissolve(.3)
    pause 0.3
    "138_07.webp" with Dissolve(.3)
    pause 0.3
    repeat

image 137_57_anim:
    "137_57_01.webp"
    pause 0.033
    "137_57_02.webp"
    pause 0.033
    "137_57_03.webp"
    pause 0.033
    "137_57_04.webp"
    pause 0.033
    "137_57_05.webp"
    pause 0.033
    "137_57_06.webp"
    pause 0.033
    "137_57_07.webp"
    pause 0.033
    "137_57_08.webp"
    pause 0.033
    "137_57_09.webp"
    pause 0.033
    "137_57_10.webp"
    pause 0.033
    "137_57_11.webp"
    pause 0.033
    "137_57_12.webp"
    pause 0.033
    "137_57_13.webp"
    pause 0.033
    "137_57_14.webp"
    pause 0.033
    "137_57_15.webp"
    pause 0.033
    "137_57_16.webp"
    pause 0.033
    "137_57_17.webp"
    pause 0.033
    "137_57_18.webp"
    pause 0.033
    "137_57_19.webp"
    pause 0.033
    "137_57_20.webp"
    pause 0.033
    "137_57_21.webp"
    pause 0.033
    "137_57_01.webp"
    pause 0.033
    "137_57_02.webp"
    pause 0.033
    "137_57_03.webp"
    pause 0.033
    "137_57_04.webp"
    pause 0.033
    "137_57_05.webp"
    pause 0.033
    "137_57_06.webp"
    pause 0.033
    "137_57_07.webp"
    pause 0.033
    "137_57_08.webp"
    pause 0.033
    "137_57_09.webp"
    pause 0.033
    "137_57_10.webp"
    pause 0.033
    "137_57_11.webp"
    pause 0.033
    "137_57_12.webp"
    pause 0.033
    "137_57_13.webp"
    pause 0.033
    "137_57_14.webp"
    pause 0.033
    "137_57_15.webp"
    pause 0.033
    "137_57_16.webp"
    pause 0.033
    "137_57_17.webp"
    pause 0.033
    "137_57_18.webp"
    pause 0.033
    "137_57_19.webp"
    pause 0.033
    "137_57_20.webp"
    pause 0.033
    "137_57_21.webp"
    pause 2.5
    repeat

image 139_16_anim:
    "139_16.webp" with Dissolve(.3)
    pause 1.5
    "139_17.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 141_34_anim:
    "141_34_1.webp" with Dissolve(.2)
    pause 0.2
    "141_34_2.webp" with Dissolve(.2)
    pause 0.2
    "141_34_3.webp" with Dissolve(.2)
    pause 0.2
    "141_34_4.webp" with Dissolve(.2)
    pause 0.2
    "141_34_3.webp" with Dissolve(.2)
    pause 0.2
    "141_34_2.webp" with Dissolve(.2)
    pause 0.2
    repeat

image 144_15_anim:
    "144_15_1.webp" with Dissolve(.6)
    pause 1.5
    "144_15_2.webp" with Dissolve(.6)
    pause 1.5
    repeat

image 144_16_anim:
    "144_16_1.webp" with Dissolve(.5)
    pause 1.5
    "144_16_2.webp" with Dissolve(.5)
    pause 1.5
    repeat

image 144_45_anim:
    "144_45.webp" with Dissolve(.3)
    pause 1.5
    "144_46.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 144_52_anim:
    "144_52_1.webp" with Dissolve(.3)
    pause 1.5
    "144_52_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 144_59_anim:
    "144_59_1.webp" with Dissolve(.3)
    pause 1.5
    "144_59_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 144_62_anim:
    "144_62_1.webp" with Dissolve(.3)
    pause 1.5
    "144_62_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 144_67_anim:
    "144_67_1.webp" with Dissolve(.3)
    pause 1.5
    "144_67_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 144_76_anim:
    "144_76_1.webp" with Dissolve(.3)
    pause 1.5
    "144_76_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 144_80_anim:
    "144_80_1.webp" with Dissolve(.3)
    pause 1.5
    "144_80_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 144_83_anim:
    "144_83_1.webp" with Dissolve(.3)
    pause 1.5
    "144_83_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 145_11_anim:
    "145_11_1.webp" with Dissolve(.3)
    pause 1.0
    "145_11_2.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 147_04_anim:
    "147_04_1.webp" with Dissolve(.5)
    pause 1.4
    "147_04_2.webp" with Dissolve(.5)
    pause 1.4
    repeat

image 147_16_anim:
    "147_16_1.webp" with Dissolve(.3)
    pause 1.0
    "147_16_2.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 147_34_anim:
    "147_34_1.webp" with Dissolve(.3)
    pause 1.0
    "147_34_2.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 148_25_anim:
    "148_25_1.webp" with Dissolve(.3)
    pause 1.0
    "148_25_2.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 148_44_anim:
    "148_44_1.webp" with Dissolve(.3)
    pause 1.5
    "148_44_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 148_57_anim:
    "148_57_1.webp" with Dissolve(.3)
    pause 1.0
    "148_57_2.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 149_21_anim:
    "149_21.webp" with Dissolve(.15)
    pause 0.15
    "149_22.webp" with Dissolve(.15)
    pause 0.15
    repeat

image 151_20_anim:
    "151_20_1.webp" with Dissolve(.3)
    pause 1.0
    "151_20_2.webp" with Dissolve(.3)
    pause 1.0
    repeat

image 152_06_anim:
    "152_06_1.webp" with Dissolve(.3)
    pause 1.5
    "152_06_2.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 152_08_anim:
    "152_08_1.webp" with Dissolve(.3)
    pause 0.8
    "152_08_2.webp" with Dissolve(.3)
    pause 0.8
    repeat

image 152_12_anim:
    "152_12_1.webp" with Dissolve(.3)
    pause 0.8
    "152_12_2.webp" with Dissolve(.3)
    pause 0.8
    repeat

image 152_19_anim:
    "152_19_1.webp" with Dissolve(.4)
    pause 1.5
    "152_19_2.webp" with Dissolve(.4)
    pause 1.5
    repeat

image 153_15_anim:
    "153_15_1.webp" with Dissolve(.2)
    pause .2
    "153_15_2.webp" with Dissolve(.2)
    pause .2
    "153_15_3.webp" with Dissolve(.2)
    pause .2
    "153_15_4.webp" with Dissolve(.2)
    pause .2
    "153_15_3.webp" with Dissolve(.2)
    pause .2
    "153_15_2.webp" with Dissolve(.2)
    pause .2
    "153_15_1.webp" with Dissolve(.2)
    pause 3.5
    repeat

image 153_40_anim:
    "153_40_1.webp" with Dissolve(.3)
    pause 1.2
    "153_40_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 154_18_anim:
    "154_18_1.webp" with Dissolve(.3)
    pause 1.2
    "154_18_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 154_31_anim:
    "154_31_1.webp" with Dissolve(.3)
    pause 1.2
    "154_31_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 154_32_anim:
    "154_32_1.webp" with Dissolve(.3)
    pause 1.2
    "154_32_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 155_15_anim:
    "155_15_1.webp" with Dissolve(.3)
    pause 1.2
    "155_15_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 155_89_anim:
    "155_89_1.webp" with Dissolve(.3)
    pause 1.2
    "155_89_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 156_02_anim:
    "156_02_1.webp" with Dissolve(.2)
    pause 0.2
    "156_02_2.webp" with Dissolve(.2)
    pause 0.2
    repeat


image 156_93_anim:
    "156_93_1.webp" with Dissolve(.3)
    pause 1.2
    "156_93_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 157_57_anim:
    "157_57_1.webp" with Dissolve(.3)
    pause 1.2
    "157_57_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 159_33_anim:
    "159_33_1.webp" with Dissolve(.3)
    pause 1.2
    "159_33_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 159_52_anim:
    "159_52_1.webp" with Dissolve(.08)
    pause 0.1
    "159_52_2.webp" with Dissolve(.06)
    pause 0.08
    "159_52_3.webp" with Dissolve(.04)
    pause 0.07
    "159_52_4.webp" with Dissolve(.04)
    pause 0.07
    "159_52_5.webp" with Dissolve(.06)
    pause 0.08
    "159_52_6.webp" with Dissolve(.08)
    pause 0.1
    "159_52_5.webp" with Dissolve(.06)
    pause 0.08
    "159_52_4.webp" with Dissolve(.04)
    pause 0.07
    "159_52_3.webp" with Dissolve(.06)
    pause 0.07
    "159_52_2.webp" with Dissolve(.08)
    pause 0.1
    repeat

image 159_53_anim:
    "159_53.webp" with Dissolve(0.3)
    pause 1.8
    "159_54.webp" with Dissolve(0.3)
    pause 1.8
    repeat

image 159_56_anim:
    "159_56_1.webp" with Dissolve(0.3)
    pause 1.8
    "159_56_2.webp" with Dissolve(0.3)
    pause 1.8
    repeat

image 162_196_anim:
    "162_196_1.webp" with Dissolve(0.5)
    pause 0.5
    "162_196_2.webp" with Dissolve(0.5)
    pause 0.5
    repeat

image 162_197_anim:
    "162_197_1.webp" with Dissolve(0.5)
    pause 0.5
    "162_197_2.webp" with Dissolve(0.5)
    pause 0.5
    repeat

image 162_199_anim:
    "162_199_1.webp" with Dissolve(0.5)
    pause 0.5
    "162_199_2.webp" with Dissolve(0.5)
    pause 0.5
    repeat

image 162_201_anim:
    "162_201_1.webp" with Dissolve(0.5)
    pause 0.5
    "162_201_2.webp" with Dissolve(0.5)
    pause 0.5
    repeat

image 162_228_anim:
    "162_228_1.webp" with Dissolve(.3)
    pause 1.2
    "162_228_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 162_239_anim:
    "162_239_1.webp" with Dissolve(.3)
    pause 1.2
    "162_239_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 162_247_anim:
    "162_247_1.webp" with Dissolve(.3)
    pause 1.2
    "162_247_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 162_285_anim:
    "162_285_1.webp" with Dissolve(.3)
    pause 1.2
    "162_285_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 162_292_anim:
    "162_292_1.webp" with Dissolve(.3)
    pause 1.2
    "162_292_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 162_328_anim:
    "162_328_1.webp" with Dissolve(0.5)
    pause 0.5
    "162_328_2.webp" with Dissolve(0.5)
    pause 0.5
    repeat

image 162_329_anim:
    "162_329_1.webp" with Dissolve(0.5)
    pause 0.5
    "162_329_2.webp" with Dissolve(0.5)
    pause 0.5
    repeat

image 162_350_anim:
    "162_350_1.webp" with Dissolve(.3)
    pause 1.2
    "162_350_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 163_60_anim:
    "163_60_1.webp" with Dissolve(.3)
    pause 1.2
    "163_60_2.webp" with Dissolve(.3)
    pause 1.2
    repeat


image 165_55_anim:
    "165_55_1.webp" with Dissolve(.3)
    pause 1.2
    "165_55_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 165_62_anim:
    "165_62_1.webp" with Dissolve(.3)
    pause 0.9
    "165_62_2.webp" with Dissolve(.3)
    pause 0.9
    repeat

image 166_24_anim:
    "166_24_1.webp" with Dissolve(.3)
    pause 1.2
    "166_24_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 166_64_anim:
    "166_64_1.webp" with Dissolve(.3)
    pause 1.2
    "166_64_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 169_18_anim:
    "169_18_1.webp" with Dissolve(.3)
    pause 1.2
    "169_18_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 170_09_anim:
    "170_09_1.webp" with Dissolve(.3)
    pause 1.2
    "170_09_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 171_30_anim:
    "171_30.webp" with Dissolve(.3)
    pause 0.6
    "171_31.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 171_73_anim:
    "171_73_1.webp" with Dissolve(.3)
    pause 1.2
    "171_73_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 171_78_anim:
    "171_78_1.webp" with Dissolve(.3)
    pause 0.6
    "171_78_2.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 171_79_anim:
    "171_79_1.webp" with Dissolve(.3)
    pause 0.6
    "171_79_2.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 171_84_anim:
    "171_84_1.webp" with Dissolve(.3)
    pause 1.2
    "171_84_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 171_225_anim:
    "171_225_1.webp" with Dissolve(.3)
    pause 1.2
    "171_225_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 171_235_anim:
    "171_235_1.webp" with Dissolve(.3)
    pause 1.2
    "171_235_2.webp" with Dissolve(.3)
    pause 1.2
    repeat


image 172_137_anim:
    "172_137.webp" with Dissolve(.3)
    pause 0.6
    "172_138.webp" with Dissolve(.3)
    pause 0.7
    repeat


image 173_14_anim:
    "173_14.webp" with Dissolve(.3)
    pause 0.6
    "173_15.webp" with Dissolve(.3)
    pause 0.7
    repeat


image 173_23_anim:
    "173_23.webp" with Dissolve(.3)
    pause 0.6
    "173_24.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 173_29_anim:
    "173_29_1.webp" with Dissolve(.3)
    pause 1.2
    "173_29_2.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 174_216_anim:
    "174_216.webp" with Dissolve(.3)
    pause 1.2
    "174_217.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 174_255_anim:
    "174_255.webp" with Dissolve(.3)
    pause 1.2
    "174_256.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 174_273_anim:
    "174_273.webp" with Dissolve(.3)
    pause 0.6
    "174_274.webp" with Dissolve(.3)
    pause 0.7
    repeat


image 175_58_anim:
    "175_58.webp" with Dissolve(.3)
    pause 1.2
    "175_59.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_143_anim:
    "175_143.webp" with Dissolve(.2)
    pause 0.4
    "175_144.webp" with Dissolve(.2)
    pause 0.4
    repeat

image 175_183_anim:
    "175_183.webp" with Dissolve(.3)
    pause 1.2
    "175_184.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_191_anim:
    "175_191.webp" with Dissolve(.3)
    pause 0.6
    "175_192.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 175_233_anim:
    "175_233.webp" with Dissolve(.3)
    pause 1.2
    "175_234.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_249_anim:
    "175_249.webp" with Dissolve(.1)
    pause 0.5
    "175_250.webp" with Dissolve(.1)
    pause 0.5
    "175_251.webp" with Dissolve(.1)
    pause 0.5
    "175_250.webp" with Dissolve(.1)
    pause 0.5
    repeat

image 175_523_anim:
    "175_523.webp" with Dissolve(.3)
    pause 1.2
    "175_524.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_529_anim:
    "175_529.webp" with Dissolve(.3)
    pause 1.2
    "175_530.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_583_anim:
    "175_583.webp" with Dissolve(.3)
    pause 1.2
    "175_584.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_587_anim:
    "175_587.webp" with Dissolve(.3)
    pause 1.2
    "175_588.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_662_anim:
    "175_662.webp" with Dissolve(.3)
    pause 0.6
    "175_663.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 175_670_anim:
    "175_670.webp" with Dissolve(.3)
    pause 1.2
    "175_671.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 175_701_anim:
    "175_701.webp" with Dissolve(.3)
    pause 1.2
    "175_702.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 176_135_anim:
    "176_135.webp" with Dissolve(.3)
    pause 0.6
    "176_136.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 176_165_anim:
    "176_165.webp" with Dissolve(.3)
    pause 1.2
    "176_166.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 176_216_anim:
    "176_216.webp" with Dissolve(.3)
    pause 1.2
    "176_217.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 178_16_anim:
    "178_16.webp" with Dissolve(.05)
    pause 0.1
    "178_17.webp" with Dissolve(.05)
    pause 0.1
    "178_18.webp" with Dissolve(.05)
    pause 0.1
    repeat

image 178_30_anim:
    "178_30.webp" with Dissolve(.05)
    pause 0.1
    "178_31.webp" with Dissolve(.05)
    pause 0.1
    "178_32.webp" with Dissolve(.05)
    pause 0.1
    repeat

image 178_37_anim:
    "178_37.webp" with Dissolve(.3)
    pause 1.2
    "178_38.webp" with Dissolve(.3)
    pause 1.2
    repeat


image 178_54_anim:
    "178_54.webp" with Dissolve(.3)
    pause 1.2
    "178_55.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 179_09_anim:
    "179_09.webp" with Dissolve(.3)
    pause 1.2
    "179_10.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 179_35_anim:
    "179_35.webp" with Dissolve(.3)
    pause 1.2
    "179_36.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 179_38_anim:
    "179_38.webp" with Dissolve(.3)
    pause 1.2
    "179_39.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 181_58_anim:
    "181_58.webp" with Dissolve(.3)
    pause 1.2
    "181_59.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 193_48_anim:
    "193_48.webp" with Dissolve(.3)
    pause 1.2
    "193_49.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 193_69_anim:
    "193_69.webp" with Dissolve(.3)
    pause 1.2
    "193_70.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 196_21_anim:
    "196_21.webp" with Dissolve(.3)
    pause 1.2
    "196_22.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 196_33_anim:
    "196_33.webp" with Dissolve(.3)
    pause 0.8
    "196_34.webp" with Dissolve(.3)
    pause 0.8
    repeat

image 196_47_anim:
    "196_47.webp" with Dissolve(.3)
    pause 1.2
    "196_48.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 198_59_anim:
    "images/0200/198_59.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/198_60.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 198_77_anim:
    "images/0200/198_77.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/198_78.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 201_04_anim:
    "images/0200/201_04.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/201_05.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 201_41_anim:
    "images/0200/201_41.webp" with Dissolve(.3)
    pause 1.5
    "images/0200/201_42.webp" with Dissolve(.3)
    pause 1.5
    repeat

image 201_101_anim:
    "images/0200/201_101.webp" with Dissolve(.2)
    pause 0.4
    "images/0200/201_102.webp" with Dissolve(.2)
    pause 0.4
    repeat

image 201_107_anim:
    "images/0200/201_107.webp" with Dissolve(.1)
    pause 0.1
    "images/0200/201_108.webp" with Dissolve(.1)
    pause 0.1
    repeat

image 201_109_anim:
    "images/0200/201_109.webp" with Dissolve(.1)
    pause 0.1
    "images/0200/201_110.webp" with Dissolve(.1)
    pause 0.1
    repeat

image 201_111_anim:
    "images/0200/201_111.webp" with Dissolve(.1)
    pause 0.1
    "images/0200/201_112.webp" with Dissolve(.1)
    pause 0.1
    repeat

image 201_113_anim:
    "images/0200/201_113.webp" with Dissolve(.1)
    pause 0.1
    "images/0200/201_114.webp" with Dissolve(.1)
    pause 0.1
    repeat

image 201_169_anim:
    "images/0200/201_169.webp" with Dissolve(.2)
    pause 0.4
    "images/0200/201_170.webp" with Dissolve(.2)
    pause 0.4
    repeat

image 201_172_anim:
    "images/0200/201_172.webp" with Dissolve(.2)
    pause 0.4
    "images/0200/201_173.webp" with Dissolve(.2)
    pause 0.4
    repeat

image 201_174_anim:
    "images/0200/201_174.webp" with Dissolve(.2)
    pause 0.4
    "images/0200/201_175.webp" with Dissolve(.2)
    pause 0.4
    repeat

image 202_33_anim:
    "images/0200/202_33.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/202_34.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 202_108_anim:
    "images/0200/202_108.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/202_109.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 204_13_anim:
    "images/0200/204_13.webp" with Dissolve(.3)
    pause 0.7
    "images/0200/204_14.webp" with Dissolve(.3)
    pause 0.7
    repeat

image 206_16_anim:
    "images/0200/206_16.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/206_17.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 206_62_anim:
    "images/0200/206_62.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/206_63.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 206_72_anim:
    "images/0200/206_72.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/206_73.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 206_126_anim:
    "images/0200/206_126.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/206_127.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 206_131_anim:
    "images/0200/206_131.webp" with Dissolve(.2)
    pause 0.4
    "images/0200/206_132.webp" with Dissolve(.2)
    pause 0.4
    repeat

image 207_78_anim:
    "images/0200/207_78.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/207_79.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 207_80_anim:
    "images/0200/207_80.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/207_81.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 208_22_anim:
    "images/0200/208_22.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/208_23.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 208_48_anim:
    "images/0200/208_48.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/208_49.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 208_52_anim:
    "images/0200/208_52.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/208_53.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 208_69_anim:
    "images/0200/208_69.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/208_70.webp" with Dissolve(.3)
    pause 1.2
    repeat

image 208_118_anim:
    "images/0200/208_118.webp" with Dissolve(.3)
    pause 1.2
    "images/0200/208_119.webp" with Dissolve(.3)
    pause 1.2
    repeat



image park_01 = "map/park_01.png"
image park_02 = "map/park_02.png"
image library_01 = "map/library_01.png"
image library_02 = "map/library_02.png"
image library_03 = "map/library_03.png"
image square_01 = "map/square_01.png"
image square_02 = "map/square_02.png"
image square_03 = "map/square_03.png"
image downtown_plate = "map/downtown_plate.png"
image pool_01 = "map/pool_01.png"
image pool_02 = "map/pool_02.png"
image supermarket_01 = "map/supermarket_01.png"
image supermarket_02 = "map/supermarket_02.png"
image supermarket_03 = "map/supermarket_03.png"
image mixed_bath_01 = "map/mixed_bath_01.png"
image school_01 = "map/school_01.png"
image school_02 = "map/school_02.png"
image school_03 = "map/school_03.png"
image school_04 = "map/school_04.png"
image school_class = "map/school_class.png"
image school_female = "map/school_female.png"
image school_male = "map/school_male.png"
image school_roof = "map/school_roof.png"
image school_teacher = "map/school_teacher.png"
image school_study = "map/school_study.png"
image bar_01 = "map/bar_01.png"
image bar_02 = "map/bar_02.png"
image gym_01 = "map/gym_01.png"
image gym_02 = "map/gym_02.png"
image gym_03 = "map/gym_03.png"
image bar_01 = "map/bar_01.png"
image bar_02 = "map/bar_02.png"
image bank_01 = "map/bank_01.png"
image club_01 = "map/club_01.png"
image club_02 = "map/club_02.png"
image photo_studio = "map/photo_studio.png"
image nuclear_01 = "map/nuclear_01.png"


default school_class_ocupada = False





image b_school = "images/b_school.webp"

image b01_1 = "images/b01_1.webp"
image b01_2 = "images/b01_2.webp"
image b01_3 = "images/b01_3.webp"
image b01_4 = "images/b01_4.webp"
image b01_5 = "images/b01_5.webp"
image b03_01 = "images/b03_01.webp"
image b03_02 = "images/b03_02.webp"
image b07_01 = "images/b07_01.webp"
image b07_02 = "images/b07_02.webp"
image b07_03 = "images/b07_03.webp"
image b07_04 = "images/b07_04.webp"

image b06_01 = "images/b06_01.webp"
image b06_02 = "images/b06_02.webp"

image 01_4 = "images/01_4.webp"
image 01_5 = "images/01_5.webp"
image 01_6 = "images/01_6.webp"
image 01_7 = "images/01_7.webp"
image 01_8 = "images/01_8.webp"

image 01_11 = "images/01_11.webp"
image 01_12 = "images/01_12.webp"
image 01_13 = "images/01_13.webp"
image 01_14 = "images/01_14.webp"
image 01_15 = "images/01_15.webp"
image 01_16 = "images/01_16.webp"
image 01_17 = "images/01_17.webp"
image 01_18 = "images/01_18.webp"
image 01_19 = "images/01_19.webp"
image 01_20 = "images/01_20.webp"
image 01_21 = "images/01_21.webp"
image 01_22 = "images/01_22.webp"

image 03_1 = "images/03_1.webp"
image 03_2 = "images/03_2.webp"
image 03_3 = "images/03_3.webp"
image 03_4 = "images/03_4.webp"

image 04_1 = "images/04_1.webp"
image 04_2 = "images/04_2.webp"
image 04_3 = "images/04_3.webp"
image 04_4 = "images/04_4.webp"
image 04_5 = "images/04_5.webp"
image 04_6 = "images/04_6.webp"
image 04_7 = "images/04_7.webp"
image 04_8 = "images/04_8.webp"
image 04_9 = "images/04_9.webp"
image 04_10 = "images/04_10.webp"
image 04_11 = "images/04_11.webp"
image 04_12 = "images/04_12.webp"
image 04_13 = "images/04_13.webp"
image 04_14 = "images/04_14.webp"
image 04_15 = "images/04_15.webp"
image 04_16a = "images/04_16a.webp"
image 04_16b = "images/04_16b.webp"
image 04_17 = "images/04_17.webp"
image 04_18 = "images/04_18.webp"
image 04_19 = "images/04_19.webp"
image 04_20 = "images/04_20.webp"
image 04_21 = "images/04_21.webp"
image 04_22 = "images/04_22.webp"
image 04_23 = "images/04_23.webp"
image 04_24 = "images/04_24.webp"
image 04_25 = "images/04_25.webp"
image 04_26 = "images/04_26.webp"
image 04_27 = "images/04_27.webp"
image 04_28 = "images/04_28.webp"
image 04_29 = "images/04_29.webp"
image 04_30 = "images/04_30.webp"
image 04_31 = "images/04_31.webp"
image 04_32 = "images/04_32.webp"
image 04_33 = "images/04_33.webp"
image 04_34 = "images/04_34.webp"
image 04_35 = "images/04_35.webp"
image 04_36 = "images/04_36.webp"
image 04_37 = "images/04_37.webp"
image 04_38 = "images/04_38.webp"
image 04_39 = "images/04_39.webp"
image 04_40 = "images/04_40.webp"
image 04_41 = "images/04_41.webp"
image 04_42 = "images/04_42.webp"
image 04_43 = "images/04_43.webp"
image 04_44 = "images/04_44.webp"

image 05_01 = "images/05_01.webp"
image 05_02 = "images/05_02.webp"
image 05_03 = "images/05_03.webp"
image 05_04 = "images/05_04.webp"
image 05_05 = "images/05_05.webp"
image 05_06 = "images/05_06.webp"
image 05_07 = "images/05_07.webp"
image 05_08 = "images/05_08.webp"
image 05_09 = "images/05_09.webp"
image 05_10 = "images/05_10.webp"
image 05_11 = "images/05_11.webp"
image 05_12 = "images/05_12.webp"
image 05_13 = "images/05_13.webp"
image 05_14 = "images/05_14.webp"
image 05_15 = "images/05_15.webp"
image 05_16 = "images/05_16.webp"
image 05_17 = "images/05_17.webp"
image 05_18 = "images/05_18.webp"
image 05_19 = "images/05_19.webp"
image 05_20 = "images/05_20.webp"
image 05_21 = "images/05_21.webp"
image 05_22 = "images/05_22.webp"
image 05_23 = "images/05_23.webp"
image 05_24 = "images/05_24.webp"
image 05_25 = "images/05_25.webp"
image 05_26 = "images/05_26.webp"
image 05_27 = "images/05_27.webp"
image 05_28 = "images/05_28.webp"
image 05_29 = "images/05_29.webp"
image 05_30 = "images/05_30.webp"
image 05_31 = "images/05_31.webp"
image 05_32 = "images/05_32.webp"
image 05_33 = "images/05_33.webp"
image 05_34 = "images/05_34.webp"
image 05_35 = "images/05_35.webp"
image 05_36 = "images/05_36.webp"
image 05_37 = "images/05_37.webp"
image 05_38 = "images/05_38.webp"
image 05_39 = "images/05_39.webp"
image 05_40 = "images/05_40.webp"
image 05_41 = "images/05_41.webp"
image 05_42 = "images/05_42.webp"
image 05_43 = "images/05_43.webp"
image 05_44 = "images/05_44.webp"
image 05_45 = "images/05_45.webp"
image 05_46 = "images/05_46.webp"
image 05_47 = "images/05_47.webp"
image 05_48 = "images/05_48.webp"
image 05_49 = "images/05_49.webp"
image 05_50 = "images/05_50.webp"
image 05_51 = "images/05_51.webp"
image 05_52 = "images/05_52.webp"
image 05_53 = "images/05_53.webp"
image 05_54 = "images/05_54.webp"
image 05_55 = "images/05_55.webp"
image 05_56 = "images/05_56.webp"

image 07_01 = "images/07_01.webp"
image 07_02 = "images/07_02.webp"
image 07_03 = "images/07_03.webp"
image 07_04 = "images/07_04.webp"
image 07_05 = "images/07_05.webp"
image 07_06 = "images/07_06.webp"
image 07_07 = "images/07_07.webp"
image 07_08 = "images/07_08.webp"
image 07_09 = "images/07_09.webp"
image 07_10 = "images/07_10.webp"
image 07_11 = "images/07_11.webp"
image 07_12 = "images/07_12.webp"
image 07_13 = "images/07_13.webp"
image 07_14 = "images/07_14.webp"
image 07_15 = "images/07_15.webp"
image 07_16 = "images/07_16.webp"
image 07_17 = "images/07_17.webp"
image 07_18 = "images/07_18.webp"
image 07_19 = "images/07_19.webp"
image 07_20 = "images/07_20.webp"
image 07_21 = "images/07_21.webp"
image 07_22 = "images/07_22.webp"
image 07_23 = "images/07_23.webp"
image 07_24 = "images/07_24.webp"
image 07_25 = "images/07_25.webp"
image 07_26 = "images/07_26.webp"
image 07_27 = "images/07_27.webp"
image 07_28 = "images/07_28.webp"
image 07_29 = "images/07_29.webp"
image 07_30 = "images/07_30.webp"
image 07_31 = "images/07_31.webp"
image 07_32 = "images/07_32.webp"
image 07_33 = "images/07_33.webp"
image 07_34 = "images/07_34.webp"
image 07_35 = "images/07_35.webp"
image 07_36 = "images/07_36.webp"
image 07_37 = "images/07_37.webp"
image 07_38 = "images/07_38.webp"
image 07_39 = "images/07_39.webp"
image 07_40 = "images/07_40.webp"
image 07_41 = "images/07_41.webp"

image 09_01 = "images/09_01.webp"
image 09_02 = "images/09_02.webp"
image 09_03 = "images/09_03.webp"
image 09_04 = "images/09_04.webp"
image 09_05 = "images/09_05.webp"
image 09_06 = "images/09_06.webp"
image 09_07 = "images/09_07.webp"
image 09_08 = "images/09_08.webp"
image 09_09 = "images/09_09.webp"
image 09_10 = "images/09_10.webp"
image 09_11 = "images/09_11.webp"
image 09_12 = "images/09_12.webp"
image 09_13 = "images/09_13.webp"
image 09_14 = "images/09_14.webp"
image 09_16 = "images/09_16.webp"
image 09_17 = "images/09_17.webp"
image 09_18 = "images/09_18.webp"
image 09_19 = "images/09_19.webp"
image 09_20 = "images/09_20.webp"
image 09_21 = "images/09_21.webp"
image 09_22 = "images/09_22.webp"
image 09_23 = "images/09_23.webp"
image 09_24 = "images/09_24.webp"
image 09_25 = "images/09_25.webp"
image 09_26 = "images/09_26.webp"
image 09_27 = "images/09_27.webp"
image 09_28 = "images/09_28.webp"
image 09_29 = "images/09_29.webp"
image 09_30 = "images/09_30.webp"
image 09_31 = "images/09_31.webp"
image 09_32 = "images/09_32.webp"
image 09_33 = "images/09_33.webp"
image 09_34 = "images/09_34.webp"
image 09_35 = "images/09_35.webp"
image 09_36 = "images/09_36.webp"
image 09_37 = "images/09_37.webp"
image 09_38 = "images/09_38.webp"
image 09_39 = "images/09_39.webp"
image 09_40 = "images/09_40.webp"
image 09_41 = "images/09_41.webp"

image 17_01 = "images/17_01.webp"
image 17_02 = "images/17_02.webp"
image 17_03 = "images/17_03.webp"
image 17_04 = "images/17_04.webp"
image 17_05 = "images/17_05.webp"
image 17_06 = "images/17_06.webp"
image 17_07 = "images/17_07.webp"
image 17_08 = "images/17_08.webp"
image 17_09 = "images/17_09.webp"
image 17_10 = "images/17_10.webp"
image 17_11 = "images/17_11.webp"
image 17_12 = "images/17_12.webp"
image 17_13 = "images/17_13.webp"
image 17_14 = "images/17_14.webp"
image 17_15 = "images/17_15.webp"
image 17_16 = "images/17_16.webp"
image 17_17 = "images/17_17.webp"
image 17_19 = "images/17_19.webp"
image 17_20 = "images/17_20.webp"
image 17_21 = "images/17_21.webp"
image 17_22 = "images/17_22.webp"
image 17_23 = "images/17_23.webp"
image 17_24 = "images/17_24.webp"
image 17_25 = "images/17_25.webp"
image 17_26 = "images/17_26.webp"
image 17_27 = "images/17_27.webp"
image 17_28 = "images/17_28.webp"
image 17_29 = "images/17_29.webp"
image 17_30 = "images/17_30.webp"
image 17_31 = "images/17_31.webp"
image 17_32 = "images/17_32.webp"
image 17_33 = "images/17_33.webp"
image 17_34 = "images/17_34.webp"
image 17_35 = "images/17_35.webp"

image 25_01 = "images/25_01.webp"
image 25_02 = "images/25_02.webp"
image 25_03 = "images/25_03.webp"
image 25_04 = "images/25_04.webp"
image 25_05 = "images/25_05.webp"
image 25_06 = "images/25_06.webp"
image 25_07 = "images/25_07.webp"
image 25_08 = "images/25_08.webp"
image 25_09 = "images/25_09.webp"
image 25_10 = "images/25_10.webp"
image 25_11 = "images/25_11.webp"
image 25_16 = "images/25_16.webp"
image 25_17 = "images/25_17.webp"
image 25_18 = "images/25_18.webp"
image 25_19 = "images/25_19.webp"
image 25_34 = "images/25_34.webp"
image 25_35 = "images/25_35.webp"
image 25_36 = "images/25_36.webp"
image 25_37 = "images/25_37.webp"
image 25_38 = "images/25_38.webp"
image 25_39 = "images/25_39.webp"
image 25_40 = "images/25_40.webp"
image 25_41 = "images/25_41.webp"
image 25_42 = "images/25_42.webp"
image 25_43 = "images/25_43.webp"
image 25_44 = "images/25_44.webp"
image 25_45 = "images/25_45.webp"
image 25_46 = "images/25_46.webp"
image 25_47 = "images/25_47.webp"
image 25_48 = "images/25_48.webp"
image 25_49 = "images/25_49.webp"
image 25_50 = "images/25_50.webp"
image 25_51 = "images/25_51.webp"
image 25_52 = "images/25_52.webp"
image 25_53 = "images/25_53.webp"
image 25_54 = "images/25_54.webp"
image 25_55 = "images/25_55.webp"
image 25_56 = "images/25_56.webp"
image 25_57 = "images/25_57.webp"
image 25_58 = "images/25_58.webp"
image 25_59 = "images/25_59.webp"
image 25_60 = "images/25_60.webp"
image 25_61 = "images/25_61.webp"
image 25_61b = "images/25_61b.webp"
image 25_62 = "images/25_62.webp"

image 34_01 = "images/34_01.webp"
image 34_02 = "images/34_02.webp"
image 34_03 = "images/34_03.webp"
image 34_04 = "images/34_04.webp"
image 34_05 = "images/34_05.webp"
image 34_06 = "images/34_06.webp"
image 34_07 = "images/34_07.webp"
image 34_08 = "images/34_08.webp"
image 34_09 = "images/34_09.webp"
image 34_10 = "images/34_10.webp"
image 34_11 = "images/34_11.webp"
image 34_12 = "images/34_12.webp"
image 34_13 = "images/34_13.webp"
image 34_14 = "images/34_14.webp"
image 34_15 = "images/34_15.webp"
image 34_16 = "images/34_16.webp"
image 34_17 = "images/34_17.webp"
image 34_18 = "images/34_18.webp"
image 34_19 = "images/34_19.webp"
image 34_20 = "images/34_20.webp"
image 34_21 = "images/34_21.webp"
image 34_22 = "images/34_22.webp"
image 34_23 = "images/34_23.webp"
image 34_24 = "images/34_24.webp"
image 34_25 = "images/34_25.webp"
image 34_26 = "images/34_26.webp"
image 34_27 = "images/34_27.webp"
image 34_28 = "images/34_28.webp"
image 34_29 = "images/34_29.webp"
image 34_30 = "images/34_30.webp"
image 34_31 = "images/34_31.webp"
image 34_32 = "images/34_32.webp"
image 34_33 = "images/34_33.webp"
image 34_34 = "images/34_34.webp"
image 34_35 = "images/34_35.webp"
image 34_36 = "images/34_36.webp"
image 34_37 = "images/34_37.webp"
image 34_38 = "images/34_38.webp"
image 34_39 = "images/34_39.webp"
image 34_40 = "images/34_40.webp"
image 34_41 = "images/34_41.webp"
image 34_42 = "images/34_42.webp"
image 34_43 = "images/34_43.webp"
image 34_44 = "images/34_44.webp"
image 34_45 = "images/34_45.webp"
image 34_46 = "images/34_46.webp"
image 34_47 = "images/34_47.webp"
image 34_48 = "images/34_48.webp"
image 34_49 = "images/34_49.webp"
image 34_50 = "images/34_50.webp"
image 34_51 = "images/34_51.webp"
image 34_52 = "images/34_52.webp"
image 34_53 = "images/34_53.webp"
image 34_54 = "images/34_54.webp"
image 34_55 = "images/34_55.webp"
image 34_56 = "images/34_56.webp"
image 34_57 = "images/34_57.webp"

image 37_01 = "images/37_01.webp"
image 37_02 = "images/37_02.webp"
image 37_03 = "images/37_03.webp"
image 37_04 = "images/37_04.webp"
image 37_05 = "images/37_05.webp"
image 37_06 = "images/37_06.webp"
image 37_07 = "images/37_07.webp"
image 37_08 = "images/37_08.webp"
image 37_09 = "images/37_09.webp"
image 37_10 = "images/37_10.webp"
image 37_11 = "images/37_11.webp"
image 37_12 = "images/37_12.webp"
image 37_13 = "images/37_13.webp"
image 37_14 = "images/37_14.webp"
image 37_15 = "images/37_15.webp"
image 37_15_2 = "images/37_15_2.webp"
image 37_16 = "images/37_16.webp"
image 37_17 = "images/37_17.webp"
image 37_18 = "images/37_18.webp"
image 37_19 = "images/37_19.webp"
image 37_20 = "images/37_20.webp"
image 37_21 = "images/37_21.webp"
image 37_22 = "images/37_22.webp"
image 37_23 = "images/37_23.webp"
image 37_24 = "images/37_24.webp"
image 37_25 = "images/37_25.webp"
image 37_27 = "images/37_27.webp"
image 37_28 = "images/37_28.webp"
image 37_29 = "images/37_29.webp"
image 37_30 = "images/37_30.webp"
image 37_31 = "images/37_31.webp"
image 37_32 = "images/37_32.webp"
image 37_33 = "images/37_33.webp"
image 37_34 = "images/37_34.webp"
image 37_35 = "images/37_35.webp"
image 37_36 = "images/37_36.webp"
image 37_37 = "images/37_37.webp"
image 37_38 = "images/37_38.webp"
image 37_39 = "images/37_39.webp"
image 37_40 = "images/37_40.webp"
image 37_41 = "images/37_41.webp"
image 37_41_2 = "images/37_41_2.webp"
image 37_42 = "images/37_42.webp"
image 37_43 = "images/37_43.webp"
image 37_44 = "images/37_44.webp"
image 37_45 = "images/37_45.webp"
image 37_46 = "images/37_46.webp"
image 37_47 = "images/37_47.webp"
image 37_48 = "images/37_48.webp"
image 37_49 = "images/37_49.webp"
image 37_50 = "images/37_50.webp"
image 37_51 = "images/37_51.webp"
image 37_52 = "images/37_52.webp"
image 37_53 = "images/37_53.webp"
image 37_54 = "images/37_54.webp"
image 37_55 = "images/37_55.webp"
image 37_56 = "images/37_56.webp"
image 37_57_1 = "images/37_57_1.webp"
image 37_57_2 = "images/37_57_2.webp"
image 37_57_3 = "images/37_57_3.webp"
image 37_57_4 = "images/37_57_4.webp"
image 37_57_5 = "images/37_57_5.webp"
image 37_57_6 = "images/37_57_6.webp"
image 37_57_7 = "images/37_57_7.webp"
image 37_58 = "images/37_58.webp"
image 37_59 = "images/37_59.webp"
image 37_60 = "images/37_60.webp"
image 37_61 = "images/37_61.webp"
image 37_62 = "images/37_62.webp"
image 37_63 = "images/37_63.webp"
image 37_64 = "images/37_64.webp"
image 37_65 = "images/37_65.webp"
image 37_66 = "images/37_66.webp"
image 37_67 = "images/37_67.webp"
image 37_68 = "images/37_68.webp"
image 37_69 = "images/37_69.webp"
image 37_70 = "images/37_70.webp"
image 37_71 = "images/37_71.webp"
image 37_72 = "images/37_72.webp"
image 37_73 = "images/37_73.webp"
image 37_74 = "images/37_74.webp"
image 37_75 = "images/37_75.webp"
image 37_76 = "images/37_76.webp"
image 37_77 = "images/37_77.webp"
image 37_78 = "images/37_78.webp"
image 37_79 = "images/37_79.webp"
image 37_80 = "images/37_80.webp"


image b03_01 = "images/b03_01.webp"
image b03_02 = "images/b03_02.webp"
image b03_03 = "images/b03_03.webp"
image b03_04 = "images/b03_04.webp"

image b_bed = "images/b_bed.webp"

image map_market_blank = "images/map_market_blank.webp"




default email_1 = False
default email_2 = False
default email_3 = False
default email_4 = False
default email_5 = False
default email_6 = False
default email_7 = False
default email_8 = False
default email_9 = False
default email_10 = False
default email_11 = False
default email_12 = False
default email_13 = False
default email_14 = False
default email_15 = False
default email_16 = False
default email_17 = False
default email_18 = False
default email_19 = False
default email_20 = False



style alpha_buttons:
    focus_mask True












label splashscreen:
    show text "{b}{size=32}Warning:{/size}{/b}\n\nThis game contains sex scenes and should only be played by adults."
    call screen age_confirmation
    return

screen age_confirmation():
    vbox:
        xalign 0.5
        yalign 0.7
        textbutton "Click here if you are over 18 years old." action Jump("continua_jogo")

label continua_jogo:
    return



define config.language = "chinese"
label start:
##############  start  起始点  ############火车王社区#############



   

      
 menu:
        "开始游戏":
            pass

#-------------  start 结束点  -------------------------

    $ quick_menu = False

    scene black with fade

    show text "Game made by TK8000. Check {a=http://www.patreon.com/tkcorp8000}my patreon{/a} for more games.\nClick to continue..." with dissolve

    $ renpy.pause()

    show text "All images were generated using Honey Select from Illusion. {a=http://www.illusion.jp/}www.illusion.jp{/a}" with dissolve

    $ renpy.pause()

    hide text with dissolve

    label select_mode:

        scene map_school_blank with Dissolve(0.3)

        call screen game_mode

    label start_prologue:

        scene black with fade

        show screen watermark

        $ quick_menu = True

        jump event_prologue





    label core_daystart:
        $ random_event_switch = True
        $ data += 1

        if data == 50:
            if game_mode == 0:
                "ENDING GAME"

        play music "music/bensound-thejazzpiano.mp3"

        if game_mode == 0:
            "MORNING OF THE DAY [data]/50."

        if game_mode == 1:
            "MORNING OF THE DAY [data]."

        $ prob_anastacia = renpy.random.randint(1, 10)
        $ prob_aya = renpy.random.randint(1, 10)
        $ prob_lucy = renpy.random.randint(1, 10)
        $ prob_kyra = renpy.random.randint(1, 10)
        $ prob_tatiana = renpy.random.randint(1, 10)
        $ prob_lisa = renpy.random.randint(1, 10)
        $ prob_sabrina = renpy.random.randint(1, 10)
        $ prob_amanda = renpy.random.randint(1, 10)
        $ prob_miranda = renpy.random.randint(1, 10)
        $ prob_alexandra = renpy.random.randint(1, 10)
        $ prob_sarah = renpy.random.randint(1, 10)
        $ prob_alanna = renpy.random.randint(1, 10)
        $ prob_adele = renpy.random.randint(1, 10)
        $ prob_verdi = renpy.random.randint(1, 10)
        $ prob_tifa = renpy.random.randint(1, 10)
        $ prob_suki = renpy.random.randint(1, 10)
        $ prob_laura = renpy.random.randint(1, 10)
        $ prob_lara = renpy.random.randint(1, 10)

        $ date_ok = True






        if data >= 5:
            if not lara_level_1:
                jump event_lara_level_1


        if data >= 15:
            if not event_lara_level_2:
                jump event_lara_level_2


        if event_kyra_1 and data >= kyra_sp1_trigger:
            if event_kyra_sp_1 == False:
                jump event_kyra_special_1


        if event_kyra_level_3 and not event_kyra_bukkake:
            jump event_kyra_bukkake


        if event_kyra_bukkake and not event_stella_market:
            jump event_stella_market


        if event_lucy_2:
            if not event_lucy_sp_1:
                jump event_lucy_special_1


        if event_lucy_3 and data >= lucy_sp2_trigger:
            if not event_lucy_sp_2:
                jump event_lucy_special_2


        if event_lucy_4:
            if not event_lucy_sp_3:
                jump event_lucy_special_3


        if event_tatiana_1 and event_lucy_sp_1 and not event_tatiana_remake_01:
            jump event_tatiana_remake_01


        if event_tatiana_remake_01 and not event_tatiana_remake_02:
            jump event_tatiana_remake_02












        if event_tatiana_remake_06 and not event_tatiana_special_4:
            jump event_tatiana_special_4






        if event_call_linda and saori_and_linda_trigger <= data:
            if not event_saori_and_linda:
                jump event_saori_and_linda


        if event_saori_and_sarah and event_lucy_house:
            if not event_sarah_school:
                jump event_sarah_school


        if event_sarah_school_2 and not event_sarah_school_3:
            jump event_sarah_school_3


        if event_lisa_1 and lisa_sp1_trigger <= data:
            if not event_lisa_special_1:
                jump event_lisa_special_1


        if event_aya_2 and not event_aya_special_1:
            jump event_aya_special_1


        if event_anastacia_2 and not event_anastacia_special_1:
            jump event_anastacia_special_1


        if event_miranda_level_1 and not event_miranda_special_1:
            jump event_miranda_special_1


        if event_miranda_level_2 and not event_miranda_special_2:
            jump event_miranda_special_2


        if event_aurora_1 and not event_miranda_special_3:
            jump event_miranda_special_3


        if event_miranda_level_3 and not event_miranda_special_4:
            jump event_miranda_special_4


        if event_lisa_special_1 and not event_lisa_special_2:
            jump event_lisa_special_2


        if event_adria_2 and not event_miranda_special_5:
            jump event_miranda_special_5


        if event_miranda_house and not event_miranda_special_6:
            jump event_miranda_special_6


        if event_lisa_level_4 and not event_lisa_special_3:
            jump event_lisa_special_3


        if event_suki_01 and not event_suki_02:
            jump event_suki_02



        "It's time to go to school."

        scene b_school with fade

        "The class passed without anything noteworthy."

        scene black with fade

        if map_mode == 0:
            jump list_mode
        if map_mode == 1:
            jump atlas_mode








    label core_dayend:
        play music "music/clock.ogg"
        "Later that night..."

        if sw_cena_noite:
            scene b_bed with fade

            ale "Ahh!! I need to sleep."

        $ sw_cena_noite = True

        if event_shibuya_5:
            scene b_bed_2 with fade
        elif True:
            if not event_shibuya_2:
                scene b_bed_2 with fade
            elif True:
                if not event_shibuya_3:
                    scene b_bed_3 with fade
                elif True:
                    scene b_bed_4 with fade

        if game_mode == 0:
            "END OF DAY [data]/50."

        if game_mode == 1:
            "END OF DAY [data]."

        stop music fadeout 1.0

        scene black with fade

        if alex_status_int > 100:
            $ alex_status_int = 100

        if alex_status_str > 100:
            $ alex_status_str = 100

        if invest != 0:
            $ money_before = money
            $ money = money + juros
            $ renpy.choice_for_skipping()
            show text "Alex current status:\n\nMoney before: [money_before]\nInvested money: [invest]\nInvestment profit: [juros]\nActual money: [money]\n\nStrength: [alex_status_str]\nIntelligence: [alex_status_int]\nAppearance: [alex_status_app]"
        elif True:

            $ renpy.choice_for_skipping()
            show text "Alex current status:\n\nMoney: [money]\n\nStrength: [alex_status_str]\nIntelligence: [alex_status_int]\nAppearance: [alex_status_app]"

        $ renpy.pause()

        hide text

        jump core_daystart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

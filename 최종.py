import pygame
import random
import os

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

# pygame 초기화
pygame.init()

# FPS 설정
clock = pygame.time.Clock()

# 게임 이름
pygame.display.set_caption("고준영 과제")

# sound
bgm = pygame.mixer.Sound("./resources/Someday_Roa.ogg")
bgm.set_volume(0.5)
bgm.play(-1)

# bgm이 현재 틀어져있나 체크하는 변수
bgm_i = 1

# sound files
ks_sound = pygame.mixer.Sound("./resources/fart.ogg")
dead_sound = pygame.mixer.Sound("./resources/fart_sound.ogg")
hb_sound = pygame.mixer.Sound("./resources/heartbeat.ogg")

# 폰트 설정
korean_font_path = 'your_korean_font_file.ttf'
game_font = pygame.font.Font(korean_font_path, 30)
game_font2 = pygame.font.Font(korean_font_path, 35)
game_font3 = pygame.font.Font(korean_font_path, 25)

# 나의 이름
my_name = game_font3.render("고준영", True, (255, 255, 255))
the_end = game_font2.render("THE END", True, (0, 0, 0))
date = game_font3.render("2023-11-21", True, (255, 255, 255))

# screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# background
background = pygame.image.load("./resources/bg2.png")
bg = [pygame.image.load("./resources/bg2.png"),
      pygame.image.load("./resources/bg21.png"),
      pygame.image.load("./resources/bg22.png"),
      pygame.image.load("./resources/bg23.png"),
      pygame.image.load("./resources/bg25.png")]

# title background
t_background = pygame.image.load("./resources/astro_2_2.jpg")

# help background
h_background = pygame.image.load("./resources/astro_help6.jpg")

lf_run = False
ud_run = False
h_run = False
run_ending = False

# character image
character_left = pygame.image.load("./resources/dog4.png")
character_right = pygame.image.load("./resources/dog3.png")

# 음악 끄기 버튼 상태
music_on = True

# 음악 끄기 버튼 그리기
def draw_music_button():
    button_color = (0, 255, 0) if music_on else (255, 0, 0)
    pygame.draw.rect(screen, button_color, (screen_width - 100, 10, 90, 40))
    text = game_font.render("음악 끄기" if music_on else "음악 켜기", True, (255, 255, 255))
    screen.blit(text, (screen_width - 95, 15))

# 타이틀 화면부터 결과 화면을 반복
run_all = True
while run_all:
    if bgm_i == 0:
        bgm.play(-1)
        bgm_i = 1
    bgm_e = 0
    score = 0

    # 상하 방향키로 선택을 도와주는 변수 (key select)
    ks = 0

    # 타이틀 화면
    run = True
    while run:
        for event in pygame.event.get():
            # X 버튼으로 프로그램 종료
            if event.type == pygame.QUIT:
                run = False
                running = False
                run_all = False

            # 마우스 클릭으로 음악 끄기 버튼 처리
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if screen_width - 100 <= mouse_x <= screen_width - 10 and 10 <= mouse_y <= 50:
                    music_on = not music_on
                    if music_on:
                        bgm.play(-1)
                    else:
                        bgm.stop()

            # 키보드 입력 받기
            if event.type == pygame.KEYDOWN:
                # ESC 키로 종료
                if event.key == pygame.K_ESCAPE:
                    run = False
                    running = False
                    run_all = False

                # 아래 방향키를 누르면
                if event.key == pygame.K_DOWN:
                    ks_sound.play()
                    if ks < 3:
                        ks += 1
                # 위 방향키를 누르면
                if event.key == pygame.K_UP:
                    ks_sound.play()
                    if ks > 0:
                        ks -= 1

                # 엔터 키를 누르면 ks 값에 따라 다음 화면으로 넘어감
                if event.key == pygame.K_RETURN:
                    ks_sound.play()
                    if ks == 0:
                        lf_run = True
                        run = False
                    if ks == 1:
                        ud_run = True
                        run = False
                    if ks == 2:
                        h_run = True
                        run = False
                    if ks == 3:
                        run = False
                        running = False
                        run_all = False

        screen.blit(t_background, (0, 0))

        # 음악 끄기 버튼 그리기
        draw_music_button()

        # 메뉴 기본 폰트 설정
        start_button = game_font.render("좌우 피하기", True, (255, 255, 255))
        updown_button = game_font.render("위아래 피하기", True, (255, 255, 255))
        help_button = game_font.render("도움말", True, (255, 255, 255))
        quit_button = game_font.render("게임 나가기", True, (255, 255, 255))

        # ks의 값(상하 방향키로 선택한 메뉴 파란색으로 강조)
        if ks == 0:
            start_button = game_font2.render("좌우 피하기", True, (154, 218, 255))
        if ks == 1:
            updown_button = game_font2.render("위아래 피하기", True, (154, 218, 255))
        elif ks == 2:
            help_button = game_font2.render("도움말", True, (154, 218, 255))
        elif ks == 3:
            quit_button = game_font2.render("게임 나가기", True, (154, 218, 255))

        # 각 글자들을 화면 중앙에 배치하기 위해 길이를 구해준다
        start_button_size = start_button.get_rect().size
        start_button_width = start_button_size[0]
        help_button_size = help_button.get_rect().size
        help_button_width = help_button_size[0]
        quit_button_size = quit_button.get_rect().size
        quit_button_width = quit_button_size[0]

        # screen blit
        screen.blit(my_name, (340, 600))
        screen.blit(date, (17, 600))
        screen.blit(start_button, ((screen_width / 2) - (start_button_width / 2), 150))
        screen.blit(updown_button, ((screen_width / 2) - (quit_button_width / 2), 257))
        screen.blit(help_button, ((screen_width / 2) - (help_button_width / 2), 365))
        screen.blit(quit_button, ((screen_width / 2) - (quit_button_width / 2), 472))

        pygame.display.update()

# pygame 종료
pygame.quit()

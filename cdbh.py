import pygame
from moviepy.editor import VideoFileClip

pygame.init()
clip = VideoFileClip("video/1st.mp4")
clip_duration = clip.duration
clip1 =VideoFileClip("video/2nd.mp4")
clip_duration1 = clip1.duration
clip2 =VideoFileClip("video/3rd.mp4")
clip_duration2 = clip2.duration
screen = pygame.display.set_mode((800, 550), pygame.RESIZABLE)
time = pygame.time.Clock()
score = 0

font_small = pygame.font.SysFont("Verdana", 20)
bg1 = pygame.image.load("images/menu.png")
bg2 = pygame.image.load("images/cafe.png")
bg3= pygame.image.load("images/salta.png")
bg4 = pygame.image.load("images/kuka.png")
question_1 = pygame.font.SysFont("Verdana",30)
bg_text = pygame.font.SysFont("Verdana",50)
bg_text1 = pygame.font.SysFont("Verdana",50)
win_text = pygame.font.SysFont("Verdana",50)
cafe_ans = "didn't choose"
location = "menu"
score_added = False
score_added1 = False
video_finished = False 
video_started = False 
video_finished1 = False 
video_started1 = False
video_finished2 = False 
video_started2 = False
last_q= False

def play_video(clip):
    global video_finished
    for frame in clip.iter_frames(fps=24, dtype='uint8'):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.time.wait(int(1000 / 24))
    video_finished = True 
def play_video1(clip1):
    global video_finished1
    for frame in clip1.iter_frames(fps=24, dtype='uint8'):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.time.wait(int(1000 / 24))
    video_finished1=True
def play_video2(clip2):
    global video_finished2
    for frame in clip2.iter_frames(fps=24, dtype='uint8'):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.time.wait(int(1000 / 24))
    video_finished2=True
done = True
while done:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (650, 10, 140, 30))
    scores = font_small.render("Score: " + str(score), True, (255, 255, 255))
    if location == "menu":
        screen.blit(bg1, (0, 0))
        screen.blit(bg_text.render("To start game", True, (255, 255, 255)), (250, 150))
        screen.blit(bg_text1.render("Press 1", True, (255, 255, 255)), (255, 200))

    if location == "video" and not video_started:
        pygame.mixer.Sound("music/1st.mp3").play()
        play_video(clip)
        video_started = True
    if location =="video1" and not video_started1:
        pygame.mixer.Sound("music/2nd.mp3").play()
        play_video1(clip1)
        video_started1 = True
    if location =="video2" and not video_started2:
        pygame.mixer.Sound("music/3rd.mp3").play()
        play_video2(clip2)
        video_started2 = True
    if video_finished:
        location = "cafe"
    if video_finished1:
        location = "Salta"
    if video_finished2:
        location = "kuka"
    if location == "cafe":
        screen.blit(bg2, (0, 0))
        screen.blit(question_1.render("Who killed Saltanat?", True, (255, 255, 255)), (250, 150))
        get_pressed = pygame.key.get_pressed()
        if not score_added:
            if get_pressed[pygame.K_a]:
                score+=25
                score_added = True
            elif get_pressed[pygame.K_b]:
                score+=20
                score_added = True
            elif get_pressed[pygame.K_c]:
                score+=15
                score_added = True
            elif get_pressed[pygame.K_d]:
                score+=15
                score_added = True
    if location == "Salta":
        screen.blit(bg3, (0, 0))
        get_pressed1 = pygame.key.get_pressed()
        if not score_added:
            if get_pressed1[pygame.K_a]:
                score+=25
                score_added = True
            elif get_pressed1[pygame.K_b]:
                score+=20
                score_added = True
            elif get_pressed1[pygame.K_c]:
                score+=15
                score_added = True
            elif get_pressed1[pygame.K_d]:
                score+=15
                score_added = True  
    if location == "kuka":
        screen.blit(bg4, (0, 0))
        get_pressed2 = pygame.key.get_pressed()
        if not score_added:
            if get_pressed2[pygame.K_a]:
                score+=20
                score_added = True
                last_q = True
            elif get_pressed2[pygame.K_b]:
                score+=20
                score_added = True
                last_q = True
            elif get_pressed2[pygame.K_c]:
                score+=15
                score_added = True
                last_q = True
            elif get_pressed2[pygame.K_d]:
                score+=25
                score_added = True 
                last_q = True
    if last_q:
        if score>=60:
            screen.fill("black")
            screen.blit(win_text.render("You won trial", True, (255, 255, 255)), (250, 150))
        else:
            screen.fill("black")
            screen.blit(win_text.render("You lost trial", True, (255, 255, 255)), (250, 150))  
    screen.blit(scores, (650, 10))   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and location == "menu":
                location = "video"
            if event.key == pygame.K_2 and location == "cafe":
                location="video1"
            if event.key == pygame.K_3 and location == "Salta":
                location='video2'
            if score_added:
                score_added=False
    pygame.display.update()
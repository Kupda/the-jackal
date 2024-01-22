import pygame


class Audio():
    def __init__(self) -> None:
        pygame.mixer.init()
        self.sounds = []
        self.click_sound = pygame.mixer.Sound('sounds/click.wav')
        self.shoot_sound = pygame.mixer.Sound('sounds/shoot.wav')
        self.click_sound = pygame.mixer.Sound('sounds/click.wav')
        self.steps_sound = pygame.mixer.Sound('sounds/steps.wav')
        self.dead_sound = pygame.mixer.Sound('sounds/dead.wav')
        self.crocodile_sound = pygame.mixer.Sound('sounds/crocodile.wav')
        pygame.mixer.music.load('sounds/music.wav')
        pygame.mixer.music.play(-1)
        self.music_muted = False
        self.sounds_muted = False
        self.sounds.append(self.click_sound)

    def mute_music(self):
        pygame.mixer.music.pause()
        self.music_muted = True
    
    def unmute_music(self):
        pygame.mixer.music.unpause()
        self.music_muted = False

    def toggle_music(self):
        if self.music_muted:
            self.unmute_music()
        else:
            self.mute_music()

    def mute_sounds(self):
        for sound in self.sounds:
            sound.set_volume(0)
        self.sounds_muted = True

    def unmute_sounds(self):
        for sound in self.sounds:
            sound.set_volume(1)
        self.sounds_muted = False

    def toggle_sounds(self):
        if self.sounds_muted:
            self.unmute_sounds()
        else:
            self.mute_sounds()


audio = Audio()
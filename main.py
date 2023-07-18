def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 2 2 f f f . . . . 
                    . . . f f f 2 2 2 2 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 2 2 2 2 2 2 e e f . . 
                    . . f e 2 f f f f f f 2 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f b f 4 4 f b f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f e e d d d d d d e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        leisurelarry,
        82,
        92)
    console.log_value("x", 66)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    music.ring_tone(698)
    music.play(music.create_song(assets.song("""
            win
        """)),
        music.PlaybackMode.UNTIL_DONE)
    game.game_over(True)
    print("END OF LINE")
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_on_overlap(sprite2, otherSprite):
    monkey.follow(leisurelarry, 55)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

projectile: Sprite = None
monkey: Sprite = None
leisurelarry: Sprite = None
music.play(music.create_song(assets.song("""
        startsong
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
scene.set_background_image(assets.image("""
    backg
"""))
tiles.set_current_tilemap(tilemap("""
    level1
"""))
myEnemy = 0
music.play(music.create_song(hex("""
        00780004080200
    """)),
    music.PlaybackMode.UNTIL_DONE)
leisurelarry = sprites.create(assets.image("""
    scull
"""), SpriteKind.player)
controller.move_sprite(leisurelarry)
scene.camera_follow_sprite(leisurelarry)
tiles.place_on_random_tile(leisurelarry, sprites.dungeon.collectible_insignia)
for index in range(4):
    monkey = sprites.create(assets.image("""
        monkey
    """), SpriteKind.enemy)
    tiles.place_on_random_tile(monkey, sprites.dungeon.chest_closed)
    monkey.follow(leisurelarry, 66)
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, leisurelarry, 82, 92)
    console.logValue("x", 69)
    console.log("YOUR FIRED!!!!!")
    console.logValue("YOURFIRED", 1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite) {
    monkey.follow(leisurelarry, 55)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    music.ringTone(698)
    music.play(music.createSong(assets.song`win`), music.PlaybackMode.UntilDone)
    game.gameOver(true)
    console.log("END OF LINE")
})
let projectile: Sprite = null
let monkey: Sprite = null
let leisurelarry: Sprite = null
let myEnemy = 5
music.play(music.createSong(assets.song`startsong`), music.PlaybackMode.LoopingInBackground)
scene.setBackgroundImage(assets.image`backg`)
tiles.setCurrentTilemap(tilemap`level1`)
leisurelarry = sprites.create(assets.image`scull`, SpriteKind.Player)
controller.moveSprite(leisurelarry)
scene.cameraFollowSprite(leisurelarry)
tiles.placeOnRandomTile(leisurelarry, sprites.dungeon.collectibleInsignia)
for (let index = 0; index < 4; index++) {
    monkey = sprites.create(assets.image`monkey`, SpriteKind.Enemy)
    tiles.placeOnRandomTile(monkey, sprites.dungeon.chestClosed)
    monkey.follow(leisurelarry, 66)
}
forever(function () {
    if (false) {
        myEnemy += 5
    } else if (false) {
    	
    } else {
    	
    }
})

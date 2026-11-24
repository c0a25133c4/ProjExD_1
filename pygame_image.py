import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # 練習1
    bg_img_fliped = pg.transform.flip(bg_img, True, False) # 練習8
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False) # 練習3
    kk_rct = kk_img.get_rect() # 練習10-1：こうかとんRectの取得
    kk_rct.center = 300, 200 # 練習10-2：こうかとん初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() # 練習10-3：全キーの状態の取得
        i = 0
        j = 0

        if key_lst[pg.K_UP]: # 練習10-4：上矢印キーが押されたら
            i = 0
            j = -1
            # kk_rct.move_ip((0, -1)) # 縦に-1動かす

        if key_lst[pg.K_DOWN]: # 練習10-4：下矢印キーが押されたら
            i = 0
            j = 1
            # kk_rct.move_ip((0, 1)) # 縦に1動かす

        if key_lst[pg.K_LEFT]: # 練習10-4：左矢印キーが押されたら
            i = -1
            j = 0
            # kk_rct.move_ip((-1, 0)) # 横に-1動かす

        if key_lst[pg.K_RIGHT]: # 練習10-4：右矢印キーが押されたら
            i = 2
            j = 0
            # kk_rct.move_ip((2, 0)) # 横に1動かす
        
        kk_rct.move_ip((i, j))

        x = tmr % 3200 # 練習5：背景画像移動用の変数　/ 練習9
        kk_rct.move_ip((-1, 0))
        screen.blit(bg_img, [-x, 0]) # 練習2
        screen.blit(bg_img_fliped, [-x+1600, 0]) # 練習7
        screen.blit(bg_img, [-x+3200, 0]) # 練習9
        # screen.blit(kk_img, [300, 200]) # 練習4
        screen.blit(kk_img, kk_rct) # 練習10-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) # 練習6：FPSの変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
import pygame
import sys
import random

# ========= Configuração =========
pygame.init()
LARGURA, ALTURA = 900, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong — Jogador vs IA")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (60, 60, 60)

# ========= Raquetes =========
RAQ_W, RAQ_H = 16, 110
MARGEM = 40
rax_jog = MARGEM
ray_jog = ALTURA // 2 - RAQ_H // 2
rax_ia = LARGURA - MARGEM - RAQ_W
ray_ia = ALTURA // 2 - RAQ_H // 2

VEL_JOG = 8
VEL_IA = 50  # IA extremamente rápida

# ========= Bola =========
BOLA_TAM = 18
bx = LARGURA // 2 - BOLA_TAM // 2
by = ALTURA // 2 - BOLA_TAM // 2
vx = 0
vy = 0
ACEL = 1.1  # aumenta mais rápido agora

clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 28)

def reset_bola():
    global bx, by, vx, vy
    bx = LARGURA // 2 - BOLA_TAM // 2
    by = ALTURA // 2 - BOLA_TAM // 2
    # sempre começa indo para o jogador
    vx = -6
    vy = random.choice([-4, 4])

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def aplicar_aceleracao(vx, vy):
    vx *= ACEL
    vy *= ACEL
    if abs(vy) < 2:
        vy = 2 if vy >= 0 else -2
    return vx, vy

def desenhar_campo():
    tela.fill(PRETO)
    dash_h = 16
    gap = 12
    x = LARGURA // 2 - 2
    y = 0
    while y < ALTURA:
        pygame.draw.rect(tela, CINZA, (x, y, 4, dash_h))
        y += dash_h + gap

def texto_canto(msg, x, y):
    img = fonte.render(msg, True, BRANCO)
    tela.blit(img, (x, y))

# Inicia o jogo
reset_bola()

# ========= Loop principal =========
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            reset_bola()

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ray_jog -= VEL_JOG
    if keys[pygame.K_s]:
        ray_jog += VEL_JOG
    ray_jog = clamp(ray_jog, 0, ALTURA - RAQ_H)

    # Movimento da IA (nunca perde)
    if ray_ia + RAQ_H / 2 < by:
        ray_ia += VEL_IA
    elif ray_ia + RAQ_H / 2 > by:
        ray_ia -= VEL_IA
    ray_ia = clamp(ray_ia, 0, ALTURA - RAQ_H)

    # Movimento da bola
    bx += vx
    by += vy

    # Teto/solo
    if by <= 0:
        by = 0
        vy = -vy
    elif by + BOLA_TAM >= ALTURA:
        by = ALTURA - BOLA_TAM
        vy = -vy

    # Colisão com raquete do jogador
    if (bx <= rax_jog + RAQ_W and
        bx >= rax_jog and
        by + BOLA_TAM > ray_jog and
        by < ray_jog + RAQ_H):
        bx = rax_jog + RAQ_W
        vx, vy = aplicar_aceleracao(abs(vx), vy)

    # Colisão com raquete da IA
    if (bx + BOLA_TAM >= rax_ia and
        bx <= rax_ia + RAQ_W and
        by + BOLA_TAM > ray_ia and
        by < ray_ia + RAQ_H):
        bx = rax_ia - BOLA_TAM
        vx, vy = aplicar_aceleracao(-abs(vx), vy)

    # Saiu da tela (ponto de alguém)
    if bx < -BOLA_TAM or bx > LARGURA:
        reset_bola()

    # Desenho
    desenhar_campo()
    pygame.draw.rect(tela, BRANCO, (rax_jog, ray_jog, RAQ_W, RAQ_H))
    pygame.draw.rect(tela, BRANCO, (rax_ia, ray_ia, RAQ_W, RAQ_H))
    pygame.draw.rect(tela, BRANCO, (int(bx), int(by), BOLA_TAM, BOLA_TAM))
    texto_canto("Pong — Jogador (W/S) vs IA — pressione R para reiniciar", 18, 14)

    pygame.display.flip()
    clock.tick(60)
    .
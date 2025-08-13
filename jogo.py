import pygame
import sys
import random

# ========= Configuração =========
pygame.init()
LARGURA, ALTURA = 900, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong — IA vs IA (Imbatíveis)")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (60, 60, 60)

# ========= Raquetes =========
RAQ_W, RAQ_H = 16, 110
MARGEM = 40
rax_esq = MARGEM
ray_esq = ALTURA // 2 - RAQ_H // 2
rax_dir = LARGURA - MARGEM - RAQ_W
ray_dir = ALTURA // 2 - RAQ_H // 2

def ia_alvo_y(bola_y):
    return int(bola_y - RAQ_H // 2)

# ========= Bola =========
BOLA_TAM = 18
bx = LARGURA // 2 - BOLA_TAM // 2
by = ALTURA // 2 - BOLA_TAM // 2
vx = 0
vy = 0
ACEL = 1.07
VEL_MAX = 22
SUBPASSO_BASE = 6.0

clock = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 28)

def reset_bola():
    global bx, by, vx, vy
    bx = LARGURA // 2 - BOLA_TAM // 2
    by = ALTURA // 2 - BOLA_TAM // 2
    direcao_x = random.choice([-1, 1])  # aleatório esquerda/direita
    direcao_y = random.choice([-1, 1])
    vx = 6 * direcao_x
    vy = 4 * direcao_y

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def aplicar_aceleracao(vx, vy, fator):
    nvx = clamp(vx * fator, -VEL_MAX, VEL_MAX)
    nvy = clamp(vy * fator, -VEL_MAX, VEL_MAX)
    if abs(nvy) < 2:
        nvy = 2 if nvy >= 0 else -2
    return nvx, nvy

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

    # IA posiciona
    ray_esq = clamp(ia_alvo_y(by), 0, ALTURA - RAQ_H)
    ray_dir = clamp(ia_alvo_y(by), 0, ALTURA - RAQ_H)

    # Movimento da bola com subpassos
    passos = max(1, int(max(abs(vx), abs(vy)) // SUBPASSO_BASE) + 1)
    stepx = vx / passos
    stepy = vy / passos

    for _ in range(passos):
        bx += stepx
        by += stepy

        # Teto/solo
        if by <= 0:
            by = 0
            vy = -vy
            stepy = vy / passos
        elif by + BOLA_TAM >= ALTURA:
            by = ALTURA - BOLA_TAM
            vy = -vy
            stepy = vy / passos

        # Colisão esquerda
        if (bx <= rax_esq + RAQ_W and
            bx >= rax_esq - BOLA_TAM and
            by + BOLA_TAM > ray_esq and
            by < ray_esq + RAQ_H):
            bx = rax_esq + RAQ_W  # empurra para fora
            vx, vy = aplicar_aceleracao(abs(vx), vy, ACEL)
            stepx = vx / passos
            stepy = vy / passos

        # Colisão direita
        if (bx + BOLA_TAM >= rax_dir and
            bx <= rax_dir + RAQ_W and
            by + BOLA_TAM > ray_dir and
            by < ray_dir + RAQ_H):
            bx = rax_dir - BOLA_TAM
            vx, vy = aplicar_aceleracao(-abs(vx), vy, ACEL)
            stepx = vx / passos
            stepy = vy / passos

        # Bola saiu da tela
        if bx < -BOLA_TAM:
            reset_bola()
            break
        if bx > LARGURA:
            reset_bola()
            break

    # Desenho
    desenhar_campo()
    pygame.draw.rect(tela, BRANCO, (rax_esq, ray_esq, RAQ_W, RAQ_H))
    pygame.draw.rect(tela, BRANCO, (rax_dir, ray_dir, RAQ_W, RAQ_H))
    pygame.draw.rect(tela, BRANCO, (int(bx), int(by), BOLA_TAM, BOLA_TAM))
    texto_canto("IA vs IA — pressione R para reiniciar a bola", 18, 14)

    pygame.display.flip()
    clock.tick(60)
<template>
  <header class="header">
    <div class="header__inner">
      <!-- Logo -->
      <RouterLink class="logo" to="/" aria-label="Forgeswords Home">
        <span class="logo__mark" aria-hidden="true"></span>
        <span class="logo__text">Forgeswords</span>
      </RouterLink>

      <!-- Nav -->
      <nav class="nav" aria-label="Primary navigation">
        <RouterLink class="nav__link" to="/">Home</RouterLink>
        <RouterLink class="nav__link" to="/about">About</RouterLink>
        <RouterLink class="nav__link" to="/posts">Posts</RouterLink>

        <RouterLink
          v-if="auth.session"
          class="nav__link nav__link--emphasis"
          to="/create_post"
        >
          Create post
        </RouterLink>
      </nav>

      <!-- Auth -->
      <div class="auth">
        <template v-if="!auth.session">
          <RouterLink class="btn btn--primary" to="/signup">Sign up</RouterLink>
          <RouterLink class="btn btn--ghost" to="/login">Login</RouterLink>
        </template>

        <template v-else>
          <RouterLink class="btn btn--ghost" to="/profile">
            <span class="user">
              <span class="user__dot" aria-hidden="true"></span>
              <span class="user__name">{{ auth.user.name }}</span>
            </span>
          </RouterLink>
        </template>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()
</script>

<style scoped>
/* =========================
   Design tokens (local)
   Позже это легко вынести в общий theme.css
========================= */
.header {
  --bg: rgba(17, 17, 20, 0.7);
  --border: rgba(255, 255, 255, 0.08);
  --text: rgba(255, 255, 255, 0.92);
  --muted: rgba(255, 255, 255, 0.72);

  --accent: #ff7f50;      /* coral */
  --accent2: #8b5cf6;     /* violet-ish */
  --ring: rgba(255, 127, 80, 0.35);

  --r-lg: 18px;
  --r-md: 12px;

  --shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
  --shadow-sm: 0 8px 20px rgba(0, 0, 0, 0.25);

  position: sticky;
  top: 0;
  z-index: 1000;

  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);

  background: var(--bg);
  border-bottom: 1px solid var(--border);
  color: var(--text);
}

.header__inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 14px 20px;

  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

/* =========================
   Logo
========================= */
.logo {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--text);

  padding: 8px 10px;
  border-radius: var(--r-md);
}

.logo:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.logo__mark {
  width: 14px;
  height: 14px;
  border-radius: 6px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  box-shadow: 0 0 0 4px rgba(255, 127, 80, 0.12);
}

.logo__text {
  font-weight: 800;
  letter-spacing: 0.2px;
  font-size: 16px;
}

/* =========================
   Nav
========================= */
.nav {
  display: flex;
  align-items: center;
  gap: 8px;

  padding: 6px;
  border-radius: var(--r-lg);
  border: 1px solid var(--border);
  background: rgba(255, 255, 255, 0.03);
  box-shadow: var(--shadow-sm);
}

.nav__link {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;

  padding: 9px 12px;
  border-radius: 12px;

  color: var(--muted);
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;

  transition: background 180ms ease, color 180ms ease, transform 180ms ease;
}

.nav__link:hover {
  color: var(--text);
  background: rgba(255, 255, 255, 0.06);
}

.nav__link:active {
  transform: translateY(1px);
}

.nav__link:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.nav__link.router-link-active {
  color: var(--text);
  background: rgba(255, 127, 80, 0.16);
  box-shadow: inset 0 0 0 1px rgba(255, 127, 80, 0.22);
}

.nav__link--emphasis {
  color: var(--text);
  background: rgba(255, 127, 80, 0.12);
}

/* =========================
   Auth / Buttons
========================= */
.auth {
  display: flex;
  align-items: center;
  gap: 10px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  text-decoration: none;
  font-weight: 700;
  font-size: 14px;

  padding: 10px 14px;
  border-radius: 14px;

  transition: transform 180ms ease, background 180ms ease, box-shadow 180ms ease, color 180ms ease;
  user-select: none;
}

.btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.btn:active {
  transform: translateY(1px);
}

.btn--primary {
  color: white;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  box-shadow: 0 10px 24px rgba(255, 127, 80, 0.18);
}

.btn--primary:hover {
  box-shadow: 0 14px 30px rgba(255, 127, 80, 0.24);
}

.btn--ghost {
  color: var(--text);
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border);
}

.btn--ghost:hover {
  background: rgba(255, 255, 255, 0.07);
}

/* =========================
   User chip
========================= */
.user {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.user__dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: rgba(52, 211, 153, 0.9); /* online vibe */
  box-shadow: 0 0 0 4px rgba(52, 211, 153, 0.12);
}

.user__name {
  max-width: 160px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* =========================
   Responsive
========================= */
@media (max-width: 860px) {
  .header__inner {
    flex-wrap: wrap;
    justify-content: center;
  }
  .nav {
    order: 3;
    width: 100%;
    justify-content: center;
  }
  .auth {
    order: 2;
  }
}

@media (max-width: 520px) {
  .nav__link {
    padding: 9px 10px;
    font-size: 13px;
  }
  .btn {
    padding: 10px 12px;
  }
}
</style>

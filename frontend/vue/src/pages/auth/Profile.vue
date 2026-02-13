<template>
  <Header />

  <main class="page">
    <section class="wrap">
      <header class="head">
        <div>
          <p class="kicker">Account</p>
          <h1 class="title">Profile</h1>
          <p class="subtitle">Manage your session and view basic account info.</p>
        </div>

        <div class="head__actions">
          <RouterLink class="btn btn--ghost" to="/posts">Posts</RouterLink>
          <button class="btn btn--danger" type="button" @click="logout">
            Logout
          </button>
        </div>
      </header>

      <div class="grid">
        <!-- Profile card -->
        <article class="card">
          <div class="profile">
            <div class="avatar" aria-hidden="true">
              <span class="avatar__dot"></span>
            </div>

            <div class="profile__info">
              <p class="profile__kicker">Signed in as</p>
              <h2 class="profile__name">{{ auth.user?.name || "Unknown" }}</h2>

              <div class="chips">
                <div class="chip">
                  <span class="chip__label">User ID</span>
                  <span class="chip__value">{{ auth.user?.id ?? "—" }}</span>
                </div>

                <div class="chip chip--soft">
                  <span class="chip__label">Status</span>
                  <span class="chip__value">Active session</span>
                </div>
              </div>
            </div>
          </div>

          <div class="divider"></div>

          <div class="card__actions">
            <RouterLink class="btn btn--primary" to="/create_post">Create post</RouterLink>
            <RouterLink class="btn btn--ghost" to="/posts">Browse posts</RouterLink>
          </div>
        </article>

        <!-- Security card -->
        <article class="card">
          <h2 class="card__title">Security</h2>
          <p class="card__text">
            If you’re using a shared device, make sure to log out when you’re done.
          </p>

          <div class="warn">
            <div class="warn__icon" aria-hidden="true"></div>
            <div>
              <p class="warn__title">Logout ends your session</p>
              <p class="warn__text">You can log in again anytime.</p>
            </div>
          </div>

          <div class="card__actions card__actions--right">
            <button class="btn btn--danger" type="button" @click="logout">
              Logout
            </button>
          </div>
        </article>
      </div>
    </section>
  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter, RouterLink } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

function logout() {
  auth.logout()
  router.push('/')
}
</script>

<style scoped>
.page {
  min-height: calc(100vh - 64px);
  padding: 28px 20px;

  background:
    radial-gradient(900px 400px at 20% 0%, rgba(255, 127, 80, 0.10), transparent 60%),
    radial-gradient(700px 360px at 90% 10%, rgba(139, 92, 246, 0.10), transparent 55%),
    #0b0b0f;
}

.wrap {
  max-width: 1100px;
  margin: 0 auto;
}

/* Header */
.head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 14px;
  margin-bottom: 16px;
}

.kicker {
  margin: 0;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.title {
  margin: 8px 0 0;
  font-size: 28px;
  font-weight: 950;
  letter-spacing: 0.2px;
  color: rgba(255, 255, 255, 0.92);
  line-height: 1.15;
}

.subtitle {
  margin: 10px 0 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.68);
}

.head__actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

@media (max-width: 760px) {
  .head {
    flex-direction: column;
    align-items: flex-start;
  }
  .head__actions {
    width: 100%;
  }
  .head__actions .btn {
    flex: 1;
  }
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 14px;
}

@media (max-width: 980px) {
  .grid {
    grid-template-columns: 1fr;
  }
}

/* Cards */
.card {
  border-radius: 22px;
  padding: 18px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);

  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.card__title {
  margin: 0;
  font-size: 16px;
  font-weight: 950;
  color: rgba(255, 255, 255, 0.92);
}

.card__text {
  margin: 10px 0 0;
  font-size: 14px;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.70);
}

/* Profile block */
.profile {
  display: flex;
  gap: 14px;
  align-items: center;
}

.avatar {
  width: 54px;
  height: 54px;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(255, 127, 80, 0.9), rgba(139, 92, 246, 0.85));
  box-shadow: 0 0 0 6px rgba(255, 127, 80, 0.12);
  display: grid;
  place-items: center;
  flex: 0 0 auto;
}

.avatar__dot {
  width: 12px;
  height: 12px;
  border-radius: 999px;
  background: rgba(52, 211, 153, 0.95);
  box-shadow: 0 0 0 5px rgba(52, 211, 153, 0.12);
}

.profile__kicker {
  margin: 0;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0.6px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.profile__name {
  margin: 6px 0 0;
  font-size: 22px;
  font-weight: 950;
  color: rgba(255, 255, 255, 0.92);
}

.chips {
  margin-top: 10px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.chip {
  display: inline-flex;
  align-items: baseline;
  gap: 10px;

  padding: 10px 12px;
  border-radius: 999px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.10);
}

.chip--soft {
  background: rgba(255, 255, 255, 0.03);
}

.chip__label {
  font-size: 12px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.60);
  text-transform: uppercase;
  letter-spacing: 0.6px;
}

.chip__value {
  font-size: 13px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.86);
}

.divider {
  height: 1px;
  margin: 16px 0;
  background: rgba(255, 255, 255, 0.06);
}

.card__actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.card__actions--right {
  justify-content: flex-end;
}

/* Warning block */
.warn {
  margin-top: 14px;
  padding: 14px;
  border-radius: 18px;

  background: rgba(239, 68, 68, 0.08);
  border: 1px solid rgba(239, 68, 68, 0.16);

  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.warn__icon {
  width: 38px;
  height: 38px;
  border-radius: 14px;
  background: rgba(239, 68, 68, 0.18);
  box-shadow: 0 0 0 6px rgba(239, 68, 68, 0.10);
  flex: 0 0 auto;
}

.warn__title {
  margin: 0;
  font-weight: 950;
  color: rgba(255, 255, 255, 0.92);
  font-size: 14px;
}

.warn__text {
  margin: 6px 0 0;
  color: rgba(255, 255, 255, 0.70);
  font-size: 13px;
}

/* Buttons (same system) */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;

  padding: 10px 14px;
  border-radius: 14px;

  font-weight: 900;
  font-size: 14px;

  border: 1px solid transparent;
  cursor: pointer;
  user-select: none;

  text-decoration: none;
  color: inherit;

  transition: transform 180ms ease, background 180ms ease, box-shadow 180ms ease, opacity 180ms ease;
}

.btn:active {
  transform: translateY(1px);
}

.btn--primary {
  color: #fff;
  background: linear-gradient(135deg, #ff7f50, #8b5cf6);
  box-shadow: 0 12px 26px rgba(255, 127, 80, 0.18);
}

.btn--primary:hover {
  box-shadow: 0 16px 34px rgba(255, 127, 80, 0.24);
}

.btn--ghost {
  color: rgba(255, 255, 255, 0.92);
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.10);
}

.btn--ghost:hover {
  background: rgba(255, 255, 255, 0.07);
}

.btn--danger {
  color: rgba(255, 255, 255, 0.95);
  background: rgba(239, 68, 68, 0.14);
  border-color: rgba(239, 68, 68, 0.22);
  box-shadow: 0 14px 34px rgba(239, 68, 68, 0.10);
}

.btn--danger:hover {
  background: rgba(239, 68, 68, 0.18);
  box-shadow: 0 18px 42px rgba(239, 68, 68, 0.14);
}
</style>

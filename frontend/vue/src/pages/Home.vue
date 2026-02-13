<template>
  <Header />

  <main class="page">
    <section class="hero">
      <div class="hero__content">
        <p class="hero__kicker">Forgeswords Platform</p>

        <h1 class="hero__title">
          Forge. Share. Inspire.
        </h1>

        <p class="hero__subtitle">
          A place where posts become creations and ideas turn into blades.
        </p>

        <div class="hero__actions">
          <RouterLink class="btn btn--primary" to="/posts">
            Explore posts
          </RouterLink>

          <RouterLink class="btn btn--ghost" to="/create_post">
            Create post
          </RouterLink>
        </div>

        <div class="hero__message" v-if="message">
          <span class="badge">Server message</span>
          <span class="hero__message-text">{{ message }}</span>
        </div>
      </div>

      <div class="hero__visual" aria-hidden="true">
        <div class="orb orb--one"></div>
        <div class="orb orb--two"></div>
        <div class="glass-card"></div>
      </div>
    </section>
  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref } from 'vue'

const message = ref('')

onMounted(async () => {
  try {
    const res = await api.get('')
    message.value = res.data.message
  } catch {
    message.value = ''
  }
})
</script>

<style scoped>
.page {
  min-height: calc(100vh - 64px);
  padding: 40px 20px;

  background:
    radial-gradient(900px 500px at 10% 0%, rgba(255, 127, 80, 0.12), transparent 60%),
    radial-gradient(800px 500px at 90% 10%, rgba(139, 92, 246, 0.12), transparent 60%),
    #0b0b0f;
}

/* HERO LAYOUT */
.hero {
  max-width: 1200px;
  margin: 0 auto;

  display: grid;
  grid-template-columns: 1.1fr 1fr;
  align-items: center;
  gap: 40px;
}

@media (max-width: 900px) {
  .hero {
    grid-template-columns: 1fr;
    text-align: center;
  }
}

/* TEXT SIDE */
.hero__kicker {
  margin: 0;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.hero__title {
  margin: 16px 0 0;
  font-size: 48px;
  font-weight: 950;
  line-height: 1.1;

  background: linear-gradient(135deg, #ffffff, #cfcfff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

@media (max-width: 600px) {
  .hero__title {
    font-size: 36px;
  }
}

.hero__subtitle {
  margin: 18px 0 0;
  font-size: 18px;
  color: rgba(255, 255, 255, 0.72);
  max-width: 520px;
}

.hero__actions {
  margin-top: 28px;
  display: flex;
  gap: 14px;
}

@media (max-width: 900px) {
  .hero__actions {
    justify-content: center;
  }
}

/* MESSAGE */
.hero__message {
  margin-top: 28px;
  padding: 14px 16px;
  border-radius: 18px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);

  display: flex;
  align-items: center;
  gap: 12px;

  backdrop-filter: blur(10px);
}

.badge {
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 0.5px;

  background: linear-gradient(135deg, #ff7f50, #8b5cf6);
  color: white;
}

.hero__message-text {
  font-size: 14px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.86);
}

/* VISUAL SIDE */
.hero__visual {
  position: relative;
  height: 420px;
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.6;
}

.orb--one {
  width: 260px;
  height: 260px;
  background: #ff7f50;
  top: 40px;
  left: 40px;
}

.orb--two {
  width: 300px;
  height: 300px;
  background: #8b5cf6;
  bottom: 40px;
  right: 40px;
}

.glass-card {
  position: absolute;
  inset: 80px;

  border-radius: 28px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);

  backdrop-filter: blur(16px);
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
}

/* BUTTON SYSTEM (same language) */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;

  padding: 12px 18px;
  border-radius: 16px;

  font-weight: 900;
  font-size: 14px;

  text-decoration: none;
  transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
}

.btn:active {
  transform: translateY(1px);
}

.btn--primary {
  color: #fff;
  background: linear-gradient(135deg, #ff7f50, #8b5cf6);
  box-shadow: 0 14px 34px rgba(255, 127, 80, 0.22);
}

.btn--primary:hover {
  box-shadow: 0 20px 44px rgba(255, 127, 80, 0.28);
}

.btn--ghost {
  color: rgba(255, 255, 255, 0.9);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
}

.btn--ghost:hover {
  background: rgba(255, 255, 255, 0.08);
}
</style>

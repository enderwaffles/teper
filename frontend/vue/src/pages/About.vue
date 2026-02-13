<template>
  <Header />

  <main class="page">
    <section class="wrap">
      <header class="head">
        <p class="kicker">About</p>
        <h1 class="title">What is Forgeswords?</h1>
        <p class="subtitle">
          A clean, premium space for sharing posts — crafted with a consistent design language.
        </p>
      </header>

      <div class="grid">
        <article class="card">
          <h2 class="card__title">Mission</h2>
          <p class="card__text">
            Build a simple platform where creators can publish and share their work without visual chaos.
          </p>
        </article>

        <article class="card">
          <h2 class="card__title">Design</h2>
          <p class="card__text">
            One theme. One system. Glass UI, strong typography, consistent spacing, and smooth interactions.
          </p>
        </article>

        <article class="card">
          <h2 class="card__title">Tech</h2>
          <p class="card__text">
            Vue + Router on the front, API-driven backend, and a UI foundation you can scale.
          </p>
        </article>
      </div>

      <section v-if="message" class="message">
        <div class="message__icon" aria-hidden="true"></div>
        <div class="message__body">
          <p class="message__kicker">Server message</p>
          <p class="message__text">{{ message }}</p>
        </div>
      </section>
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
    const res = await api.get('/about')
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

.wrap {
  max-width: 1100px;
  margin: 0 auto;
}

.head {
  margin-bottom: 18px;
}

.kicker {
  margin: 0;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.title {
  margin: 10px 0 0;
  font-size: 34px;
  font-weight: 950;
  line-height: 1.15;
  color: rgba(255, 255, 255, 0.92);
}

.subtitle {
  margin: 12px 0 0;
  font-size: 15px;
  color: rgba(255, 255, 255, 0.70);
  max-width: 720px;
}

/* Cards grid */
.grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

@media (max-width: 900px) {
  .grid {
    grid-template-columns: 1fr;
  }
}

.card {
  border-radius: 22px;
  padding: 18px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);

  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);

  transition: transform 180ms ease, background 180ms ease, border-color 180ms ease;
}

.card:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.12);
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

/* Server message */
.message {
  margin-top: 16px;

  display: flex;
  gap: 14px;
  align-items: flex-start;

  padding: 16px;
  border-radius: 22px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);

  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.message__icon {
  width: 44px;
  height: 44px;
  border-radius: 16px;
  flex: 0 0 auto;

  background: linear-gradient(135deg, rgba(255, 127, 80, 0.9), rgba(139, 92, 246, 0.85));
  box-shadow: 0 0 0 6px rgba(255, 127, 80, 0.12);
}

.message__kicker {
  margin: 0;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.message__text {
  margin: 8px 0 0;
  font-size: 14px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.86);
}
</style>

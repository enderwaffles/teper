<template>
  <Header />

  <main class="page">
    <section class="wrap">
      <header class="head">
        <div>
          <h1 class="title">Posts</h1>
          <p class="subtitle">Browse the latest posts and open any one to read more.</p>
        </div>

        <div class="head__actions">
          <RouterLink class="btn btn--ghost" to="/">Home</RouterLink>
          <RouterLink class="btn btn--primary" to="/create_post">Create post</RouterLink>
        </div>
      </header>

      <!-- Loading -->
      <div v-if="loading" class="grid">
        <article v-for="i in 6" :key="i" class="card card--skeleton" aria-hidden="true">
          <div class="sk sk--thumb"></div>
          <div class="sk sk--line"></div>
          <div class="sk sk--line sk--short"></div>
          <div class="sk sk--line sk--btn"></div>
        </article>
      </div>

      <!-- Empty -->
      <div v-else-if="posts.length === 0" class="empty">
        <div class="empty__icon" aria-hidden="true"></div>
        <h2 class="empty__title">No posts yet</h2>
        <p class="empty__text">Be the first to publish something.</p>
        <RouterLink class="btn btn--primary" to="/create_post">Create your first post</RouterLink>
      </div>

      <!-- List (card = link) -->
      <div v-else class="grid">
        <RouterLink
          v-for="p in posts"
          :key="p.id"
          class="card card--link"
          :to="`/posts/${p.id}`"
          :aria-label="`Open post: ${p.title}`"
        >
          <div class="thumb">
            <img
              v-if="p.file_path"
              class="thumb__img"
              :src="fileUrl(p.file_path)"
              :alt="p.title || 'Post image'"
              loading="lazy"
            />
            <div v-else class="thumb__empty">
              <div class="thumb__icon" aria-hidden="true"></div>
              <p class="thumb__text">No image</p>
            </div>

            <div class="thumb__overlay" aria-hidden="true">
              <span class="thumb__chip">Open</span>
            </div>
          </div>

          <div class="meta">
            <p class="kicker">Post</p>
            <h3 class="card__title">{{ p.title }}</h3>

            <div class="author">
              <span class="author__dot" aria-hidden="true"></span>
              <span class="author__name">{{ p.author?.name || "Unknown author" }}</span>
            </div>
          </div>
        </RouterLink>
      </div>
    </section>
  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref } from 'vue'

const posts = ref([])
const loading = ref(true)

const BASE_URL = 'http://localhost:8000'

function fileUrl(path) {
  if (!path) return ''
  return `${BASE_URL}${path}`
}

onMounted(async () => {
  try {
    loading.value = true
    const res = await api.get('/posts')
    posts.value = res.data
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* Same page language as Create post */
.page {
  min-height: calc(100vh - 64px);
  padding: 28px 20px;

  background:
    radial-gradient(900px 400px at 20% 0%, rgba(255, 127, 80, 0.10), transparent 60%),
    radial-gradient(700px 360px at 90% 10%, rgba(139, 92, 246, 0.10), transparent 55%),
    #0b0b0f;
}

.wrap {
  max-width: 1200px;
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

.title {
  margin: 0;
  font-size: 26px;
  font-weight: 900;
  letter-spacing: 0.2px;
  color: rgba(255, 255, 255, 0.92);
}

.subtitle {
  margin: 8px 0 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.68);
}

.head__actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

@media (max-width: 980px) {
  .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .head {
    align-items: flex-start;
    flex-direction: column;
  }
}

@media (max-width: 560px) {
  .grid {
    grid-template-columns: 1fr;
  }
  .head__actions {
    width: 100%;
  }
  .head__actions .btn {
    flex: 1;
  }
}

/* Card */
.card {
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);

  overflow: hidden;
  display: flex;
  flex-direction: column;

  transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
}

.card:hover {
  transform: translateY(-2px);
  border-color: rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.05);
}

/* Make the whole card clickable */
.card--link {
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.card--link:focus-visible {
  outline: 2px solid rgba(255, 127, 80, 0.35);
  outline-offset: 4px;
  box-shadow: 0 0 0 4px rgba(255, 127, 80, 0.12);
}

/* Thumbnail */
.thumb {
  width: 100%;
  aspect-ratio: 16 / 9;
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  position: relative;
  overflow: hidden;
}

.thumb__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transform: scale(1);
  transition: transform 220ms ease;
}

.card--link:hover .thumb__img {
  transform: scale(1.03);
}

/* Fallback when no image */
.thumb__empty {
  height: 100%;
  display: grid;
  place-items: center;
  gap: 8px;
  padding: 18px;
  text-align: center;
}

.thumb__icon {
  width: 44px;
  height: 44px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(255, 127, 80, 0.9), rgba(139, 92, 246, 0.85));
  box-shadow: 0 0 0 6px rgba(255, 127, 80, 0.12);
}

.thumb__text {
  margin: 0;
  font-size: 13px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.72);
}

/* Hover overlay */
.thumb__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.0) 30%,
    rgba(0, 0, 0, 0.55) 100%
  );
  opacity: 0;
  transition: opacity 200ms ease;
  display: grid;
  place-items: end start;
  padding: 12px;
}

.card--link:hover .thumb__overlay {
  opacity: 1;
}

.thumb__chip {
  padding: 8px 10px;
  border-radius: 999px;
  font-weight: 900;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.92);
  background: rgba(255, 255, 255, 0.10);
  border: 1px solid rgba(255, 255, 255, 0.14);
  backdrop-filter: blur(8px);
}

/* Meta */
.meta {
  padding: 14px 14px 14px;
  display: grid;
  gap: 8px;
}

.kicker {
  margin: 0;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.6px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.card__title {
  margin: 0;
  font-size: 16px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.92);
  line-height: 1.25;
}

.card--link:hover .card__title {
  text-decoration: underline;
  text-decoration-color: rgba(255, 127, 80, 0.45);
  text-underline-offset: 3px;
}

.author {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: rgba(255, 255, 255, 0.72);
  font-size: 13px;
  font-weight: 700;
}

.author__dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: rgba(52, 211, 153, 0.9);
  box-shadow: 0 0 0 4px rgba(52, 211, 153, 0.12);
}

/* Buttons (same system) */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  padding: 10px 14px;
  border-radius: 14px;

  font-weight: 800;
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

/* Empty state */
.empty {
  margin-top: 18px;
  border-radius: 22px;
  padding: 22px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);

  text-align: center;
}

.empty__icon {
  width: 44px;
  height: 44px;
  margin: 0 auto 10px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(255, 127, 80, 0.9), rgba(139, 92, 246, 0.85));
  box-shadow: 0 0 0 6px rgba(255, 127, 80, 0.12);
}

.empty__title {
  margin: 0;
  font-size: 18px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.92);
}

.empty__text {
  margin: 8px 0 14px;
  color: rgba(255, 255, 255, 0.68);
  font-size: 14px;
}

/* Skeletons */
.card--skeleton {
  overflow: hidden;
}

.card--skeleton:hover {
  transform: none;
}

.sk {
  margin: 14px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.06);
  position: relative;
  overflow: hidden;
}

.sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.08), transparent);
  animation: shimmer 1.1s infinite;
}

.sk--thumb {
  margin: 0;
  height: 170px;
  border-radius: 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.sk--line {
  height: 14px;
}

.sk--short {
  width: 65%;
}

.sk--btn {
  height: 36px;
  width: 120px;
  margin-left: auto;
}

@keyframes shimmer {
  100% {
    transform: translateX(100%);
  }
}
</style>

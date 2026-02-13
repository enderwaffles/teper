<template>
  <Header />
<<<<<<< HEAD

  <main class="page">
    <section class="wrap">
      <!-- Top bar -->
      <div class="topbar">
        <div>
          <p class="kicker">Post</p>
          <h1 class="title">{{ post?.title || "Loading…" }}</h1>
          <p v-if="post" class="subtitle">
            By <span class="author">{{ post.author?.name || "Unknown author" }}</span>
          </p>
        </div>

        <div class="topbar__actions">
          <RouterLink class="btn btn--ghost" to="/posts">Back to posts</RouterLink>
          <button
            class="btn btn--danger"
            type="button"
            @click="delete_post"
            :disabled="deleting || !post"
          >
            {{ deleting ? "Deleting…" : "Delete" }}
          </button>
        </div>
      </div>

      <!-- Loading -->
      <div v-if="loading" class="card card--skeleton">
        <div class="sk sk--hero"></div>
        <div class="sk sk--line"></div>
        <div class="sk sk--line sk--short"></div>
        <div class="sk sk--line"></div>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="card error">
        <h2 class="error__title">Couldn’t load the post</h2>
        <p class="error__text">{{ error }}</p>
        <div class="error__actions">
          <button class="btn btn--primary" type="button" @click="fetchPost">Retry</button>
          <RouterLink class="btn btn--ghost" to="/posts">Go to posts</RouterLink>
        </div>
      </div>

      <!-- Content -->
      <article v-else-if="post" class="card">
        <div v-if="post.file_path" class="hero">
          <img class="hero__img" :src="fileUrl(post.file_path)" :alt="post.title || 'Post image'" />
        </div>

        <div class="content">
          <div class="row">
            <div class="pill">
              <span class="pill__dot" aria-hidden="true"></span>
              <span class="pill__text">{{ post.author?.name || "Unknown author" }}</span>
            </div>

            <div class="pill pill--soft">
              <span class="pill__text">ID: {{ post.id }}</span>
            </div>
          </div>

          <div class="block">
            <h2 class="block__title">Title</h2>
            <p class="block__text">{{ post.title }}</p>
          </div>

          <div class="divider"></div>

          <div class="actions">
            <RouterLink class="btn btn--ghost" to="/posts">Back</RouterLink>
            <button class="btn btn--danger" type="button" @click="delete_post" :disabled="deleting">
              {{ deleting ? "Deleting…" : "Delete post" }}
            </button>
          </div>
        </div>
      </article>
    </section>
  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'

const route = useRoute()
const router = useRouter()
=======

  <h1>Post</h1>

  <div v-if="post">

    <p>post title: {{ post.title }}</p>
    <p>post text: {{ post.text }}</p>
    <p>user name: {{ post.author?.name }}</p>

    <img
      v-if="post.upload_url"
      :src="'http://localhost:8000' + post.upload_url"
      style="max-width: 400px"
    />

    <br>
    <div v-if="auth.user.id == post.author.id">
      <button type="button" @click="delete_post">Delete</button>
    </div>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const route = useRoute();
const router = useRouter();
const auth = useAuthStore()

>>>>>>> 6d13676

const post = ref(null)
const loading = ref(true)
const deleting = ref(false)
const error = ref('')

const BASE_URL = 'http://localhost:8000'
const post_id = route.params.id

function fileUrl(path) {
  if (!path) return ''
  return `${BASE_URL}${path}`
}

async function fetchPost() {
  try {
    loading.value = true
    error.value = ''
    const res = await api.get(`/posts/${post_id}`)
    post.value = res.data
  } catch (e) {
    error.value = 'Server error or post not found.'
    post.value = null
  } finally {
    loading.value = false
  }
}

async function delete_post() {
  if (!post.value || deleting.value) return

  const ok = confirm('Delete this post permanently?')
  if (!ok) return

  try {
    deleting.value = true
    await api.delete(`/posts/${post_id}`)
    router.push('/posts')
  } finally {
    deleting.value = false
  }
}

onMounted(fetchPost)
</script>

<style scoped>
/* Same background language */
.page {
  min-height: calc(100vh - 64px);
  padding: 28px 20px;

  background:
    radial-gradient(900px 400px at 20% 0%, rgba(255, 127, 80, 0.10), transparent 60%),
    radial-gradient(700px 360px at 90% 10%, rgba(139, 92, 246, 0.10), transparent 55%),
    #0b0b0f;
}

.wrap {
  max-width: 980px;
  margin: 0 auto;
}

/* Top bar */
.topbar {
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
  letter-spacing: 0.6px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.title {
  margin: 6px 0 0;
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

.author {
  font-weight: 900;
  color: rgba(255, 255, 255, 0.86);
}

.topbar__actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

@media (max-width: 720px) {
  .topbar {
    flex-direction: column;
    align-items: flex-start;
  }
  .topbar__actions {
    width: 100%;
  }
  .topbar__actions .btn {
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
}

/* Hero image */
.hero {
  width: 100%;
  aspect-ratio: 16 / 9;
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.hero__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Content */
.content {
  padding: 16px;
  display: grid;
  gap: 14px;
}

.row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 10px;

  padding: 10px 12px;
  border-radius: 999px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.10);

  color: rgba(255, 255, 255, 0.84);
  font-weight: 800;
  font-size: 13px;
}

.pill--soft {
  color: rgba(255, 255, 255, 0.72);
  background: rgba(255, 255, 255, 0.03);
}

.pill__dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: rgba(52, 211, 153, 0.9);
  box-shadow: 0 0 0 4px rgba(52, 211, 153, 0.12);
}

.block__title {
  margin: 0;
  font-size: 13px;
  font-weight: 900;
  letter-spacing: 0.6px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.block__text {
  margin: 8px 0 0;
  font-size: 16px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.92);
}

.divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.06);
}

.actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

@media (max-width: 520px) {
  .actions {
    flex-direction: column;
  }
  .actions .btn {
    width: 100%;
  }
}

/* Buttons */
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

.btn:disabled {
  opacity: 0.55;
  cursor: not-allowed;
  transform: none;
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

/* Danger */
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

/* Error card */
.error {
  padding: 18px;
}

.error__title {
  margin: 0;
  font-size: 18px;
  font-weight: 950;
  color: rgba(255, 255, 255, 0.92);
}

.error__text {
  margin: 8px 0 14px;
  color: rgba(255, 255, 255, 0.68);
}

.error__actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

@media (max-width: 520px) {
  .error__actions {
    flex-direction: column;
  }
  .error__actions .btn {
    width: 100%;
  }
}

/* Skeleton */
.card--skeleton {
  padding: 0;
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

.sk--hero {
  margin: 0;
  height: 320px;
  border-radius: 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.sk--line {
  height: 14px;
}

.sk--short {
  width: 60%;
}

@keyframes shimmer {
  100% {
    transform: translateX(100%);
  }
}
</style>

<template>
  <Header />

  <div class="title">
    <h1>Posts</h1>
  </div>

  <!-- Loading -->
  <main v-if="loading" class="empty">
    <p>Loading...</p>
  </main>

  <!-- List -->
  <main v-else-if="sortedPosts.length">
    <RouterLink
      v-for="post in sortedPosts"
      :key="post.id"
      :to="`/posts/${post.id}`"
      class="post"
      :aria-label="`Open post: ${post.title}`"
    >
      <img
        v-if="postImageUrl(post)"
        :src="postImageUrl(post)"
        class="post_img"
        :alt="post.title || ''"
        loading="lazy"
      />

      <div class="post_text">
        <div class="post_title">{{ post.title }}</div>
        <div class="post_author">{{ post.author?.name || 'Unknown author' }}</div>
        <div v-if="post.date" class="date">
          {{ new Date(post.date).toLocaleString('ru-RU') }}
        </div>
      </div>
    </RouterLink>
  </main>

  <!-- Empty -->
  <main v-else class="empty">
    <p>No post</p>
  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref, computed } from 'vue'

const posts = ref([])
const loading = ref(true)

const sortedPosts = computed(() => {
  // если даты нет — такие посты уйдут вниз
  return [...posts.value].sort((a, b) => {
    const da = a?.date ? new Date(a.date).getTime() : 0
    const db = b?.date ? new Date(b.date).getTime() : 0
    return db - da
  })
})

function postImageUrl(post) {
  const path = post?.upload_url || post?.file_path
  if (!path) return ''
  return api.defaults.baseURL + path
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
.title {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
}

/* Сетка 3 в ряд */
main {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
  padding: 0 20px 20px;
}

/* Адаптив */
@media (max-width: 900px) {
  main {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media (max-width: 600px) {
  main {
    grid-template-columns: 1fr;
  }
}

.post {
  background-color: rgb(30, 30, 30);
  border-radius: 20px;
  text-decoration: none;
  overflow: hidden;
  cursor: pointer;
  transition: 0.2s;
  display: flex;
  flex-direction: column;
}

.post:hover {
  background-color: rgb(50, 50, 50);
}

.post_img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
}

.post_text {
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.post_title {
  color: rgb(200, 200, 200);
  font-size: 16px;
}

.post_author,
.date {
  color: rgb(120, 120, 120);
  font-size: 13px;
}

/* Пусто / загрузка */
.empty {
  display: flex;
  justify-content: center;
  padding: 30px;
}
</style>

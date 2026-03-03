<template>
  <Header />

  <div style="display: flex; justify-content: center; align-items: center;">
    <h1>Posts</h1>
  </div>

  <div class="posts-wrapper">
  <div v-for="post in posts" :key="post.id" class="post-card">

    <p class="post-id">#{{ post.id }}</p>
    <p class="post-title">{{ post.title }}</p>
    <p class="post-text">{{ post.text }}</p>

    <div v-if="post.uploads.length" class="post-images">
      <div v-for="upload in post.uploads" :key="upload.id">
        <img :src="api.defaults.baseURL + upload.upload_url">
      </div>
    </div>

    <div class="post-meta">
      <p>{{ post.date }}</p>
      <p>{{ post.author.email }}</p>
      <RouterLink :to="`/user/${post.author.nickname}`">Open user</RouterLink>
      |
      <RouterLink :to="`/posts/${post.id}`">Open post</RouterLink>
    </div>

  </div>
</div>

</template>


<script setup>
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()


//data
let posts = ref([])


//functions
onMounted(async () => {
    const res = await api.get('/posts')
    posts.value = res.data
})

</script>


<style scoped>
/* Контейнер страницы */
div {
  box-sizing: border-box;
}

/* Заголовок */
h1 {
  color: coral;
  font-size: 32px;
  letter-spacing: 1px;
  margin: 30px 0;
  text-transform: uppercase;
}

/* Обёртка всех постов */
.posts-wrapper {
  max-width: 900px;
  margin: 0 auto 60px auto;
  padding: 0 20px;
}

/* Карточка поста */
.post-card {
  background: rgb(30, 30, 30);
  padding: 20px;
  margin-bottom: 25px;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
  transition: 0.3s ease;
  border: 1px solid rgba(255, 127, 80, 0.15);
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 25px rgba(255, 127, 80, 0.2);
}

/* ID */
.post-id {
  font-size: 12px;
  opacity: 0.5;
}

/* Заголовок поста */
.post-title {
  font-size: 20px;
  margin: 10px 0;
  color: coral;
}

/* Текст */
.post-text {
  margin-bottom: 15px;
  line-height: 1.5;
}

/* Картинки */
.post-images img {
  width: 200px;
  border-radius: 8px;
  margin-right: 10px;
  margin-top: 10px;
  transition: 0.3s;
}

.post-images img:hover {
  transform: scale(1.05);
}

/* Мета информация */
.post-meta {
  font-size: 13px;
  opacity: 0.7;
  margin-top: 10px;
}

/* Ссылки */
a {
  color: coral;
  text-decoration: none;
  transition: 0.2s;
}

a:hover {
  text-decoration: underline;
  opacity: 0.8;
}
</style>

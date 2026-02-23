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
        <div class="post_author">{{ post.author?.email || 'Unknown author' }}</div>
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
let loading = ref(true)


const sortedPosts = computed(() => {
  // если даты нет — такие посты уйдут вниз
  return [...posts.value].sort((a, b) => {
    const da = a?.date ? new Date(a.date).getTime() : 0
    const db = b?.date ? new Date(b.date).getTime() : 0
    return db - da
  })
})


//functions
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

</style>

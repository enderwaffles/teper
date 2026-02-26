<template>
  <Header />

  <div style="display: flex; justify-content: center; align-items: center;">
    <h1>Posts</h1>
  </div>

  <div v-for="post in posts" :key="post.id">
    <p>{{ post.id }}</p>
    <p>{{ post.title }}</p>
    <p>{{ post.text }}</p>
    <!-- <img :src="api.defaults.baseURL + post.upload_url" alt="" style="width: 200px;"> -->
    
    <div v-if="post.uploads.length">
      <div v-for="upload in post.uploads" :key="upload.id">
        <img :src="api.defaults.baseURL + upload.upload_url" style="width:200px;">
      </div>
    </div>
    <p>{{ post.date }}</p>
    <p>{{ post.author.email }}</p>
    <RouterLink :to="`/user/${post.author.nickname}`">Open user</RouterLink> <br>
    <RouterLink :to="`/posts/${post.id}`">Open post</RouterLink>
    <br> <br> <br>
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

</style>

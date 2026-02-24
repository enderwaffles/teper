<template>
  <Header />

  <div>
    <h1>Post</h1>
  </div>

  <div v-if="post">
    <p>{{ post.id }}</p>
    <p>{{ post.title }}</p>
    <p>{{ post.text }}</p>
    <img :src="api.defaults.baseURL + post.upload_url" alt="" style="width: 200px;"> 
    <p>{{ post.date }}</p>
    <p>{{ post.author.email }}</p>
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
let post = ref(null)
let post_id = route.params.id


//functions
onMounted(async () => {
  const res = await api.get(`/posts/${post_id}`)
  post.value = res.data
})

</script>


<style scoped>

</style>

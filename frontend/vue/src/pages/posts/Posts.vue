<template>
  <Header />

  <div style="display: flex; justify-content: center; align-items: center;">
    <h1>Posts</h1>
  </div>

  <div class="posts">

    <div class="post" v-for="post in sortedPosts" :key="post.id">

      <!-- <p>{{ post.id }}</p> -->
      <!-- <img :src="api.defaults.baseURL + post.upload_url" alt="" style="width: 200px;"> -->
      
      <!-- there are max 10 photos -->
      <!-- <p>{{ post.author.email }}</p> -->
      
      <div class="user-card">
        <img class="avatar" :src="api.defaults.baseURL + post.author.avatar_url" alt="">
        <RouterLink :to="`/user/${post.author.nickname}`">{{ post.author.email }}</RouterLink> <br>
      </div>
      
      <div v-if="post.uploads.length">
        <div v-for="upload in post.uploads" :key="upload.id">
          <img class="post-image" :src="api.defaults.baseURL + upload.upload_url">
        </div>
      </div>
      <p>{{ post.text }}</p>
      
      <!-- <p>{{ post.title }}</p> -->

      <p>{{ post.date }}</p>
      <RouterLink :to="`/posts/${post.id}`">Open post</RouterLink> <br> <br>
      <button class="delete-button" v-if="post.author.id == auth.user.id" v-on:click="delete_post(post.id)">Delete</button>
      <button class="update-button" v-if="post.author.id == auth.user.id" v-on:click="update_post(post.id)">Update</button>
      <br> <br> <br>

    </div>

  </div>

</template>


<script setup>
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { onMounted, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()


//data
let posts = ref([])

const sortedPosts = computed(() => {
  return posts.value.slice().sort((a, b) => new Date(b.date) - new Date(a.date))
})

//functions

onMounted(async () => {
  const res = await api.get('/posts')
  posts.value = res.data
})

async function delete_post(post_id) {
  await api.delete(`/posts/${post_id}`)
  const res = await api.get('/posts')
  posts.value = res.data
  router.push('/posts')
}

async function update_post(post_id) {
  router.push(`/update_post/${post_id}`)
}

</script>


<style scoped>
body {
    margin: 0;
    background-color: rgb(15, 15, 15);
    color: rgb(200, 200, 200);
}
.posts {
  display: grid;
  gap: 20px;
  margin: 20px;
  grid-template-columns: repeat(3, 1fr);
}
.post {
  background-color: rgb(20, 20, 20);
  padding: 20px;
  border-radius: 5%;
}
.user-card {
  display: flex;
  align-items: center;
  margin: 10px;
  gap: 10px;
}
</style>
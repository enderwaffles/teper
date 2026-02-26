<template>
  <Header />

  <div>
    <h1>Post</h1>
  </div>

  <div v-if="post">
    <p>{{ post.id }}</p>
    <p>{{ post.title }}</p>
    <p>{{ post.text }}</p>

    <!-- <img :src="api.defaults.baseURL + post.upload_url" alt="" style="width: 200px;">  -->
    <div v-if="post.uploads.length">
      <div v-for="upload in post.uploads" :key="upload.id">
        <img :src="api.defaults.baseURL + upload.upload_url" style="width:200px;">
      </div>
    </div>

    <p>{{ post.date }}</p>
    <p>{{ post.author.email }}</p>
    <button v-if="post.author.id == auth.user.id" v-on:click="delete_post">Delete</button>

    <hr>

    <div v-if="auth.user">
      <p>{{ auth.user.email }}</p>
      <input type="text" v-model="comment_text" placeholder="Write comment">
      <button v-on:click="send_comment">Send</button>
    </div>

    <hr>
    
    <p>{{ post.comments }}</p>
    
    <hr>

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

async function delete_post() {
  const res = await api.delete(`/posts/${post_id}`)
  router.push('/posts')
}

let comment_text = ref("")
async function send_comment() {

  let form = new FormData()
  form.append("text", comment_text.value)

  const res = await api.post(`/posts/comments/${post_id}`, form)
  
  if (!post.value.comments) post.value.comments = []
  post.value.comments.push(res.data)

  comment_text.value = ""
}

</script>


<style scoped></style>

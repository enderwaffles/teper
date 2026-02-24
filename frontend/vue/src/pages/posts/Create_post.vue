<template>
  <Header />

  <div>
    <h1>Create post</h1>
  </div>

  <div>
    <input type="text" v-model="title" placeholder="Title">
    <input type="text" v-model="text" placeholder="Text">
    <input type="file" v-on:change="onFileChange">

    <button v-on:click="send">Send</button>
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
let title = ref("")
let text = ref("")
let file = ref(null)


//functions
function onFileChange(e) {
  file.value = e.target.files[0]
}

async function send() {

  let form = new FormData()
  form.append("title", title.value)
  form.append("text", text.value)
  if (file.value) {
    form.append("file", file.value)
  }

  const res = await api.post("/posts", form)
  router.push("/posts")
}

</script>


<style scoped>

</style>
